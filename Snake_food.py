import pygame
from pygame.locals import *
import random

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120
        self.apple_img = pygame.image.load(
            "Python39/Snake Game/resources/apple.jpg").convert()

    def draw(self):
        self.parent_screen.blit(self.apple_img, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24)*SIZE
        self.y = random.randint(1, 12)*SIZE
