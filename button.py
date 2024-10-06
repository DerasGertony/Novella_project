# Imports
import sys
import pygame




class Button():

    def __init__(self, x, y, width, height,objects, font, c, fc,  buttonText='Button', lvl=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lvl = lvl

        self.alreadyPressed = False
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonText = font.render(buttonText, True, fc)

        self.fillColors = {
            'normal': c,
            'hover': (c[0]*1.2 , c[1]*1.2, c[2]*1.2),
            'pressed': (c[0]*0.8 , c[1]*0.8, c[2]*0.8),
        }
        objects.append(self)

    def process(self,screen):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                start(self.lvl)
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonText, [
            self.buttonRect.width / 2 - self.buttonText.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonText.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)