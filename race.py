import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 50, 100
BUS_WIDTH, BUS_HEIGHT = 1.44 * CAR_WIDTH, 1.44 * CAR_HEIGHT
BUS_SPEED, CAR_SPEED = 4, 7
LANE_WIDTH = WIDTH // 3
MIN_DISTANCE = 100

# пунктирные линии

length_line = HEIGHT // 10
distance = HEIGHT // length_line * 3

RED = (255, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гони")

files_cars = ['images/blue_car.png', 'images/red_car.png']


# класс для максима
class Bus:
    def __init__(self):
        self.image = pygame.image.load('images/bus.png')
        self.image = pygame.transform.scale(self.image, (BUS_WIDTH, BUS_HEIGHT))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - BUS_HEIGHT - 10))
        self.lane = 1
        self.target_x = self.rect.x

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.lane > 0:
            self.lane -= 1
        if keys[pygame.K_RIGHT] and self.lane < 2:
            self.lane += 1

        self.target_x = self.lane * LANE_WIDTH + (LANE_WIDTH - BUS_WIDTH) // 2

        # насколько быстро автобус меняет свое местоположение по иксу
        if self.rect.x + BUS_SPEED < self.target_x:
            self.rect.x += BUS_SPEED
        elif self.rect.x - BUS_SPEED > self.target_x:
            self.rect.x -= BUS_SPEED
        else:
            self.rect.x = self.target_x


    def draw(self):
        screen.blit(self.image, self.rect)


# то от чего уворачиваемся
class Car:
    def __init__(self, lane):
        koef = random.randint(0, 1)
        self.image = pygame.image.load(files_cars[koef])
        if koef == 0:
            self.image = pygame.transform.rotozoom(self.image, 0, 0.12)
        else:
            self.image = pygame.transform.rotozoom(self.image, 0, 0.14)

        x_position = lane * LANE_WIDTH + LANE_WIDTH // 2

        self.rect = self.image.get_rect(center=(x_position, -CAR_HEIGHT))  # спавн как бы за экраном поэтому минус
        self.lane = lane

    def update(self):
        self.rect.y += CAR_SPEED  # скорость машин, чтобы повысить сложность можем увеличить этот параметр или фпс (переменная)

    def draw(self):
        screen.blit(self.image, self.rect)


def main():
    clock = pygame.time.Clock()
    bus = Bus()
    cars = []

    # пунктир
    line_position = -length_line

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

        for i in range(line_position + distance, HEIGHT + length_line, distance + length_line):
            pygame.draw.line(screen, WHITE, [WIDTH // 3, i - distance],
                             [WIDTH // 3, i - distance + length_line], 10)
            pygame.draw.line(screen, WHITE, [WIDTH // 3 * 2, i - distance],
                             [WIDTH // 3 * 2, i - distance + length_line], 10)

        line_position += 5 # обязательно число, которое делит 10 без остатка
        if line_position == distance:
            line_position = -length_line

        bus.draw()
        for car in cars:
            car.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
