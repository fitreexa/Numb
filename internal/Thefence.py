"""
подключил необходимые модули
"""
import pygame
class Wall(pygame.sprite.Sprite):
    """
    создал класс wall
    """
    def __init__(
        self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height
    ):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self, screen: pygame.Surface):
        """
        сделал модуль для отрисовки стен
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))
