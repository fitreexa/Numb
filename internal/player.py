"""
подключил необходимый модуль
"""
from sprite import GameSprite
class Player(GameSprite):
    """
    сделал наследование
    """
    def __init__(self,imaged,x,y,sizex,sizey,speed):
        super().__init__(imaged,x,y,sizex,sizey,speed)
