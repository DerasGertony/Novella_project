import pygame
RED = (255, 0, 0)

class ProgressBar:
    def __init__(self, screen, window_w, window_h):
        self.screen = screen
        self.height = window_h*0.05
        self.width = window_w*0.005
        self.window_w = window_w
        self.window_h = window_h

    def draw(self, new_width):
        self.width = new_width
        pygame.draw.rect(self.screen, RED, (self.window_w*0.33, self.window_h*0.9, self.width, self.height))