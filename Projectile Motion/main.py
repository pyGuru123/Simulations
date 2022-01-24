# Projectile Motion

import math
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
FPS = 45

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

font = pygame.font.SysFont('verdana', 11)

origin = (80, 400)
radius = 250
pos = None

u = 10
g = 9.8

class Projectile(pygame.sprite.Sprite):
    def __init__(self, u, theta, h=0):
        super(Projectile, self).__init__()

        self.u = u
        self.theta = toRadian(theta)
        self.h = h
        self.x, self.y = origin
        self.f = self.getFlight()
        print(math.tan(theta))
        print(self.f)

        self.ux = u * math.cos(self.theta)
        self.uy = u * math.sin(self.theta)

    def timeOfFlight(self):
        return (2 * self.uy) / g

    def getFlight(self):
        return round(g /  (2 * (self.u ** 2) * (math.cos(self.theta) ** 2)), 5)

    def update(self):
        self.x += 0.1
        height = self.h
        x = self.x * math.tan(self.theta)
        y = self.f * x ** 2
        self.y = (x - y)

        pygame.draw.circle(win, BLUE, (self.x, self.y), 3)
        text = font.render(f"{self.x, self.y, self.f}", True, GREEN)
        win.blit(text, (100, 450))

p = Projectile(6, 60)
    # trajectory formula
    # y = h + xtan(α) - gx²/2V₀²cos²(α)

projectile_group = pygame.sprite.Group()

clicked = False

running = True
while running:
    win.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninh = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not clicked:
                cliced = True

            px, py = pos = event.pos
            if px < 80 or py > 400:
                pos = None

            if pos:
                theta = getAngle(pos, origin)
                projectile = Projectile(u, theta)
                projectile_group.add(projectile)
    
    pygame.draw.line(win, WHITE, origin, (origin[0] + 300, origin[1]), 2)
    pygame.draw.line(win, WHITE, origin, (origin[0], origin[1] - 300), 2)

    if pos:
        position = font.render(f'{pos}, {theta}', True, GREEN)
        win.blit(position, (pos[0] + 6, pos[1] - 6))
        pygame.draw.circle(win, RED, pos, 5)

    projectile_group.update()

    pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT), 2)
    clock.tick(FPS)
    pygame.display.update()
            
pygame.quit()