# Imports
import sys
import pygame
from ld_images import *

# Configuration
pygame.init()
fps = 10
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
game_started = False
font = pygame.font.SysFont('Arial', 40)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text, font,fc, image, size, where):
        pygame.sprite.Sprite.__init__(self)
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
        image = pygame.transform.scale(image, (width, height))
        self.image = image
        self.rect = self.image.get_rect(center=(width / 2, height / 2))


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
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

butns = []
backs = []
heroes = []


def level(num):
    return 1









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