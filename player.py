import pygame, random
from neural_network import *

class Player:

    speed = 300
    sprite = pygame.image.load("ball.png")
    rect = sprite.get_rect()

    moving = [0, 0, 0, 0]

    width, height = 0,0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def update(self, dt):

        self.handle_movement(dt)

    def handle_movement(self, dt):

        tomove = [0, 0]
        keys = pygame.key.get_pressed()

        self.moving = [0,0,0,0]
        
        if keys[ord('a')]:
            tomove[0] -= self.speed * dt
            self.moving[2] = 1
        if keys[ord('d')]:
            tomove[0] += self.speed * dt
            self.moving[3] = 1
        if keys[ord('w')]:
            tomove[1] -= self.speed * dt
            self.moving[0] = 1
        if keys[ord('s')]:
            tomove[1] += self.speed * dt
            self.moving[1] = 1

        #if tomove[0] != 0 and tomove[1] != 0:
         #   tomove = [i / 1.414 for i in tomove] #sqrt(2)

        self.rect = self.rect.move(tomove)

        self.check_collision()

    def check_collision(self):

        if self.rect.left < 0:
            self.rect = self.rect.move([-self.rect.left, 0])
        elif self.rect.right > self.width:
            self.rect = self.rect.move([self.width - self.rect.right, 0])

        if self.rect.top < 0:
            self.rect = self.rect.move([0, -self.rect.top])
        elif self.rect.bottom > self.height:
            self.rect = self.rect.move([0, self.height - self.rect.bottom])


class ControlledPlayer(Player):

    brain = NeuralNetwork()

    def __init__(self, width, height):
        self.brain.randomize_weights()
        self.width = width
        self.height = height

        self.rect.left = 5
        self.rect.top = height / 2

    def update(self, dt):

        output = self.brain.think([self.rect.left, self.rect.top])

        self.tomove = [0,0,0,0]

        if output[0] > 0.8:
            self.tomove[2] = 1
        elif output[0] < 0.2:
            self.tomove[3] = 1
        
        if output[1] > 0.8:
            self.tomove[1] = 1
        elif output[1] < 0.2:
            self.tomove[0] = 1

        self.handle_movement(dt)

    def handle_movement(self, dt):

        tomove = [0, 0]
        self.moving = [0,0,0,0]
        
        if self.tomove[2] == 1:
            tomove[0] -= self.speed * dt
            self.moving[2] = 1
        if self.tomove[3] == 1:
            tomove[0] += self.speed * dt
            self.moving[3] = 1
        if self.tomove[0] == 1:
            tomove[1] -= self.speed * dt
            self.moving[0] = 1
        if self.tomove[1] == 1:
            tomove[1] += self.speed * dt
            self.moving[1] = 1

        #if tomove[0] != 0 and tomove[1] != 0:
          #  tomove = [i / 1.414 for i in tomove] #sqrt(2)

        self.rect = self.rect.move(tomove)

        self.check_collision()
