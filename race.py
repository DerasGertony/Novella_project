import pygame
import random
from const import *
from bus import Bus
from car import Car

pygame.init()


def start_race():
    screen = pygame.display.set_mode((WIDTH_CAR_WINDOW, HEIGHT_CAR_WINDOW))
    pygame.display.set_caption("Гони")

    files_cars = ['images/blue_car.png', 'images/red_car.png']
    clock = pygame.time.Clock()
    bus = Bus(screen)
    cars = []
    count_cars = 0

    # пунктир
    line_position = -length_line

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bus.move()

        if random.randint(1, frequency) == 1:
            lane_choice = random.randint(0, 2)
            if (all(abs(car.rect.y + CAR_HEIGHT) >= MIN_DISTANCE for car in cars if car.lane == lane_choice)
                    and count_cars < WIN): # для условия победы
                count_cars += 1 # количество машин
                cars.append(Car(lane_choice, files_cars, screen))

        for car in cars[:]:
            car.update()
            if car.rect.y > HEIGHT_CAR_WINDOW:
                cars.remove(car)

        for car in cars:
            if bus.rect.colliderect(car.rect):
                running = False

        # отрисовка
        screen.fill((90, 90, 90))

        for i in range(line_position + distance, HEIGHT_CAR_WINDOW + length_line, distance + length_line):
            pygame.draw.line(screen, WHITE, [WIDTH_CAR_WINDOW // 3, i - distance],
                             [WIDTH_CAR_WINDOW // 3, i - distance + length_line], 10)
            pygame.draw.line(screen, WHITE, [WIDTH_CAR_WINDOW // 3 * 2, i - distance],
                             [WIDTH_CAR_WINDOW // 3 * 2, i - distance + length_line], 10)

        line_position += 5 # обязательно число, которое делит 10 без остатка
        if line_position == distance:
            line_position = -length_line

        bus.draw()
        for car in cars:
            car.draw()

        pygame.display.flip()
        clock.tick(FPS)

        if count_cars == WIN and not cars:
            pygame.quit()
            break

    pygame.quit()


start_race()
