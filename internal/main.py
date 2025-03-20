import pygame
from helper import resource_path
from Sprite import *
from class_player import Player

pygame.init()

width,height= 1000,563
screen=pygame.display.set_mode((width,height))
background=pygame.image.load(resource_path('assets/field.png'))
pygame.display.set_caption('future game')


# player=pygame.image.load(resource_path('assets/КУБ.jpg'))
# player_rect=player.get_rect(center=(width//2,height//2))

sprit1=Player(resource_path('assets/КУБ.jpg'),10,400,65,65,10)
player_rect=sprit1.get_rect(center=(width//2,height//2))

game=True

FPS=60
timer=pygame.time.Clock()
while game:
    screen.blit(background,(0,0))
    sprit1.reset()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and sprit1.rect.y >1: 
        sprit1.up()
    if keys[pygame.K_DOWN]and sprit1.rect.y < 1000: 
        sprit1.down()
    if keys[pygame.K_LEFT]and sprit1.rect.x >1:
        sprit1.left()
    if keys[pygame.K_RIGHT]and sprit1.rect.x <600:
        sprit1.right()

pygame.quit()