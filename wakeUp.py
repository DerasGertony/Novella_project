import pygame
import ProgressBarClass

pygame.init()

WIDTH, HEIGTH = 1100, 800

screen = pygame.display.set_mode((WIDTH,HEIGTH))
btnEventId = {"SPACE": 32}

FPS = 60

def wakeUp(minus_progress: int, minus_progress_5_sec: int):
    clock = pygame.time.Clock()
    clicks = 5
    time_minusProgress = set()
    time_minusProgress_5_sec = set()

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
            clicks -= minus_progress
            time_minusProgress.add(second_now)

        if second_now > 0 and (second_now)%5 == 0 and second_now not in time_minusProgress_5_sec:
            clicks -= minus_progress_5_sec
            time_minusProgress_5_sec.add(second_now)

        screen.fill((0,0,0))

        room_image_background = pygame.image.load(f"./images/{clicks//10}0_progress.jpg").convert()
        room_image_background = pygame.transform.scale(room_image_background, (WIDTH, HEIGTH))
        screen.blit(room_image_background, (0,0))

        press_space = pygame.font.SysFont('arial', 20)
        text_message = press_space.render("Нажимайте SPACE, чтобы увеличивать шкалу прогресса", False, (255,255,255))
        screen.blit(text_message, (260, 700))

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

wakeUp(minus_progress=1, minus_progress_5_sec=5)