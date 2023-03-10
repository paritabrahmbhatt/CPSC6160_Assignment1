# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:18:17 2023

@author: parita and rintu
"""

import pygame 
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        
        super().__init__()
         
        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        pygame.draw.rect(self.image, color, [0, 0, width,height])
        
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400