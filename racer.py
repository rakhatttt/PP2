import pygame,sys
from pygame.locals import *
import random

pygame.init()

FPS=(60)
FramePerSec=pygame.time.Clock()




width=400
height = 600
SPEED=5
SCORE=0

color1 = pygame.Color(0, 0, 0)         #Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

font=pygame.font.SysFont("Verdana",60)
font_small=pygame.font.SysFont("Verdana",20)
gameover=font.render("Game Over",True, color1)

background=pygame.image.load("/Users/admin/Downloads/PygameTutorial_3_0/AnimatedStreet.png")



screen = pygame.display.set_mode((width,height))
screen.fill(color2)
pygame.display.set_caption("racer")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/admin/Downloads/PygameTutorial_3_0/Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,width-40),0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top>600):
            self.rect.top=0
            self.rect.center=(random.randint(30,width-40),0)

    def draw(self, surface):
        surface.blit(self.image,self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/admin/Downloads/PygameTutorial_3_0/Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)
    
    def move(self):
        pressed_keys=pygame.key.get_pressed()
        if self.rect.left>0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

    def draw(self,surface):
        surface.blit(self.image, self.rect)

P1=Player()
E1=Enemy()

enemies=pygame.sprite.Group()
enemies.add(E1)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED=pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED,1000)

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background,(0,0))
    scores=font_small.render(str(SCORE),True,color1)
    screen.blit(scores,(10,10))

    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound("/Users/admin/Downloads/PygameTutorial_3_0/crash.wav").play()
        time.sleep(0.5)

        screen.fill(color4)
        screen.blit(gameover,(30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    pygame.display.update()
    FramePerSec.tick(FPS)