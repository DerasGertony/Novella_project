import pygame

pygame.init()
screen = pygame.display.set_mode((1100,800))
btnEventId = {"SPACE": 32}

FPS = 60

def wakeUp():
    is_running = True
    clock = pygame.time.Clock()
    count = 0

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == btnEventId["SPACE"]:
                count+=1
        print(count)

        pygame.display.update()

wakeUp()