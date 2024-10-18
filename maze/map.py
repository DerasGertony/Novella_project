from const import TILE, MAP_TILE
import pygame


text_map = [
    '111111111111',
    '1......1...1',
    '111111.....1',
    '1......11.11',
    '1.......1..1',
    '1.......1..1',
    '1..1.......1',
    '111111111111'
]

world_map = {}
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE