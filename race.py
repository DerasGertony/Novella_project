import pygame
import random
from const import *
from Classes.bus import Bus
from Classes.car import Car

pygame.init()


def start_race(screen, window_w, window_h):
    # screen = pygame.display.set_mode((WIDTH_CAR_WINDOW, HEIGHT_CAR_WINDOW))
    pygame.display.set_caption("Гони")
    LANE_WIDTH = window_w // 3

    length_line = window_h // 5  # длина пунктирной линии
    distance = length_line  # расстояние между пунктирными линиями

    files_cars = ['images/blue_car.png', 'images/red_car.png']
    clock = pygame.time.Clock()
    bus = Bus(screen, window_w, window_h, LANE_WIDTH)
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
                    and count_cars < WIN):  # для условия победы
                count_cars += 1  # количество машин
                cars.append(Car(lane_choice, files_cars, screen, LANE_WIDTH))

        for car in cars[:]:
            car.update()
            if car.rect.y > window_h:
                cars.remove(car)

        for car in cars:
            if bus.rect.colliderect(car.rect):
                running = False

        # отрисовка
        screen.fill((90, 90, 90))

        for i in range(line_position + distance, window_h + length_line, distance + length_line):
            pygame.draw.line(screen, WHITE, [window_w // 3, i - distance],
                             [window_w // 3, i - distance + length_line], 15)
            pygame.draw.line(screen, WHITE, [window_w // 3 * 2, i - distance],
                             [window_w // 3 * 2, i - distance + length_line], 15)

        line_position += 10  # обязательно число, которое делит 10 без остатка
        if line_position > distance:
            line_position = -length_line

        bus.draw()
        for car in cars:
            car.draw()

        pygame.display.flip()
        clock.tick(FPS)

        if count_cars == WIN and not cars:
            break
