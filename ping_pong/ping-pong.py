from pygame import *

from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = transform.scale(
    image.load("phon.jpg"),
    (win_width, win_height)
)

clock = time.Clock()
FPS = 60
lost = 0
score = 0
game = True
finish = False

score = 0
goal = 10
lost = 0
max_lost = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1




player_1 = Player("rocket.png", 30, 200, 50, 150, 4)
player_2 = Player("rocket.png", 520, 200, 50, 150, 4)
ball = GameSprite("ball.png", 200, 200, 50, 45, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
       window.blit(background,(0,0))
       player_1.update_l()
       player_2.update_r()
       player_1.reset()
       player_2.reset()
       ball.reset()
    display.update()
    clock.tick(FPS)