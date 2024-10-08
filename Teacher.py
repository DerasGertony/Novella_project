import pygame

class Teacher:
    def __init__(self, screen):
        self.screen = screen

    def show_Next_Symbol(self, task_key): #отображаем символ, который надо нажать
        self.task_message = pygame.image.load(f'images/{task_key}.jpg') # изображение
        self.screen.blit(self.task_message, (400,500))

    def show_Wrong_Answer(self):
        pass
    def show_Right_Asnwer(self):
        pass
    def delete_previous_Symbol(self):
        pass