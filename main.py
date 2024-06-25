import pygame
import random
import math

pygame.init()

#Size of the screen
SCREEN_WIDTH = 501
SCREEN_HEIGTH = 404
#Sets the screen with the correct size with a name
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Pong")
#Load background image
background = pygame.image.load('Img/background.png').convert()
#Used to get the FPS
clock = pygame.time.Clock()

scorePlayer1 = 0
scorePlayer2 = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width= width 
        self.height = height
        self.color = (0,255,0)
        self.vel = 5
        self.hitbox = (self.x, self.y, self.width,self.height)
    #Used to draw the object in the screen and update the movement of the players
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width,self.height)
        pygame.draw.rect(screen, (255, 0, 0), (self.hitbox), 2)
        
        
class ball(object):
    def __init__(self, x, y, vel, radius, xDirection, yDirection):
        self.x = x
        self.y = y
        self.vel = vel
        self.radius = radius
        self.color = (0,0,255)
        self.xDirection = xDirection
        self.yDirection = yDirection
    #Used to draw the ball
    def draw(self, screen):
        self.move()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
       
        #pygame.draw.circle(screen, (255, 0, 0), (self.hitbox), 2)
        
    def move(self):
        self.collision()
        self.x += self.vel*self.xDirection
        self.y += self.vel*self.yDirection
        
    def collision(self):
        global ball1
        global scorePlayer2
        global scorePlayer1
        
        if self.x - self.radius*2 <= player1.x + player1.width:
            if self.y <= player1.y +player1.height and self.y >= player1.y:
                self.xDirection = self.xDirection*-1
                print("Spiller 1 treffer ballen")
        elif self.x + self.radius*2 >= player2.x:
            if  self.y <= player2.y +player2.height and self.y >= player2.y:
                self.xDirection = self.xDirection*-1
                print("Spiller 2 treffer ballen")

        
            
        if self.x+ self.radius*2 >= SCREEN_WIDTH:
            scorePlayer1 += 1
            print("Spiller 1 får poeng")
            del ball1
            ball1 = ball(SCREEN_WIDTH/2 + 2, SCREEN_HEIGTH/2, 3, 10, -1, 1)
            redrawGameWindow()
        elif self.x - self.radius*2 <= 0:
            scorePlayer2 += 1
            print("Spiller 2 får poeng")
            
            del ball1
            ball1 = ball(SCREEN_WIDTH/2 + 2, SCREEN_HEIGTH/2, 3, 10, -1, -1)
            redrawGameWindow()

        elif self.y - self.radius <= 0:
            self.yDirection=self.yDirection*-1
            print("Ballen treffer taket")
                 
        elif self.y + self.radius >= SCREEN_HEIGTH:
            self.yDirection=self.yDirection*-1
            print("Ballen treffer gulvet")
        
            
                    
        
        

def redrawGameWindow():
    
    screen.blit(background, (0,0))
    text = font.render(str(scorePlayer1) + ' - ' + str(scorePlayer2), 1, (255,0,0))
    screen.blit(text, (SCREEN_WIDTH/2-37, 20))
    player1.draw(screen)
    player2.draw(screen)
    ball1.draw(screen)
    pygame.display.update()
    
    
#Main loop
font = pygame.font.SysFont('comicsans', 30, True)
player1 = player(0, SCREEN_HEIGTH/2-75, 30, 150)
player2 = player(SCREEN_WIDTH-30, SCREEN_HEIGTH/2-75, 30, 150)
startingAngle = 1
while startingAngle == 1 or startingAngle == 0:
    startingAngle = random.random()
    print(startingAngle)
   
ball1 = ball(SCREEN_WIDTH/2 + 2, SCREEN_HEIGTH/2, 3, 10, math.cos(startingAngle), math.sin(startingAngle))
run = True
while run:
    clock.tick(60)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player1.y >= player1.vel:
        player1.y -= player1.vel
    if key[pygame.K_DOWN] and player1.y <= SCREEN_HEIGTH-player1.height-player1.vel:
        player1.y += player1.vel


    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
    redrawGameWindow()