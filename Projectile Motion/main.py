# Projectile Motion

import math
import random
import pygame

from functions import *

pygame.init()
SCREEN = WIDTH, HEIGHT = 640, 480

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 30

BLACK = (18, 18, 18)
WHITE = (217, 217, 217)
RED = (255, 0, 0)
GREEN = (0,177,64)
GREEN2 = (0, 255, 0)
BLUE = (30, 144,255)
ORANGE = (252,76,2)
YELLOW = (254,221,0)
PURPLE = (155,38,182)
AQUA = (0,103,127)

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE]

font = pygame.font.SysFont('verdana', 12)

origin = (80, 400)
radius = 250

u = 50
g = 9.8

class Projectile(pygame.sprite.Sprite):
    def __init__(self, u, theta):
        super(Projectile, self).__init__()

        self.u = u
        self.theta = toRadian(abs(theta))
        self.x, self.y = origin
        self.color = random.choice(COLORS)

        self.ch = 0
        
        self.f = self.getTrajectory()
        self.range = self.x + abs(self.getRange())
        self.time = self.timeOfFlight()

        self.path = []

    def timeOfFlight(self):
        return (2 * self.u * math.sin(self.theta)) / g

    def getRange(self):
        return ((self.u ** 2) * 2 * math.sin(self.theta) * math.cos(self.theta)) / g

    def getTrajectory(self):
        return round(g /  (2 * (self.u ** 2) * (math.cos(self.theta) ** 2)), 4)

    def getProjectilePos(self, x):
        return x * math.tan(self.theta) - self.f * x ** 2

    def update(self):
        dx = 2
        if self.x >= self.range:
            self.kill()
        self.x += dx
        self.ch = self.getProjectilePos(self.x - origin[0])

        self.path.append((self.x, self.y-abs(self.ch)))
        self.path = self.path[-15:]

        pygame.draw.circle(win, self.color, self.path[-1], 5)
        for pos in self.path[:-1:3]:
            pygame.draw.circle(win, WHITE, pos, 1)

        # text = font.render(f"{self.ch}", True, GREEN)
        # win.blit(text, (100, 450))

projectile_group = pygame.sprite.Group()

clicked = False
currentp = None

theta = -30
end = getPosOnCircumeference(theta, origin)
arct = toRadian(theta)
arcrect = pygame.Rect(origin[0]-30, origin[1]-30, 60, 60)

running = True
while running:
    win.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

            pos = event.pos
            theta = getAngle(pos, origin)
            if -90 < theta <= 0:
                projectile = Projectile(u, theta)
                projectile_group.add(projectile)
                currentp = projectile

        if event.type == pygame.MOUSEMOTION:
            if clicked:
                pos = event.pos
                theta = getAngle(pos, origin)
                if -90 < theta <= 0:
                    end = getPosOnCircumeference(theta, origin)
                    arct = toRadian(theta)
    
    pygame.draw.line(win, WHITE, origin, (origin[0] + 300, origin[1]), 2)
    pygame.draw.line(win, WHITE, origin, (origin[0], origin[1] - 300), 2)
    pygame.draw.line(win, BLUE, origin, end, 2)
    pygame.draw.arc(win, AQUA, arcrect, 0, -arct, 2)

    projectile_group.update()

    # Info
    fpstext = font.render(f"FPS : {int(clock.get_fps())}", True, WHITE)
    thetatext = font.render(f"Angle : {int(abs(theta))}", True, WHITE)
    win.blit(fpstext, (WIDTH-150, 60))
    win.blit(thetatext, (WIDTH-150, 80))

    if currentp:
        timetext = font.render(f"Time : {int(currentp.timeOfFlight())}s", True, WHITE)
        rangetext = font.render(f"Range : {int(currentp.getRange())}m", True, WHITE)
        win.blit(timetext, (WIDTH-150, 140))
        win.blit(rangetext, (WIDTH-150, 160))

    pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT), 2)
    clock.tick(FPS)
    pygame.display.update()
            
pygame.quit()