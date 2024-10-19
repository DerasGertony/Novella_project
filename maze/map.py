from const import TILE
import pygame


text_map = [
    '111111111111111111111111',
    '1........111....1.1....1',
    '111111.1.....11.1...11.1',
    '1......11.11111.1.1.11.1',
    '1.1........11.1...1.1111',
    '1.1111111..11.11111.1..1',
    '1.11.......11..11...1..1',
    '1..1.1.1111111.11.111..1',
    '1111.1....1.........1111',
    '1....1.11...1.11111...11',
    '111111.111111.1...11...1',
    '11...111...11...1..111.1',
    '11.1.....1....1111.....1',
    '11W111111111111111111111'
]

# W - win, конец лабиринта

world_map = {}
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == 'W':
                world_map[(i * TILE, j * TILE)] = 'W'


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE