from pygame import *
#НЕОБХОДИМЫЕ КЛАССЫ

background = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background)

font.init()
font1 = font.SysFont('Times New Roman', 80)
lose1 = font1.render('player 1 lose', True, (255, 255, 255))
lose2 = font1.render('player 1 lose', True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = GameSprite('ball.jpg', 200, 200, 4, 50, 50)
speed_x = 3
speed_y = 3 
finish = False

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y +=self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y +=self.speed

racket_l = Player('Без названия.jpg', 30,200,4,50,150)
racket_r = Player('Без названия.jpg', 520,200,4,50,150)

game  = True
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(background)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            
        
        


        ball.reset()
        racket_l.update_l()
        racket_r.update_r()
        racket_l.reset()
        racket_r.reset()
    display.update()
    clock.tick(60)
























































