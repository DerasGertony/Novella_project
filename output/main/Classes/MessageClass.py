import pygame

X_CORD_KEY_TASK_MESSAGE = 570
Y_CORD_KEY_TASK_MESSAGE = 150

class Message:
    def __init__(self, screen, window_w, window_h):
        self.screen = screen
        self.updating = False
        self.window_w = window_w
        self.window_h = window_h

    def draw_Symbol(self, task_key): #отображаем символ, который надо нажать
        self.task_message = pygame.image.load(f'images/{task_key}.png').convert_alpha() # создание изображения
        self.task_message = pygame.transform.scale(self.task_message, (self.window_w*0.1, self.window_w*0.1))
        self.screen.blit(self.task_message, (self.window_w*0.51, self.window_h*0.19))