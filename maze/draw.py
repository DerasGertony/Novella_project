import pygame
from const import *
from ray_casting_func import ray_casting


class Draw:
    def __init__(self, sc, sc_map):
        self.sc_map = sc_map
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    # бэкграунд пол небо
    def back(self):
        pygame.draw.rect(self.sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def walls(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)


    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                               map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        self.sc.blit(self.sc_map, MAP_POS)
