from const import *
import pygame
import random


# то от чего уворачиваемся
class Car:
    def __init__(self, lane, files_cars, screen, LANE_WIDTH):
        koef = random.randint(0, 1)
        self.image = pygame.image.load(files_cars[koef])
        # if koef == 0:
        #     self.image = pygame.transform.rotozoom(self.image, 0, ())
        # else:
        self.image = pygame.transform.scale(self.image, (CAR_WIDTH, CAR_HEIGHT))

        x_position = lane * LANE_WIDTH + LANE_WIDTH // 2

        self.rect = self.image.get_rect(center=(x_position, -CAR_HEIGHT))  # спавн как бы за экраном поэтому минус
        self.lane = lane
        self.screen = screen

    def update(self):
        self.rect.y += CAR_SPEED  # скорость машин, чтобы повысить сложность, можем увеличить этот параметр или фпс (переменная)

    def draw(self):
        self.screen.blit(self.image, self.rect)