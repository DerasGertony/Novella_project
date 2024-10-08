import pygame
import Teacher

pygame.init()

screen = pygame.display.set_mode((1100,800))
btnEventId = {"RIGHT": 1073741903, "LEFT": 1073741904, "DOWN": 1073741905, "UP":1073741906}

def rhythm_game_start():
    rhythm_line = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP"] # список клавиш, которые надо нажать
    task_num = 0
    
    teacher = Teacher.Teacher(screen)

    is_Rhythm_Game_Running = 1
    while is_Rhythm_Game_Running:
        pygame.display.update()

        teacher.show_Next_Symbol(rhythm_line[task_num])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_Rhythm_Game_Running = 0
                pygame.quit()

            #Обработка нажатых клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == btnEventId[ rhythm_line[task_num] ]: # проверка на условие нажатая клавиша == ожидаемой клавише
                    print("Cool")
                    task_num+=1

                    teacher.delete_previous_Symbol()
                    teacher.show_Next_Symbol(rhythm_line[task_num])

                else:
                    print("Bad!")
                    #task_num+=1


rhythm_game_start()