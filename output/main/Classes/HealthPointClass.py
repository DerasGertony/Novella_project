import pygame

class HP:
    def __init__(self, screen, x_cord, y_cord, window_w, window_h):
        self.screen = screen
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.window_w = window_w
        self.window_h = window_h

    def draw(self):
        self.health = pygame.image.load("./images/HEART.png").convert_alpha()
        self.health = pygame.transform.scale(self.health, (self.window_w*0.1, self.window_w*0.1))
        self.screen.blit(self.health, (self.x_cord, self.y_cord))