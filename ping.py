from typing import Any 
from pygame import* 
from random import randint 
racket = 0 
tenis_ball = 0 
class GameSprite(sprite.Sprite):  
  
    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed):  
        sprite.Sprite.__init__(self)  
        self.image = transform.scale(image.load(player_image),(50 , 50))   
        self.speed = player_speed  
        self.rect = self.image.get_rect()  
        self.rect.x = player_x  
        self.rect.y = player_y 
     
 
class Player(GameSprite):  
    def update(self):  
        #key = K_SPACE()  
        keys_pressed = key.get_pressed() 
        if keys_pressed [K_UP] and self.rect.x > 5 :  
            self.rect.x -= self.speed    
 
            keys_pressed = key.get_pressed()  
        if keys_pressed [K_DOWN] and self.rect.x < win_width - 50 :  
            self.rect.x += self.speed 
  
class Player(GameSprite):  
    def update(self):  
        #key = K_SPACE()  
        keys_pressed = key.get_pressed() 
        if keys_pressed [K_w] and self.rect.x > 5 :  
            self.rect.x -= self.speed    
 
            keys_pressed = key.get_pressed()  
        if keys_pressed [K_s] and self.rect.x < win_width - 50 :  
            self.rect.x += self.speed  
win_width = 700 
win_height = 500 
 
racket_1 = 'racket.png' 
racket_2 = 'racket.png' 
tenis_ball = 'tenis_ball.png' 
 
racket_1 = Player(racket, 10, win_height - 100, 80, 100, 20) 
racket_2 = Player(racket, 10, win_height - 100, 80, 100, 20)  
tenis_ball = GameSprite() 
 
window = display.set_mode((win_width, win_height))  
display.set_caption("Shooter Game") 
 
display = display.update()