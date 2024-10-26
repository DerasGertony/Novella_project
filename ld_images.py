import sys
import pygame

busted = pygame.image.load('Pictures/badend.png')
good = pygame.image.load('Pictures/goodend.png')
btup = pygame.image.load('Pictures/btnsup.png')
btdn = pygame.image.load('Pictures/btnsdn.png')
tsk = pygame.image.load('Pictures/tsk.png')
# Backs
startback = pygame.image.load('images/stbc.jpg')
bus = pygame.image.load('Pictures/backgrounds/bus/3.jpg')
home = pygame.image.load('images/stbc.jpg')
bed = pygame.image.load('images/stbc.jpg')

# Buttons
sb1 = pygame.image.load('images/Group 198.png')
sb2 = pygame.image.load('images/Group 199.png')
sb3 = pygame.image.load('images/Group 200.png')

# dg window
dg = pygame.image.load('images/dgf.png')
ex = pygame.image.load('images/btexit.png')
sk = pygame.image.load('images/btfr.png')
bc = pygame.image.load('images/btbc.png')

# Heroes
gm_good = pygame.image.load('Pictures/characters/кокет бабка.png')
gm_angry = pygame.image.load('Pictures/characters/злой бабка((.png')
qr = pygame.image.load('Pictures/characters/квадробер.png')
gop_normal1 = pygame.image.load('Pictures/characters/гопник 1 нормис.png')
gop_normal2 = pygame.image.load('Pictures/characters/гопник 2 нормис.png')
gop_friendly1 = pygame.image.load('Pictures/characters/гопник 1 добри.png')
gop_friendly2 = pygame.image.load('Pictures/characters/гопник 2 добри.png')
biv_ild = pygame.image.load('Pictures/characters/биван ильдягин.png')
ser_depression = pygame.image.load('Pictures/characters/дипрессия козла сергеевича.png')
sh_friendly = pygame.image.load('Pictures/characters/добри шалья ильявин)).png')
sh_angry = pygame.image.load('Pictures/characters/злой шалья илявин((.jpg')
bi_sigma = pygame.image.load('Pictures/characters/игорь борисович сигма с шаурмой.png')
ser_normal = pygame.image.load('Pictures/characters/ser_normal.png')
sh_friendly = pygame.image.load('Pictures/characters/добри шалья ильявин)).png')
sh_angry = pygame.image.load('Pictures/characters/злой шалья илявин((.jpg')
bi_sigma = pygame.image.load('Pictures/characters/игорь борисович сигма с шаурмой.png')

# BackGrounds
# BUS
bus1 = pygame.image.load('Pictures/backgrounds/bus/1.jpg')
bus2 = pygame.image.load('Pictures/backgrounds/bus/2.jpg')
bus3 = pygame.image.load('Pictures/backgrounds/bus/3.jpg')
busout = pygame.image.load('Pictures/backgrounds/bstop.jpg')
math = pygame.image.load('Pictures/backgrounds/matan.jpg')
table = pygame.image.load('Pictures/backgrounds/tv.png')
vok = pygame.image.load('Pictures/backgrounds/vinside.jpg')
ener = pygame.image.load('Pictures/backgrounds/drugs.jpg')
sort = pygame.image.load('Pictures/backgrounds/mansion.jpg')
met = pygame.image.load('Pictures/backgrounds/метро-.jpg')
# HOME
alarm = pygame.image.load('Pictures/backgrounds/home/alarm.png')
kitchen = pygame.image.load('Pictures/backgrounds/home/kitchen.png')
phone = pygame.image.load('Pictures/backgrounds/home/phone.png')
mainbg = pygame.image.load('Pictures/backgrounds/home/main_back.png')
magas = pygame.image.load('Pictures/backgrounds/пятерочка.png')
kond = pygame.image.load('Pictures/backgrounds/kond.jpg')
tt = pygame.image.load('Pictures/backgrounds/phone/tt.jpg')
# OUTSIDE
CrowdedModernStreet = pygame.image.load('Pictures/backgrounds/outside/3.jpg')
CrowdedStreet = pygame.image.load('Pictures/backgrounds/outside/5.jpg')
DesertedDarknessStreet = pygame.image.load('Pictures/backgrounds/outside/4.jpg')
DesertedSunnyStreet = pygame.image.load('Pictures/backgrounds/outside/1.jpg')
DesertedRadiantStreet = pygame.image.load('Pictures/backgrounds/outside/2.jpg')
airp = pygame.image.load('Pictures/backgrounds/zdv.jpg')
tick = pygame.image.load('Pictures/backgrounds/билет.png')
car = pygame.image.load('Pictures/backgrounds/car.jpg')
hosp = pygame.image.load('Pictures/backgrounds/dead.jpg')
shav = pygame.image.load('Pictures/backgrounds/shava.jpg')
lv = pygame.image.load('Pictures/backgrounds/львовка.png')
window = pygame.image.load('Pictures/backgrounds/window.jpg')
shkura = pygame.image.load('Pictures/backgrounds/shkura.jpg')
lake = pygame.image.load('Pictures/backgrounds/lake.jpg')
