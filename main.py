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

# special sprite for buttons
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

    def use(self):
        return 1








use_sprites = pygame.sprite.Group() # interactive sprites


#starting screen
st1 = Button([width/2, height/3], 'brat', font, (0,0,0))
st2 = Button([width/2, height/2], 'brat', font, (0,0,0))
st3 = Button([width/2, height/1.5], 'brat', font, (0,0,0))
use_sprites.add(st1)
use_sprites.add(st2)
use_sprites.add(st3)

#dialogue window
back = 0
hero = 0



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
                    sprite.use()



    use_sprites.update()
    screen.fill((0,0,0))
    use_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)