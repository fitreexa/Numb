import pygame
from helper import resource_path
from Sprite import GameSprite
from Thefence import Wall

pygame.init()

width,height= 1000,563 
screen=pygame.display.set_mode((width,height))
background=pygame.image.load(resource_path('assets/field.png'))
pygame.display.set_caption('future game')

player = pygame.image.load(resource_path('assets/ам ням.webp'))
player_rect=player.get_rect(center=(width//16,height//1.1))
game=True

wall1=Wall(0,123,2,100,100,13,450)
wall2=Wall(0,150,2,500,300,13,200)       
wall3=Wall(0,150,2,100,90,500,13)
wall4=Wall(0,150,2,400,200,500,13)
pygame.sprite.collide_rect(player,wall1)
pygame.sprite.collide_rect(player,wall2)
pygame.sprite.collide_rect(player,wall3)
pygame.sprite.collide_rect(player,wall4)

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
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    if not jump:
        if keys[pygame.K_UP]:
            jump =True
    else:
        if jump_size >= -10:
            if jump_size > 0:
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
