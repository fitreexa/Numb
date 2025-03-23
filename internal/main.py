"""
подключил все необходимые модули
"""

import pygame
from helper import resource_path
from thefence import Wall
from sprite import GameSprite

pygame.init()

"""
создал фон для игры
"""

width, height = 1000, 563
screen = pygame.display.set_mode((width, height))
background = pygame.image.load(resource_path("assets/field.png"))
pygame.display.set_caption("future game")

aset = resource_path("assets/Леденец.webp")
asset = resource_path("assets/ам ням.webp")
player = GameSprite(asset,10,450,100,100,10)
sprit3 = GameSprite(aset,950,400,100,100,0)
"""
создал игрока и расположил его в в нужном месте
"""

# player = pygame.image.load(resource_path("assets/ам ням.webp"))
# player_rect = player.get_rect(center=(width // 16, height // 1.1))
GAME = True
FINISH=False
"""
создал стены
"""

wall1=Wall(0,123,2,200,500,13,150)
wall2=Wall(0,150,2,400,500,13,100)
wall3=Wall(0,150,2,600,500,13,100)
wall4=Wall(0,150,2,800,500,13,100)

"""
сделал коллизию для стен
"""

pygame.sprite.collide_rect(player,wall1)
pygame.sprite.collide_rect(player,wall2)
pygame.sprite.collide_rect(player,wall3)
pygame.sprite.collide_rect(player,wall4)

"""
добавил font и два условия его отображения при победе и проигрыше
"""

pygame.font.init()
font=pygame.font.Font(None,70)
win=font.render('ПОБЕДА!!!',True,(255,215,0))
end=font.render('НЕ ПОБЕДА!!!',True,(255,215,255))

"""
создал переменные для работы прыжка
"""
JUMP = False
JUMP_SIZE = 10

FPS = 60
timer = pygame.time.Clock()

"""
создал цикл для работы игры и управления игрока и работы font(a)
"""

while GAME:
    keys = pygame.key.get_pressed()
    screen.blit(background, (0, 0))
    player.reset(screen)
    wall1.draw_wall(screen)
    wall2.draw_wall(screen)
    wall3.draw_wall(screen)
    wall4.draw_wall(screen)
    if pygame.sprite.collide_rect(player,sprit3):
        screen.blit(win,(200,200))
        FINISH=True
    if pygame.sprite.collide_rect(player,wall1):
        screen.blit(end,(200,200))
        FINISH=True
    if pygame.sprite.collide_rect(player,wall3):
        screen.blit(end,(200,200))
        FINISH=True
    if pygame.sprite.collide_rect(player,wall2):
        screen.blit(end,(200,200))
        FINISH=True
    if pygame.sprite.collide_rect(player,wall4):
        screen.blit(end,(200,200))
        FINISH=True
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = False
    if not JUMP:
        if keys[pygame.K_UP]:
            JUMP = True
    else:
        if JUMP_SIZE >= -10:
            if JUMP_SIZE > 0:
                player.rect.y -= (JUMP_SIZE**2) / 2
            else:
                player.rect.y += (JUMP_SIZE**2) / 2
            JUMP_SIZE -= 1
        else:
            JUMP = False
            JUMP_SIZE = 10

    if keys[pygame.K_LEFT] and player.rect.x > 1:
        player.rect.x -= 4
    if keys[pygame.K_RIGHT] and player.rect.x < 900:
        player.rect.x += 4
pygame.quit()
