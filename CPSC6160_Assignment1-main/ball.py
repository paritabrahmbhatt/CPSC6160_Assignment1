import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.vel = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

    def bounce(self):
        self.vel[0] = -self.vel[0]
        self.vel[1] = randint(-8, 8)