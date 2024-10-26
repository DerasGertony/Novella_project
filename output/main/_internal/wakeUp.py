import pygame
import const
import Classes.ProgressBarClass as ProgressBarClass

pygame.init()


def wakeUp(screen, window_w, window_h):
    minus_progress, minus_progress_5_sec = 1, 5

    # screen = pygame.display.set_mode((const.WIDTH_WAKEUP_WINDOW, const.HEIGHT_WAKEUP_WINDOW))
    clock = pygame.time.Clock()

    clicks = 15
    time_minusProgress = set()
    time_minusProgress_5_sec = set()

    progress = ProgressBarClass.ProgressBar(screen, window_w, window_h)
    progress.draw(0)

    is_running = True
    while is_running:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN and event.key == const.btnEventId["SPACE"]:
                clicks += 1

        second_now = pygame.time.get_ticks() // 1000
        if second_now > 0 and second_now not in time_minusProgress:
            clicks -= minus_progress
            time_minusProgress.add(second_now)

        if second_now > 0 and (second_now) % 5 == 0 and second_now not in time_minusProgress_5_sec:
            clicks -= minus_progress_5_sec
            time_minusProgress_5_sec.add(second_now)

        room_image_background = pygame.image.load(f"./images/{abs(clicks) // 10}0_progress.jpg").convert()
        room_image_background = pygame.transform.scale(room_image_background, (window_w, window_h))
        screen.blit(room_image_background, (0, 0))

        press_space = pygame.font.SysFont('arial', 20)
        text_message = press_space.render("Нажимайте SPACE, чтобы увеличивать шкалу прогресса", False, (255, 255, 255))
        screen.blit(text_message, (window_w * 0.3, window_h * 0.8))

        progress.draw(clicks * 5)

        pygame.display.update()

        if clicks >= 100:  # WIN
            is_running = False

        elif clicks <= 0:  # LOSE
            is_running = False

# wakeUp(const.setting_wakeup_1lvl)
