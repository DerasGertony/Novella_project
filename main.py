import pygame

pygame.init()

rhythm_line = ["right", "left", "down", "down", "up"]
btnEventId = {"right": 1073741903, "left": 1073741904, "down": 1073741905, "up":1073741906}
task_num = 0

screen = pygame.display.set_mode((600,300))

#square = pygame.Surface((50,170))
#square.fill("blue")

is_Rhythm_Game_Running = 1
while is_Rhythm_Game_Running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_Rhythm_Game_Running = 0
            pygame.quit()
        print("Press ", rhythm_line[task_num])
        if event.type == pygame.KEYDOWN:
            if event.key == btnEventId[ rhythm_line[task_num] ]: # нажатая клавиша == ожидаемой клавише
                print("Cool")
                task_num+=1
            else:
                print("Bad!")
                #task_num+=1