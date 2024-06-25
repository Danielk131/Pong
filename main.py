import pygame

pygame.init()

SCREEN_WIDTH = 501
SCREEN_HEIGTH = 404

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Pong")

background = pygame.image.load('Img/background.png').convert()

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width= width 
        self.height = height
        self.color = (0,255,0)
        self.vel = 5
        self.hitbox = (self.x, self.y, self.width,self.height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width,self.height)
        pygame.draw.rect(screen, (255, 0, 0), (self.hitbox), 2)
        
class ball(object):
    def __init__(self, x, y, vel, radius):
        self.x = x
        self.y = y
        self.vel = vel
        self.radius = radius
        self.color = (0,0,255)
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
       
        #pygame.draw.circle(screen, (255, 0, 0), (self.hitbox), 2)

def redrawGameWindow():
    
    screen.blit(background, (0,0))
    player1.draw(screen)
    player2.draw(screen)
    ball1.draw(screen)
    pygame.display.update()
#Main loop
player1 = player(0, SCREEN_HEIGTH/2-75, 30, 150)
player2 = player(SCREEN_WIDTH-30, SCREEN_HEIGTH/2-75, 30, 150)
ball1 = ball(SCREEN_WIDTH/2 + 2, SCREEN_HEIGTH/2, 5, 10)
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