#from map import map.mapping, map.world_map
import Functions.map as map
from const import *
import pygame


def ray_casting(sc, player_pos, player_angle, textures, window_w, window_h):
    ox, oy = player_pos
    xm, ym = map.mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV

    SCALE = window_w // NUM_RAYS
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # вертикали
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, window_w, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = map.mapping(x + dx, yv)
            if tile_v in map.world_map:
                texture_v = map.world_map[tile_v]
                # проверяем, падает ли взор на стену, если да - обрываем
                break
            x += dx * TILE

        # горизонтали
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, window_h, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = map.mapping(xh, y + dy)
            if tile_h in map.world_map:
                texture_h = map.world_map[tile_h]
                break
            y += dy * TILE

        # проекция
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle) # избавление от эффекта рыбьего глаза
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJ_COEFF / depth), 6 * window_h)

        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, window_h/2 - proj_height // 2))

        cur_angle += DELTA_ANGLE
