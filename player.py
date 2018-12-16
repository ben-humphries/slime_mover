import pygame

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

