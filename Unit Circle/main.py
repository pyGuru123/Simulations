import math
import pygame

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512

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

origin = WIDTH//2, HEIGHT//2
radius = 120
angle = 0
arcrect = pygame.Rect(origin[0]-25, origin[1]-25, 50, 50)

def toRadian(theta):
    return theta * math.pi / 180
    
def getPoint():
    theta= toRadian(angle)
    x = origin[0] + radius * math.cos(theta)
    y = origin[1] + radius * math.sin(theta)
    return x, y

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
            clicked = True
            
    theta = toRadian(angle)
    pygame.draw.arc(win, AQUA, arcrect, 0, -theta, 1)
    pygame.draw.line(win, GREEN, (origin[0] - 1.3 * radius, origin[1]), (origin[0] + 1.3 * radius, origin[1]))
    pygame.draw.line(win, GREEN, (origin[0], origin[1] - 1.3 * radius), (origin[0], origin[1] + 1.3 * radius))
    pygame.draw.circle(win, GREEN2, origin, radius, 2)
    pygame.draw.circle(win, GREEN, origin, radius, 1)
    
    x, y = getPoint()
    
    pygame.draw.line(win, WHITE, origin, (x, y))
    pygame.draw.line(win, BLUE, origin, (x, origin[1]))
    pygame.draw.line(win, RED, (x, y), (x, origin[1]))
    pygame.draw.circle(win, YELLOW, (x, y), 5)
    pygame.draw.circle(win, RED, (x, y), 5, 1)
    pygame.draw.circle(win, RED, (x, origin[1]), 3)
    
    theta = toRadian(abs(angle))
    angletext = font.render(f"x : {abs(angle) % 360}", True, BLUE)
    atrect = angletext.get_rect(center = (origin[0], origin[1] - 1.5 * radius))
    sintext = font.render(f"sin({math.sin(theta):.5f})", True, ORANGE)
    sinrect = sintext.get_rect(center=(origin[0] -  radius+30, origin[1] - 1.5 * radius))
    costext = font.render(f"cos({math.cos(theta):.5f})", True, ORANGE)
    cosrect = costext.get_rect(center=(origin[0] +  radius-30, origin[1] - 1.5 * radius))
    info = font.render("Unit Circle of Trigonometry", True, PURPLE)
    inforect = info.get_rect(center=(origin[0], origin[1] + 1.8 * radius))
    
    win.blit(angletext, atrect)
    win.blit(sintext, sinrect)
    win.blit(costext, cosrect)
    win.blit(info, inforect)
    
    r = font.render("r", True, WHITE)
    win.blit(r, ((origin[0] + x) /2 - 5 , (origin[1] + y)/2))
    rcos = font.render("r.cos x", True, BLUE)
    win.blit(rcos, ((origin[0] + x) / 2 - 20, origin[1] + 5))
    rcos = font.render("r.sin x", True, RED)
    win.blit(rcos, (x + 5,  (origin[1]  + y) / 2 - 10))
    
    if clicked:
        angle -= 1
        if abs(angle) % 360 == 0:
            angle = 0
    
    
    clock.tick(FPS)
    pygame.display.update()
            
pygame.quit()