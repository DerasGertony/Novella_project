import pygame
import MessageClass

pygame.init()

screen = pygame.display.set_mode((1100,800))
clock = pygame.time.Clock()
btnEventId = {"RIGHT": 1073741903, "LEFT": 1073741904, "DOWN": 1073741905, "UP":1073741906}

WAIT_NEW_MSG_TIME = 3
WAIT_ANSWER_TIME = 5
FPS = 60

def rhythm_game_start():
    rhythmLine = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP"] # список клавиш, которые надо нажать
    task_num = 0

    msg = MessageClass.Message(screen)
    msg.show_Next_Symbol(rhythmLine[task_num])

    tick_update_msg = pygame.time.get_ticks()
    
    is_running = True
    while is_running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

            #Обработка нажатых клавиш
            if event.type == pygame.KEYDOWN:
                if not(msg.updating) and event.key == btnEventId[ rhythmLine[task_num] ]: # проверка на условие нажатая клавиша == ожидаемой клавише
                    print("Cool")

                    msg.updating = True
                    ticks_next_msg = pygame.time.get_ticks()
                    
                    msg.show_Next_Symbol("RIGHT_ANSWER")
                else:
                    msg.show_Next_Symbol("WRONG_ANSWER")
                    # -health
        try:
            if (pygame.time.get_ticks() - ticks_next_msg)//1000 == WAIT_NEW_MSG_TIME:
                task_num+=1

                msg.updating = False
                ticks_next_msg = None
                tick_update_msg = pygame.time.get_ticks()
                
                msg.show_Next_Symbol(rhythmLine[task_num])

        except:
            pass

        try:
            if (pygame.time.get_ticks() - tick_update_msg)//1000 == WAIT_ANSWER_TIME:
                msg.updating = True
                tick_update_msg = None
                ticks_next_msg = pygame.time.get_ticks()
                
                screen.fill((0,0,0))
        except:
            pass


        pygame.display.update()

rhythm_game_start()