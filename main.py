import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 50, 100
LANE_WIDTH = WIDTH // 3
MIN_DISTANCE = 100
OTSTUP = 15 # слева и справа от дороги

RED = (255, 0, 0)
GREEN = (0, 128, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гони")

files_cars = ['images/blue_car.png', 'images/red_car.png']


# класс максима
class Bus:
    def __init__(self):
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill((0, 255, 0))
        # self.image = pygame.image.load('images/img_.png').convert()
        # self.image.set_colorkey((90, 90, 90))
        self.image = pygame.transform.scale(self.image, (1.3 * CAR_WIDTH, 1.3 * CAR_HEIGHT))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - CAR_HEIGHT - 10))
        self.lane = 1
        self.target_x = self.rect.x

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.lane > 0:
            self.lane -= 1
        if keys[pygame.K_RIGHT] and self.lane < 2:
            self.lane += 1

        self.target_x = self.lane * LANE_WIDTH + (LANE_WIDTH - CAR_WIDTH) // 2

        # насколько быстро автобус меняет свое местоположение по иксу
        if self.rect.x + 5 < self.target_x:
            self.rect.x += 5
        elif self.rect.x - 5 > self.target_x:
            self.rect.x -= 5
        else:
            self.rect.x = self.target_x


    def draw(self):
        screen.blit(self.image, self.rect)


# то от чего уворачиваемся
class Car:
    def __init__(self, lane):
        # self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        koef = random.randint(0, 1)
        self.image = pygame.image.load(files_cars[koef])
        if koef == 0:
            self.image = pygame.transform.rotozoom(self.image, 0, 0.13)
        else:
            self.image = pygame.transform.rotozoom(self.image, 0, 0.15)
        # self.image = pygame.transform.scale(self.image, (CAR_WIDTH, CAR_HEIGHT))

        x_position = lane * LANE_WIDTH + LANE_WIDTH // 2

        self.rect = self.image.get_rect(center=(x_position, -CAR_HEIGHT))  # спавн как бы за экраном поэтому минус
        self.lane = lane

    def update(self):
        self.rect.y += 7  # скорость машин, чтобы повысить сложность можем увеличить этот параметр или фпс (переменная)

    def draw(self):
        screen.blit(self.image, self.rect)


def main():
    clock = pygame.time.Clock()
    bus = Bus()
    cars = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bus.move()

        if random.randint(1, 40) == 1:  # частота появления машин (чем больше второе число - тем реже)
            lane_choice = random.randint(0, 2)
            if all(abs(car.rect.y + CAR_HEIGHT) >= MIN_DISTANCE for car in cars if car.lane == lane_choice):
                cars.append(Car(lane_choice))

        for car in cars[:]:
            car.update()
            if car.rect.y > HEIGHT:
                cars.remove(car)

        for car in cars:
            if bus.rect.colliderect(car.rect):
                running = False

        # отрисовка

        screen.fill((90, 90, 90))
        pygame.draw.rect(screen, GREEN, (0, 0, OTSTUP, HEIGHT))
        pygame.draw.rect(screen, GREEN, (WIDTH - OTSTUP, 0, WIDTH - OTSTUP, HEIGHT))
        pygame.draw.line(screen, (255, 255, 255), [OTSTUP, 0], [OTSTUP, HEIGHT], 4)
        pygame.draw.line(screen, (255, 255, 255), [WIDTH - OTSTUP, 0],
                         [WIDTH - OTSTUP, HEIGHT], 4)
        pygame.draw.line(screen, (255, 255, 255), [(WIDTH - OTSTUP * 2) / 3, 0],
                         [(WIDTH - OTSTUP * 2) / 3, HEIGHT], 4)
        pygame.draw.line(screen, (255, 255, 255), [(WIDTH - OTSTUP * 2) / 3 * 2, 0],
                         [(WIDTH - OTSTUP * 2) / 3 * 2, HEIGHT], 4)

        bus.draw()
        for car in cars:
            car.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
