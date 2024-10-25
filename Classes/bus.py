from const import *
import pygame


# класс для максима
class Bus:
    def __init__(self, screen, window_w, window_h, LANE_WIDTH):
        self.image = pygame.image.load('images/bus.png')
        self.image = pygame.transform.scale(self.image, (BUS_WIDTH, BUS_HEIGHT))
        self.rect = self.image.get_rect(center=(window_w // 2, window_h - BUS_HEIGHT - 10))
        self.lane = 1
        self.target_x = self.rect.x
        self.screen = screen
        self.LANE_WIDTH = LANE_WIDTH

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.lane > 0:
            self.lane -= 1
        if keys[pygame.K_RIGHT] and self.lane < 2:
            self.lane += 1

        self.target_x = self.lane * self.LANE_WIDTH + (self.LANE_WIDTH - BUS_WIDTH) // 2

        # насколько быстро автобус меняет свое местоположение по иксу
        if self.rect.x + BUS_SPEED < self.target_x:
            self.rect.x += BUS_SPEED
        elif self.rect.x - BUS_SPEED > self.target_x:
            self.rect.x -= BUS_SPEED
        else:
            self.rect.x = self.target_x


    def draw(self):
        self.screen.blit(self.image, self.rect)