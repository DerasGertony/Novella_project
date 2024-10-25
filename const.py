import math
import time

# ---------------------------------
# переменные для лабиринта
# время на прохождение в сек

delta_time = 100

# произвольно

WIDTH_MAZE_WINDOW, HEIGHT_MAZE_WINDOW = 1200, 800
HALF_WIDTH = WIDTH_MAZE_WINDOW // 2
HALF_HEIGHT = HEIGHT_MAZE_WINDOW // 2
FPS = 60
TILE = 100
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE

# рей кастинг

FOV = math.pi / 3 # чем больше делитель тем ближе стены
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2 * DIST * TILE
SCALE = WIDTH_MAZE_WINDOW // NUM_RAYS
TEXTURE_WIDTH = 200
TEXTURE_HEIGHT = 200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# настройки игрока

player_pos = (TILE * 1.5, TILE * 1.5)
player_angle = 0
player_speed = 6

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
    delta = (time.time_ns() - cur_time) / 1000000000
    cur_time = time.time_ns()
    return delta

# -----------------------------------------------------
# переменные для гонок

WIDTH_CAR_WINDOW, HEIGHT_CAR_WINDOW = 600, 800
CAR_WIDTH, CAR_HEIGHT = 50, 100
BUS_SCALE = 1.44 # во сколько раз автобус больше чем машины
BUS_WIDTH, BUS_HEIGHT = BUS_SCALE * CAR_WIDTH, BUS_SCALE * CAR_HEIGHT
BUS_SPEED, CAR_SPEED = 4, 7
LANE_WIDTH = WIDTH_CAR_WINDOW // 3
MIN_DISTANCE = 100 # минимальное расстояние между машинами
WIN = 40 # столько машин надо преодолеть, чтобы выиграть

length_line = HEIGHT_CAR_WINDOW // 10 # длина пунктирной линии
distance = HEIGHT_CAR_WINDOW // length_line * 3 # расстояние между пунктирными линиями
frequency = 40 # частота появления машин (чем больше число - тем реже)