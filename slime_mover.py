import pygame, sys


pygame.init()

size = width, height = 800, 600
BLACK = (0,0,0)

screen = pygame.display.set_mode(size)

while 1:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			sys.exit()

	screen.fill(BLACK)
	
	pygame.display.flip()