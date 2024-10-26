import math
import time

# ---------------------------------
# переменные для лабиринта
# время на прохождение в сек

delta_time = 100

# произвольно

FPS = 30
TILE = 100
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE

# рей кастинг

FOV = math.pi / 3  # чем больше делитель тем ближе стены
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2 * DIST * TILE
TEXTURE_WIDTH = 200
TEXTURE_HEIGHT = 200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# настройки игрока

player_pos = (TILE * 1.5, TILE * 1.5)
player_angle = 0

# цвета

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKRED = (140, 0, 0)
DARKGRAY = (40, 40, 40)
FLOOR = (74, 70, 64)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

cur_time = time.time_ns()


def freeze():
    global cur_time
    delta = (time.time_ns() - cur_time) / 10000000000
    cur_time = time.time_ns()
    return delta


# -----------------------------------------------------
# переменные для гонок

CAR_WIDTH, CAR_HEIGHT = 100, 200
BUS_SCALE = 1.3  # во сколько раз автобус больше чем машины
BUS_WIDTH, BUS_HEIGHT = BUS_SCALE * CAR_WIDTH, BUS_SCALE * CAR_HEIGHT
BUS_SPEED, CAR_SPEED = 10, 16
MIN_DISTANCE = 140  # минимальное расстояние между машинами
WIN = 50  # столько машин надо преодолеть, чтобы выиграть

frequency = 40  # частота появления машин (чем больше число - тем реже)

#    |----------------------------------|
#    |    переменные для РИТМ ИГРЫ      |
#    |----------------------------------|

WIDTH_RYTHM_WINDOW, HEIGHT_RYTHM_WINDOW = 1100, 800
btnEventId = {"RIGHT": 1073741903, "LEFT": 1073741904, "DOWN": 1073741905, "UP": 1073741906, "SPACE": 32}

rhythmLine_1LVL = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP"]  # список клавиш, которые надо  (1LVL)
setting_rythm_1lvl = (5, 3, 5, rhythmLine_1LVL)  # healt_points, wait_new_msg, wait_answer

rhythmLine_2LVL = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP", "DOWN", "RIGHT", "LEFT"]  # список клавиш, которые надо  (1LVL)
setting_rythm_2lvl = (3, 2, 3, rhythmLine_1LVL)  # healt_points, wait_new_msg, wait_answer

rhythmLine_3LVL = ["RIGHT", "LEFT", "DOWN", "DOWN", "UP", "RIGHT", "LEFT", "DOWN", "UP", "LEFT", "RIGHT"]  # список клавиш, которые надо  (3LVL)
setting_rythm_3lvl = (2, 1, 2, rhythmLine_1LVL)  # healt_points, wait_new_msg, wait_answer

#    |----------------------------------|
#    |  переменные для ПРОСЫПАШКИ ИГРЫ  |
#    |----------------------------------|

WIDTH_WAKEUP_WINDOW, HEIGHT_WAKEUP_WINDOW = 1100, 800
setting_wakeup_1lvl = (1, 5)  # уменьшение прогресса каждую секунду, уменьшение прогресса через 5сек
setting_wakeup_2lvl = (2, 7)
setting_wakeup_3lvl = (3, 10)
