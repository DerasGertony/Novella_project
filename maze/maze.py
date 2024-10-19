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
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
player = Player()
time_finish = int(time.time() + delta_time)
drawing = Draw(sc, sc_map, time_finish)

# запуск
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
    # проверка на прохождение, коэффициенты зависимо от карты
    ox, oy = player.pos
    if TILE * 2 <= ox <= TILE * 3 and TILE * 12.5 <= oy <= TILE * 14:
        pygame.quit()
        break
    player.movement()
    drawing.back(player.angle)
    drawing.walls(player.pos, player.angle)
    drawing.timer(time.time())
    pygame.display.flip()
    clock.tick()