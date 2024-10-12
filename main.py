# Imports
import sys
import pygame
from ld_images import *

# Configuration
pygame.init()
fps = 10
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
pygame.display.set_caption('HSE! STUDENT! LIFE!')
screen = pygame.display.set_mode((width, height))
game_started = False
font = pygame.font.SysFont('Arial', 40)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text, font,fc, image, size, where):
        pygame.sprite.Sprite.__init__(self)
        if image == ex:
            image.set_alpha(255)
        image = pygame.transform.scale(image, size)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.buttonText = font.render(text, True, fc)
        self.where = where

    def use(self):
        return self.where


class BackGround(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        if image != startback and image != dg:
            image.set_alpha(250)
        image = pygame.transform.smoothscale(image, (width, height))
        self.image = image
        self.rect = self.image.get_rect(center=(width / 2, height / 2))


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, image, size):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.transform.scale(image, size)
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))


use_sprites = pygame.sprite.Group()  # interactive sprites
dec_sprites = pygame.sprite.Group()
# starting screen
back = BackGround(startback)
st1 = Button([width / 4, height / 2 + 50], 's', font, (0, 0, 0),sb1, (808, 152), (1,1))
st2 = Button([width/4 +10, height/2 +200], '', font, (0,0,0),sb2,(804, 151), (2,1))
st3 = Button([width/4, height/2 + 350], '', font, (0,0,0),sb3,(800, 150), (3,1))
use_sprites.add(st1)
use_sprites.add(st2)
use_sprites.add(st3)
dec_sprites.add(back)

butns = {}
backs = {}
heroes = {}


def level(num):
    if num == (0,0):
        exit(0)
    use_sprites.empty()
    dec_sprites.empty()
    pygame.display.flip()
    back = BackGround(bus)
    dec_sprites.add(back)
    dec_sprites.add(BackGround(dg))
    use_sprites.add(Button([150, 50], '', font, (0, 0, 0), bc, (300, 80), (num[0], num[1]-1)))
    use_sprites.add(Button([width - 150, 50], '', font, (0, 0, 0), sk, (300, 80), (num[0],num[1]+1)))
    use_sprites.add(Button([width/2, 60], '', font, (0, 0, 0), ex, (300, 120), (0,0)))




#dialogue window
#back = BackGround()
#hero = Hero()

clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in use_sprites:
                if sprite.rect.collidepoint(event.pos):
                    level(sprite.use())
    dec_sprites.update()
    use_sprites.update()
    screen.fill((0, 0, 0))
    dec_sprites.draw(screen)
    use_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)