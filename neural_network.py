import random
import numpy as np

class NeuralNetwork():


	def __init__(self):
		pass

	def randomize_weights(self):
		self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]
		print(self.weights)

	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	def think(self, inputs):

		outputs = [self.sigmoid(i * w + 2) for i, w in zip(inputs, self.weights)]

		return outputs
