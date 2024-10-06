# Imports
import sys
import pygame
from button import Button
# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('ANGST', 40)


obj = []





Button(30, 30, 400, 100,obj,font, 'Button One (onePress)', print)
Button(30, 140, 400, 100,obj,font, 'Button Two (multiPress)', print, True)

while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in obj:
        object.process(screen)
    pygame.display.flip()
    fpsClock.tick(fps)