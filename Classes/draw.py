import pygame
from const import *
from Functions.ray_casting_func import ray_casting


class Draw:
    def __init__(self, sc, time_finish, window_w, window_h):
        self.sc = sc
        #self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True) # для таймера
        # под единицей картинка стен, W - финиш (win)
        self.textures = {'1': pygame.image.load('images/wall.png').convert(),
                         'W': pygame.image.load('images/finish.jpg').convert()
                         }
        self.time_finish = time_finish
        self.window_w = window_w
        self.window_h = window_h

    def back(self, angle):
        pygame.draw.rect(self.sc, BLACK, (0, 0, self.window_w, self.window_h/2))
        pygame.draw.rect(self.sc, FLOOR, (0, self.window_h/2, self.window_w, self.window_h/2))

    def walls(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures, self.window_w, self.window_h)

    def timer(self, time_now):
        if self.time_finish - int(time_now) <= 0:
            pygame.quit() # тут окно проигрыша
        else:
            render = self.font.render(str(self.time_finish - int(time_now)), 0, DARKRED)
            w, h = pygame.display.get_surface().get_size()
            self.sc.blit(render, (w // 2 - 20,  5))
