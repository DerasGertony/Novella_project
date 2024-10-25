import pygame

class HP:
    def __init__(self, screen, x_cord, y_cord):
        self.screen = screen
        self.x_cord = x_cord
        self.y_cord = y_cord

    def draw(self):
        self.health = pygame.image.load("./images/HEART.png").convert_alpha()
        self.screen.blit(self.health, (self.x_cord, self.y_cord))