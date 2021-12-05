from random import random
import pygame, sys, random

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN
pygame.init()

MOVE = 20
WIDTHSCREEN  = 800
HEIGHTSCREEN = 700
FPS = 200
BLACK = (0, 0, 0)
GREEN = (0, 155, 0)
RED = (155, 0, 0)
WHITE = (255, 255, 255)
SIZESHOOTER = 30
SIZESHOOT = 10
SIZEOP = 20
TIMEWAIT = 3000
vt_y = HEIGHTSCREEN - SIZESHOOTER*3
vt_x = int(WIDTHSCREEN/2) 
shoot_list = []
sOP_list = []

screen = pygame.display.set_mode((WIDTHSCREEN, HEIGHTSCREEN))
pygame.display.set_caption("Y8 Gaming")
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("comicsansms", 30)

addOP = pygame.USEREVENT
pygame.time.set_timer(addOP, TIMEWAIT)

def drawShooter(x, y):
    pygame.draw.rect(screen, GREEN, [x, y, SIZESHOOTER, SIZESHOOTER])
def drawShoot(shoot):
    for x in shoot:
        pygame.draw.rect(screen, RED, [x[0], x[1], SIZESHOOT, SIZESHOOT])
def drawOP(sOP):
    for x in sOP:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], SIZEOP, SIZEOP])
def check_collision(x, y, z, t):
    if (x >= z and x <= z + SIZEOP and y >= t and y <= t + SIZEOP) or (x + 10>= z and x + 10 <= z + SIZEOP and y >= t and y <= t + SIZEOP):
        return True
    return False
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, RED)
    screen.blit(value, [WIDTHSCREEN/2 - 100, 10])

score = 0
ok = True

while ok:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and vt_x <= WIDTHSCREEN - MOVE:
                vt_x += MOVE
            elif event.key == K_UP and vt_x <= WIDTHSCREEN - MOVE*2:
                vt_x += MOVE*2    
            elif event.key == K_LEFT and vt_x >= MOVE:
                vt_x -= MOVE
            elif event.key == K_DOWN and vt_x >= MOVE*2:
                vt_x -= MOVE*2    
            elif event.key == K_SPACE:
                shoot_head = []
                shoot_head.append(vt_x + SIZESHOOTER/2 - SIZESHOOT/2)
                shoot_head.append(vt_y)
                shoot_list.append(shoot_head)
        if event.type == addOP:
                sOP_head = []
                sOP_head.append(round(random.randrange(SIZEOP + 10, WIDTHSCREEN - SIZEOP)))
                sOP_head.append(10)
                sOP_list.append(sOP_head)    
    xx = -1     
    for x in shoot_list:
        xx += 1
        x[1] = x[1] - 2
        if x[1] <= 0:
            del shoot_list[xx]
    for x in sOP_list:
        x[1] = x[1] + 1
        if x[1] >= HEIGHTSCREEN - 20:
            ok = False
    xx = -1    
    for shoot in shoot_list:
        xx += 1
        xs = -1
        for sOP in sOP_list:
            xs += 1
            if check_collision(shoot[0], shoot[1], sOP[0], sOP[1]):
                    del shoot_list[xx]
                    del sOP_list[xs]
                    score += 1 
    Your_score(score)                
    drawShooter(vt_x, vt_y)        
    drawShoot(shoot_list)
    drawOP(sOP_list)
    pygame.display.update()    
    clock.tick(FPS)