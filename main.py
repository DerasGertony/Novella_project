# Imports
import sys
import pygame
from ld_images import *
from pyplot import *

# Configuration
pygame.init()
info = pygame.display.Info()
fps = 10
fpsClock = pygame.time.Clock()
pygame.display.set_caption('HSE! STUDENT! LIFE!')
width = info.current_w
height = info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.SCALED)
game_started = False
font = pygame.font.SysFont('Montserrat Regular', 30)
nm = (0, 0)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text, font, fc, image, size, where):
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
st1 = Button([width / 4, height / 2 + 50], 's', font, (0, 0, 0), sb1, (808, 152), (1, 0, 0))
st2 = Button([width / 4 + 10, height / 2 + 200], '', font, (0, 0, 0), sb2, (804, 151), (2, 0, 0))
st3 = Button([width / 4, height / 2 + 350], '', font, (0, 0, 0), sb3, (800, 150), (3, 0, 0))
use_sprites.add(st1)
use_sprites.add(st2)
use_sprites.add(st3)
dec_sprites.add(back)

butns = {}
backs = {}
heroes = {}


def blit_text(surface, text, pos, font, color=pygame.Color('gray')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()[0] - 150, surface.get_size()[1]
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


def level(num):
    global nm
    use_sprites.empty()
    dec_sprites.empty()
    nm = num
    if num == (0, 0):
        exit(0)
    if num == (-1, 0):
        back = BackGround(busted)
        dec_sprites.add(back)
        return 0
    if num == (-1, 1):
        back = BackGround(good)
        dec_sprites.add(back)
        return 0
    pygame.display.flip()
    back = BackGround(bus)
    dec_sprites.add(back)
    dlg = BackGround(dg)
    dec_sprites.add(dlg)
    frw = Button([width - 150, 50], '', font, (0, 0, 0), sk, (300, 80), (num[0], num[1], min(mx[(num[0], num[1])], num[2] + 1)))
    bck = Button([150, 50], '', font, (0, 0, 0), bc, (300, 80), (num[0], num[1], max(num[2] - 1, 0)))
    exi = Button([width / 2, 60], '', font, (0, 0, 0), ex, (300, 120), (0, 0))
    use_sprites.add(bck)
    use_sprites.add(frw)
    use_sprites.add(exi)
    if num[2] == mx[num[0], num[1]] and num not in finale.keys():
        ch1 = Button([width - width / 6, 670], '', font, (0, 0, 0), ex, (600, 50), btn[num[0], num[1], 1][1])
        ch2 = Button([width - width / 6, 750], '', font, (0, 0, 0), ex, (600, 50), btn[num[0], num[1], 2][1])
        use_sprites.add(ch1)
        use_sprites.add(ch2)
        textpos = (0, 10)
        blit_text(ch1.image, btn[num[0], num[1], 1][0], textpos, font)
        textpos = (0, 10)
        blit_text(ch2.image, btn[num[0], num[1], 2][0], textpos, font)
    if num in finale.keys():
        ch1 = Button([width - width / 6, 670], '', font, (0, 0, 0), ex, (600, 50), (-1, finale[num]))
        use_sprites.add(ch1)
        textpos = (0, 10)
        blit_text(ch1.image, 'THe EnD', textpos, font)

    textpos = (220, 835)
    blit_text(dlg.image, text[num], textpos, font)


# dialogue window
# back = BackGround()
# hero = Hero()
temp = 0
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
                    sprite.image.set_alpha(50)
                    temp = sprite
        elif event.type == pygame.MOUSEBUTTONUP and temp:
            level(temp.use())
            temp = 0
        elif event.type == pygame.KEYDOWN:
            if nm[0] == -1:
                exit(0)
            if event.key == pygame.K_RIGHT:
                print(nm)
                if nm != (0, 0):
                    level((nm[0], nm[1], min(mx[(nm[0], nm[1])], nm[2] + 1)))
            if event.key == pygame.K_LEFT:
                print(nm)
                if nm != (0, 0):
                    level((nm[0], nm[1], max(nm[2] - 1, 0)))

    dec_sprites.update()
    use_sprites.update()
    screen.fill((0, 0, 0))
    dec_sprites.draw(screen)
    use_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
