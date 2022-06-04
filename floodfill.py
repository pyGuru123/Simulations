import pygame
import sys
sys.setrecursionlimit(3000)

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
FPS = 60

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

colors = [BLUE, RED, GREEN]

# TEXT ************************************************************************

font = pygame.font.SysFont('freesansbold', 26)
text = font.render('Flood Fill Algo test', True, WHITE)

# LOADING IMAGES **************************************************************
clear = pygame.image.load('clear.png')
clear = pygame.transform.scale(clear, (30, 30))
clear_rect = clear.get_rect()
clear_rect.x = WIDTH - 40
clear_rect.y = HEIGHT - 60

clicked = False
polygon = []

def floodfill(x, y, old, new):
	pixel = win.get_at((x, y))
	if pixel != old:
		return
	elif pixel == new:
		return
	else:
		print(x, y)
		win.set_at((x, y), new)
		pygame.display.update()

		floodfill(x-2, y, old, new)
		floodfill(x+1, y, old, new)
		floodfill(x, y-1, old, new)
		floodfill(x, y+2, old, new)
		# floodfill(x-1, y-1, old, new)
		# floodfill(x-1, y+1, old, new)
		# floodfill(x+1, y-1, old, new)
		# floodfill(x+1, y+1, old, new)

class Rect:
	def __init__(self, x, y, c):
		self.x = x
		self.y = y
		self.c = c
		self.rect = pygame.Rect(x, y, 30, 30)

	def draw(self):
		pygame.draw.rect(win, self.c, self.rect)

r1 = Rect(WIDTH-40, 10, RED)
r2 = Rect(WIDTH-40, 45, GREEN)
r3 = Rect(WIDTH-40, 85, BLUE)

rects = [r1, r2, r3]
color = RED

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos
			btn = pygame.mouse.get_pressed()
			if btn[0]:
				clicked = True

			elif btn[2]:
				if pos[0] < WIDTH - 50:
					floodfill(pos[0], pos[1], (0,0,0), color)

			if pos[0] > WIDTH - 50:
				for r in rects:
					if r.rect.collidepoint(pos):
						color = r.c

			if clear_rect.collidepoint(pos):
				win.fill(BLACK)

		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False

		if event.type == pygame.MOUSEMOTION:
			if clicked:
				pos = event.pos
				btn = pygame.mouse.get_pressed()
				if btn[0]:
					if pos[0] < WIDTH - 50:
						pygame.draw.circle(win, WHITE, pos, 5)
				
	pygame.draw.rect(win, WHITE, (0, 0, WIDTH-50, HEIGHT), 3)
	pygame.draw.rect(win, WHITE, (WIDTH-50, 0, 50, HEIGHT), 2)

	win.blit(text, (60, 40))
	win.blit(clear, clear_rect)

	for rect in rects:
		rect.draw()

	clock.tick(FPS)
	pygame.display.update()

pygame.quit()