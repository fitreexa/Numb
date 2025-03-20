from Sprite import GameSprite
class Player(GameSprite):
    def right(self):
        self.rect.x +=self.speed
    def left(self):
        self.rect.x -=self.speed
    def up(self):
        self.rect.y -= self.speed
    def down(self):
        self.rect.y += self.speed
