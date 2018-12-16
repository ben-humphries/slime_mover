import pygame

class MovementIndicator:

	WHITE = (255,255,255)
	RED = (255, 0, 0)

	rects = up, down, left, right = pygame.Rect(50, 500, 48, 48), pygame.Rect(50,550,48,48), pygame.Rect(0,550,48,48), pygame.Rect(100,550,48,48)

	def __init__(self, screen):
		self.screen = screen

	def draw(self, moving):

		for i in range(4):
			pygame.draw.rect(self.screen, self.RED if moving[i] == 1 else self.WHITE, self.rects[i])



