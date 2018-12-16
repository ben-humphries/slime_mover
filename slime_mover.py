import pygame, sys

from player import *
from movement_indicator import *

pygame.init()

size = width, height = 800, 600
BLACK = (0,0,0)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

player = Player(width, height)
movement_indicator = MovementIndicator(screen)

while 1:

	dt = clock.tick(60) / 1000

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			sys.exit()


	player.update(dt)


	screen.fill(BLACK)

	screen.blit(player.sprite, player.rect)
	movement_indicator.draw(player.moving)

	pygame.display.flip()