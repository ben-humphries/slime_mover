import pygame, random, sys

from player import *
from movement_indicator import *

PLAYERS_PER_GEN = 50

BLACK = (0,0,0)

class Generation:

	clock = pygame.time.Clock()

	players = []

	def __init__(self, screen, width, height):
		for i in range(PLAYERS_PER_GEN):
			self.players.append(ControlledPlayer(width, height))

		self.screen = screen
		self.clock.tick()

		self.width = width
		self.height = height

	def execute(self):

		mi = MovementIndicator(self.screen)

		elapsedTime = 0
		while elapsedTime < 2:
			dt = self.clock.tick(60) / 1000
			#dt = 1
			elapsedTime += dt

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.display.quit()
					pygame.quit()
					sys.exit()

			self.screen.fill(BLACK)


			for player in self.players:
				player.update(dt)
				self.screen.blit(player.sprite, player.rect)

			mi.draw(self.players[0].moving)

			pygame.display.flip()

	def player_fitness(self, player):

		return player.get_fitness()

	def sort_players(self):

		self.players.sort(key = self.player_fitness);

	def kill_lowest_x(self, x):

		self.sort_players()

		for i in range(x):
			del self.players[0]

	def repopulate(self):
		
		new_players = []

		for i in range(PLAYERS_PER_GEN):

			weights = [[0,0], [0,0]]

			player1 = random.choice(self.players)
			player2 = random.choice(self.players)

			for i in range(len(weights)):
				for j in range(len(weights[i])):
					if random.randint(0,1) == 1:
						weights[i][j] = player1.brain.weights[i][j]
					else:
						weights[i][j] = player2.brain.weights[i][j]

					if random.randint(0, 9) == 0: #1/10 of the time
						weights[i][j] += random.uniform(-0.2, 0.2)
						print("randomly mutated")

			player = ControlledPlayer(self.width, self.height)
			player.set_brain(NeuralNetwork(weights))
			new_players.append(player)

		self.players = new_players

	def get_new_generation(self):
		return self