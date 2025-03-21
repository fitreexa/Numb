import pygame
from helper import resource_path
from Sprite import GameSprite


pygame.init()

width,height= 1000,563 
screen=pygame.display.set_mode((width,height))
background=pygame.image.load(resource_path('assets/field.png'))
pygame.display.set_caption('future game')

player = pygame.image.load(resource_path('assets/ам ням.webp'))
# player_rect=player.get_rect(center=(width//2,height//2))
player_rect=player.get_rect(center=(width//16,height//1.1))
game=True

player_rect.y=450

vertical_velocity = 0 
gravity = 1 

jump=False
jump_size=10

FPS=60
timer=pygame.time.Clock()
while game:
    keys=pygame.key.get_pressed()  
    screen.blit(background,(0,0))
    screen.blit(player,player_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    if not jump:
        if keys[pygame.K_UP]:
            jump =True
    else:
        if jump_size >= -10:
            if jump_size > 110:
                player_rect.y -= (jump_size ** 2) / 2
            else:
                player_rect.y += (jump_size ** 2) / 2
            jump_size -= 1
        else:
            jump=False
            jump_size = 10

    if keys[pygame.K_LEFT]and player_rect.x >1:
        player_rect.x -= 4
    if keys[pygame.K_RIGHT]and player_rect.x < 900:
        player_rect.x += 4
pygame.quit()
