WIDTH_CAR_WINDOW, HEIGHT_CAR_WINDOW = 600, 800
FPS = 60
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

RED = (255, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)