# Imports
import sys
import pygame

# Configuration
pygame.init()
fps = 10
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
game_started = False
font = pygame.font.SysFont('Arial', 40)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text, font,fc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 50))
        self.image.fill((0,100,0))
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.buttonText = font.render(text, True, fc)
        pygame.draw.rect(self.image,(0,100,0),pygame.Rect(0, 0, width, height))
        self.image.blit(self.buttonText, [
            self.rect.width / 2 - self.buttonText.get_rect().width / 2,
            self.rect.height / 2 - self.buttonText.get_rect().height / 2
        ])




all_sprites = pygame.sprite.Group()
st1 = Button([width/2, height/3], 'brat', font, (0,0,0))
st2 = Button([width/2, height/2], 'brat', font, (0,0,0))
st3 = Button([width/2, height/1.5], 'brat', font, (0,0,0))
all_sprites.add(st1)
all_sprites.add(st2)
all_sprites.add(st3)

clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)