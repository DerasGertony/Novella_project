from map import mapping, world_map
from const import *
from pygame import draw


def ray_casting(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE
        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE
        # projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        if depth != 0:
            proj_height = PROJ_COEFF / depth
        else:
            proj_height = PROJ_COEFF
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c // 2, c // 3)
        draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE
