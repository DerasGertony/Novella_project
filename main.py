import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 50, 100
LANE_WIDTH = WIDTH // 3

RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гони")


# класс максима
class Bus:
    def __init__(self):
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - CAR_HEIGHT))
        self.lane = 1

    def move(self):
        keys = pygame.key.get_pressed()
        # for event in pygame.event.get():
        # мне не оч нравится что даблкликается но позже добавлю плавность
        # будто по диагонали начнем двигаться, тогда и мансить можно будет между линий
        if keys[pygame.K_LEFT] and self.lane > 0:
            self.lane -= 1
        if keys[pygame.K_RIGHT] and self.lane < 2:
            self.lane += 1

        self.rect.x = self.lane * LANE_WIDTH + (LANE_WIDTH - CAR_WIDTH) // 2

    def draw(self):
        screen.blit(self.image, self.rect)


# то от чего уворачиваемся
class Car:
    def __init__(self, lane):
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(RED)

        x_position = lane * LANE_WIDTH + LANE_WIDTH // 2

        self.rect = self.image.get_rect(center=(x_position, -CAR_HEIGHT))  # спавн как бы за экраном поэтому минус
        self.lane = lane

    def update(self):
        self.rect.y += 5  # скорость машин, чтобы повысить сложность можем увеличить этот параметр или фпс (переменная)

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
            cars.append(Car(lane_choice))

        for car in cars[:]:
            car.update()
            if car.rect.y > HEIGHT:
                cars.remove(car)

        for car in cars:
            if bus.rect.colliderect(car.rect):
                running = False

        screen.fill((255, 255, 255))
        bus.draw()
        for car in cars:
            car.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
