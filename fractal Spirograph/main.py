import math

import pygame

pygame.init()

SCREEN = WIDTH, HEIGHT = 288, 512

info = pygame.display.Info()

width = info.current_w

height = info.current_h

if width >= height:

	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)else:

	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()

FPS = 60

# COLORS **********************************************************************

WHITE = (255, 255, 255)

BLUE = (30, 144,255)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLACK = (0, 0, 20)

COLOR = WHITE

# FUNCTIONS *******************************************************************

def rotate(CENTER, radius, angle, r):

	x = round(CENTER[0] + radius * math.cos(angle * math.pi / 180))

	y = round(CENTER[1] + radius * math.sin(angle * math.pi / 180))

	rect = pygame.draw.circle(win, COLOR, (x,y), r, 2)

	return rect

# GAME ************************************************************************

CENTER = WIDTH//2, HEIGHT//2

angle1 = angle2 = angle3 = 0

radius = 92

pos = []

running = True

while running:

	win.fill(BLACK)

	

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			running = False

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:

				running = False		

	

	rect = rotate(CENTER, radius, round(angle1), 15)

	rect2 = rotate(rect.center, 17, angle2, 5)

	rect3 = rotate(rect2.center, 6, angle3, 1)

	angle1 += 0.2

	angle2 += 1

	angle3 += 2

	pos.append(rect3.center)

	

	pygame.draw.circle(win, WHITE, CENTER, 80, 2)

	for c in pos:

		pygame.draw.circle(win, RED, c, 1)

				

	clock.tick(FPS)

	pygame.display.update()

pygame.quit()
