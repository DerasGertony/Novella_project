import pygame
from pygame import K_ESCAPE, KEYDOWN
from const import *
from draw import Draw
from player import Player


# чтобы менять сложность, будем изменять размер карты в map и время на прохождение
# инициализация
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Draw(sc, sc_map)


# запуск
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
    player.movement()
    drawing.back()
    drawing.walls(player.pos, player.angle)
    pygame.display.flip()
    clock.tick()