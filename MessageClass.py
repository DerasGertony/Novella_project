import pygame

X_CORD_KEY_TASK_MESSAGE = 400
Y_CORD_KEY_TASK_MESSAGE = 500

class Message:
    def __init__(self, screen):
        self.screen = screen
        self.updating = False

    def show_Next_Symbol(self, task_key): #отображаем символ, который надо нажать
        self.task_message = pygame.image.load(f'images/{task_key}.jpg').convert() # создание изображения
        self.screen.blit(self.task_message, (X_CORD_KEY_TASK_MESSAGE, Y_CORD_KEY_TASK_MESSAGE))