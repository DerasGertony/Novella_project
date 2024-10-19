import math
import time

# время на прохождение в сек

delta_time = 120

# произвольно

WIDTH, HEIGHT = 1200, 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - 200)

# рей кастинг

FOV = math.pi / 3 # чем больше делитель тем ближе стены
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
TEXTURE_WIDTH = 200
TEXTURE_HEIGHT = 200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# настройки игрока

player_pos = (TILE * 1.5, TILE * 1.5)
player_angle = 0
player_speed = 1.7

# цвета

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKRED = (140, 0, 0)
DARKGRAY = (40, 40, 40)
FLOOR = (74, 70, 64)
SKY = (110, 184, 224)

cur_time = time.time_ns()

def freeze():
    global cur_time
    delta = (time.time_ns() - cur_time)/ 1000000000
    cur_time = time.time_ns()
    return delta