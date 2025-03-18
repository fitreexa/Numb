import pygame
from helper import resource_path

pygame.init()

width,height= 1920,1020
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('future game')

player=pygame.image.load(resource_path('assets/КУБ.jpg'))
player_rect=player.get_rect(center=(width//2,height//2))

speed=2

game=True

FPS=60
timer=pygame.time.Clock()
while game:
    screen.fill((1 ,255 ,30))
    screen.blit(player,player_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]: 
        player_rect.y -= speed
    if keys[pygame.K_DOWN]: 
        player_rect.y += speed
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed

pygame.quit()