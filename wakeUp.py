import pygame
import ProgressBarClass

pygame.init()
screen = pygame.display.set_mode((1100,800))
btnEventId = {"SPACE": 32}

FPS = 60

def wakeUp():
    clock = pygame.time.Clock()
    clicks = 5
    time_minusProgress = set()
    time_minusProgress_after_n_sec = set()

    progress = ProgressBarClass.ProgressBar(screen)
    progress.draw(0)

    is_running = True
    while is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == btnEventId["SPACE"]:
                clicks+=1

        second_now = pygame.time.get_ticks()//1000
        if second_now > 0 and second_now not in time_minusProgress:
            clicks-=1
            time_minusProgress.add(second_now)

        if second_now > 0 and (second_now)%5 == 0 and second_now not in time_minusProgress_after_n_sec:
            clicks-=5
            time_minusProgress_after_n_sec.add(second_now)
        print(clicks)

        screen.fill((0,0,0))

        progress.draw(clicks*5)

        pygame.display.update()

        if clicks>=100:
            print("WAKE UP, BRO! \nBREATH AIR!")
            is_running = False
            pygame.quit()

        elif clicks <= 0:
            print("YOUR ARE SLEEPING, BRO! \nTRY ANOTHER ROUND!")
            is_running = False
            pygame.quit()

wakeUp()