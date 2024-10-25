import pygame

X_CORD_KEY_TASK_MESSAGE = 570
Y_CORD_KEY_TASK_MESSAGE = 150

class Message:
    def __init__(self, screen):
        self.screen = screen
        self.updating = False

    def draw_Symbol(self, task_key): #отображаем символ, который надо нажать
        self.task_message = pygame.image.load(f'images/{task_key}.png').convert_alpha() # создание изображения
        self.screen.blit(self.task_message, (X_CORD_KEY_TASK_MESSAGE, Y_CORD_KEY_TASK_MESSAGE))