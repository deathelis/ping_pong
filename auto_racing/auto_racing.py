from pygame import *
from time import sleep
from random import randint
#создай игру "Лабиринт"!
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(
    image.load("road.png"),
    (win_width, win_height)
)

seconds_left = 100

lost = 0
score = 0
game = True
finish = False
clock = time.Clock()
FPS = 60

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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y < win_height:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1




car = Player("car.png", 5, win_height - 100, 80, 100, 5)
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy("car1.png", randint(80, win_width - 80), -40, 80, 120, randint(1, 5))
    monsters.add(monster)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        car.update()
        monsters.update()
        car.reset()
        monsters.draw(window)
        if sprite.spritecollide(car, monsters, False):
            finish = True 


        display.update()
    clock.tick(FPS)
       
       


