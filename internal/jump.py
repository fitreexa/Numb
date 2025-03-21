import pygame
from main import *

"переменные"
vertical_velocity = 0 
gravity = 1 

"цикл обратки событий"
for event in pygame.event.get(): 
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_SPACE: 
            vertical_velocity = -10 
            vertical_velocity += gravity 
if player_rect.y >= 465: 
    player_rect.y = 465 
    vertical_velocity = 0 