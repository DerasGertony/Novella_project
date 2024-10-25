import pygame
import const
import Classes.MessageClass as MessageClass
import Classes.HealthPointClass as HealthPointClass

pygame.init()

def rhythm_game_start(args):
    healt_points, wait_new_msg, wait_answer, rythm_line = args

    screen = pygame.display.set_mode((const.WIDTH_RYTHM_WINDOW, const.HEIGHT_RYTHM_WINDOW))
    clock = pygame.time.Clock()

    backgroud = pygame.image.load("./images/rhythm_background.jpg").convert()
    backgroud = pygame.transform.scale(backgroud, (const.WIDTH_RYTHM_WINDOW, const.HEIGHT_RYTHM_WINDOW))
    screen.blit(backgroud, (0,0))
    
    WAIT_NEW_MSG_TIME = wait_new_msg # время до отображения нового сообщения
    WAIT_ANSWER_TIME = wait_answer # время ожидания ответа

    task_num = 0 # номер задания в настоящий момент

    HP = [] # массив с классами "сердца"
    hp_x_cord = 20
    hp_y_cord = 20

    for _ in range(healt_points): # заполнение массива
        HP.append(HealthPointClass.HP(screen, hp_x_cord, hp_y_cord))
        hp_x_cord+= 40

    msg = MessageClass.Message(screen)
    msg.draw_Symbol(rythm_line[task_num])

    tick_update_msg = pygame.time.get_ticks() # получение тиков в данный момент
    
    is_running = True
    while is_running:

        clock.tick(const.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

            #Обработка нажатых клавиш
            if event.type == pygame.KEYDOWN:
                if not(msg.updating) and event.key == const.btnEventId[ rythm_line[task_num] ]: # проверка на условие нажатая клавиша == ожидаемой клавише
                    print("Cool")

                    msg.updating = True
                    tick_update_msg = None
                    ticks_next_msg = pygame.time.get_ticks()
                    
                    msg.draw_Symbol("RIGHT_ANSWER")
                else:
                    msg.draw_Symbol("WRONG_ANSWER")
                    HP.pop() # удаление сердца за неправильный ответ
        
        # Если с момента Правильного ответа прошло WAIT_NEW_MSG_TIME, то отображаем новую карточку с заданием
        try: 
            if (pygame.time.get_ticks() - ticks_next_msg)//1000 == WAIT_NEW_MSG_TIME:
                msg.updating = False
                ticks_next_msg = None
                tick_update_msg = pygame.time.get_ticks()
                
                task_num+=1

        except:
            pass

        # Если мы ждём ответ WAIT_ANSWER_TIME, то убираем карточку и запускаем процесс отображения новой
        try:
            if (pygame.time.get_ticks() - tick_update_msg)//1000 == WAIT_ANSWER_TIME:
                msg.updating = True
                tick_update_msg = None
                ticks_next_msg = pygame.time.get_ticks()
                
                HP.pop() # удаление сердца за неправильный ответ

        except:
            pass

        screen.blit(backgroud, (0,0))
        
        if not(msg.updating):
            msg.draw_Symbol(rythm_line[task_num])


        if len(HP) == 0:
            pygame.display.update()
            is_running = False

            pygame.quit()
        else:
            for i in range(len(HP)): # отрисовка сердец
                HP[i].draw()
        
        pygame.display.update()
        

# rhythm_game_start(const.setting_rythm_1lvl)