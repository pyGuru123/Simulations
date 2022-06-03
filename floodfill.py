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
FPS = 60

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

colors = [BLUE, RED, GREEN]

# GAME ************************************************************************

font = pygame.font.SysFont('arial', 16)
text = font.render('Flood Fill Algo test#1', True, WHITE)

clicked = False
polygon = []

def floodfill(x, y, old, new):
	if win.get_at((x, y)) != old:
		return
	else:
		pygame.draw.circle(win, new, (x, y), 1)
		pygame.display.update()

		floodfill(x-1, y, old, new)
		floodfill(x+1, y, old, new)
		floodfill(x, y-1, old, new)
		floodfill(x, y+1, old, new)
		floodfill(x-1, y-1, old, new)
		floodfill(x-1, y+1, old, new)
		floodfill(x+1, y-1, old, new)
		floodfill(x+1, y+1, old, new)

color = RED

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

running = True
while running:
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

		if event.type == pygame.MOUSEMOTION:
			if clicked:
				pos = event.pos
				btn = pygame.mouse.get_pressed()
				if btn[0]:
					if pos[0] < WIDTH - 50:
						pygame.draw.circle(win, WHITE, pos, 5)

				elif btn[2]:
					if pos[0] < WIDTH - 50:
						floodfill(pos[0], pos[1], (0,0,0), color)

				if pos[0] > WIDTH - 50:
					for r in rects:
						if r.rect.collidepoint(pos):
							print(True)
							color = rect.c
				
	pygame.draw.rect(win, WHITE, (0, 0, WIDTH-50, HEIGHT), 3)
	pygame.draw.rect(win, WHITE, (WIDTH-50, 0, 50, HEIGHT), 2)

	win.blit(text, (60, 40))

	for rect in rects:
		rect.draw()

	clock.tick(FPS)
	pygame.display.update()

pygame.quit()
