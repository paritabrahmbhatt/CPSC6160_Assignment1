# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:31:05 2023

@author: parit
"""

import screen as s
import pygame
from pygame import mixer

class Game(s.Screen):
    def run(self):
        running = True
        mixer.music.load(r"Music/bgMusic.wav")
        mixer.music.play(-1)
        while running:
            s.screen.fill(0,0,0)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            pygame.display.update()