import pygame
from helper import resource_path
from Sprite import *

pygame.init()

width,height= 1000,563
screen=pygame.display.set_mode((width,height))
background=pygame.image.load(resource_path('assets/field.png'))
pygame.display.set_caption('future game')


player=pygame.image.load(resource_path('assets/КУБ.jpg'))
player_rect=player.get_rect(center=(width//2,height//2))

speed=2

game=True

FPS=60
timer=pygame.time.Clock()
while game:
    screen.blit(background,(0,0))
    screen.blit(player,player_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y >1: 
        player_rect.y -= speed
    if keys[pygame.K_DOWN]and player_rect.y < 500: 
        player_rect.y += speed
    if keys[pygame.K_LEFT]and player_rect.x >1:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]and player_rect.x <900:
        player_rect.x += speed

pygame.quit()