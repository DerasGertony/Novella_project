import math

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
NUM_RAYS = 350 # было 300, можно менять
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
TEXTURE_WIDTH = 512
TEXTURE_HEIGHT = 512
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# настройки игрока

player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 1

# цвета

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKRED = (140, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
YELLOW = (220, 220, 0)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)