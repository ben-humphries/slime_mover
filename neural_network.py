import random
import numpy as np

class NeuralNetwork():

	# weights = [i1->o, i2->o]
	# i1->o = [->o1, ->o2]
	# i2->o = [->o1, ->o2]

	bias = 1

	def __init__(self, weights = [[random.uniform(-1, 1), random.uniform(-1, 1)], [random.uniform(-1, 1), random.uniform(-1, 1)]]):
		self.weights = weights

	def randomize_weights(self):
		self.weights = [[random.uniform(-1, 1), random.uniform(-1, 1)], [random.uniform(-1, 1), random.uniform(-1, 1)]]

	def set_weights(self, weights):
		self.weights = weights

	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	def think(self, inputs):

		o1 = self.sigmoid(inputs[0] * self.weights[0][0] + inputs[1] * self.weights[1][0] + self.bias)
		o2 = self.sigmoid(inputs[0] * self.weights[0][1] + inputs[1] * self.weights[1][1] + self.bias)

		outputs = [o1, o2]

		return outputs
