import pygame 
import math
from datetime import datetime
  
pygame.init() 

width=800
height=600
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("clock") 

body=pygame.image.load("/Users/admin/Downloads/clock.png")
minute=pygame.image.load("/Users/admin/Downloads/min_hand.png")
second=pygame.image.load("/Users/admin/Downloads/sec_hand.png")

center = (width//2, height//2)

def rotate(image,angle,pivot):
    rot_img=pygame.transform.rotate(image,angle)
    rect= rot_img.get_rect(center=pivot)
    return rot_img, rect

clock = pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    now=datetime.now()
    minn=now.minute
    secc=now.second


    screen.fill((255,255,255))

    screen.blit(body, (width//2 - body.get_width()//2, height//2 - body.get_height()//2))

    minute_angle=-6*minn
    rotated_righthand, right_rect=rotate(minute,minute_angle,center)
    screen.blit(rotated_righthand,right_rect.topleft)

    second_angle=-6*secc
    rotated_lefthand,left_rect=rotate(second,second_angle,center)
    screen.blit(rotated_lefthand,left_rect.topleft)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()



        
