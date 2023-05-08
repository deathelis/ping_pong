from pygame import *

from random import randint
#создай игру "Лабиринт"!
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(
    image.load("galaxy.jpg"),
    (win_width, win_height)
)


mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
kick = mixer.Sound("fire.ogg")

lost = 0
score = 0
game = True
finish = False
font.init()
font1 = font.Font(None, 80)
win = font.render('Победа', True, (255, 255, 255))
lose = font.render("Проигрыш", True, (180, 0, 0))
font2 = font.Font(None, 36)

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

class Bullet(sprite.Sprite):
    def update(self):
        self.rect.y += self.speed
    if self.rect.y < 0:
        self.kill()



ship = Player("rocket.png", 5, win_height - 100, 80, 100, 10)
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy("ufo.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
bullets = sprite.Group()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    if not finish:
       window.blit(background,(0,0))
       ship.update()
       monsters.update()
       bullets.update()
       ship.reset()
       monsters.draw(window)
       bullets.draw(window)
       collides = sprite.groupcollide(monsters, bullets, True, True)
       for c in collides:
           score = score + 1
           monster = Enemy("ufo.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
           monsters.add(monster)
       if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
           finish = True 
           window.blit(lose, (200, 200))
       if score >= goal:
           finish = True
           window.blit(win, (200, 200))
       text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
       window.blit(text, (10, 20))
       text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
       window.blit(text_lose, (10, 50))
       display.update()
    time.delay(50)