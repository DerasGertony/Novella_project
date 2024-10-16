import pygame
RED = (255, 0, 0)

class ProgressBar:
    def __init__(self, screen):
        self.screen = screen
        self.height = 40
        self.width = 5

    def draw(self, new_width):
        self.width = new_width
        pygame.draw.rect(self.screen, RED, (275, 750, self.width, self.height))