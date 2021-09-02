import pygame
from pygame.locals import *

screen_x, screen_y = 1300, 600
SIZE = 40


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load(
            "Python39/Snake Game/resources/block.jpg").convert()
        self.length = length
        self.x = [SIZE]*self.length
        self.y = [SIZE]*self.length
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        elif self.direction == 'right':
            self.x[0] += SIZE
        elif self.direction == 'up':
            self.y[0] -= SIZE
        elif self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increaseLength(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
