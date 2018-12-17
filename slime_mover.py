import pygame, sys

from player import *
from movement_indicator import *
from generation import *
from neural_network import *

RUN_GENERATIONS = 1

pygame.init()

size = width, height = 800, 600
BLACK = (0,0,0)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

player = ControlledPlayer(width, height)
movement_indicator = MovementIndicator(screen)

if(RUN_GENERATIONS == 0):

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
else:

	generation = Generation(screen, width, height)

	for i in range(100):

		generation.execute()
		generation.kill_lowest_x(25)
		generation.repopulate()
		print(generation.players[-1].brain.weights)
		generation = generation.get_new_generation()

