#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255,215,0)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COUNTER = 0

coins_weights = {1:(30,30),
                3: (40,40),
                5: (50,50)}

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 55)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER", True, RED)


background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Gonshick Nelegalniy")

speed_booster = False


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE, SPEED, speed_booster
        if COINS_COUNTER >= 50 and not speed_booster:
            SPEED += 5
            speed_booster = True
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bigimage = pygame.image.load("coin.png")
        self.rect = None
        self.reset()

    #to reset everytime and spawn the new coin
    def reset(self): 
        global random_key 
        random_key = random.choice(list(coins_weights.keys()))
        self.image = pygame.transform.smoothscale(self.bigimage, coins_weights[random_key])
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.reset()


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.Sound('background2.wav').play(-1)


#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Text of scores and numbers
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    number_of_coins = font_small.render(str(COINS_COUNTER), True, ORANGE)
    DISPLAYSURF.blit(number_of_coins, (370, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    #Logic od coins
    collected_coin = pygame.sprite.spritecollideany(P1, coins)
    if collected_coin:
        coin_sound = pygame.mixer.Sound("coin_sound.wav").play()
        coin_sound.set_volume(0.5)
        COINS_COUNTER += random_key
        collected_coin.reset()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
                
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
                entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
    pygame.display.update()
    FramePerSec.tick(FPS)
