import pygame
from const import *
from ray_casting_func import ray_casting


class Draw:
    def __init__(self, sc, sc_map, time_finish):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True) # для таймера
        # под единицей картинка стен, под S - потолок/небо
        self.textures = {'1': pygame.image.load('wall.jpg').convert(),
                         'S': pygame.image.load('img.png').convert()
                         }
        self.time_finish = time_finish

    def back(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def walls(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)

    def timer(self, time_now):
        if self.time_finish - int(time_now) <= 0:
            pygame.quit() # тут окно проигрыша
        else:
            render = self.font.render(str(self.time_finish - int(time_now)), 0, DARKRED)
            w, h = pygame.display.get_surface().get_size()
            self.sc.blit(render, (w // 2 - 20,  5))