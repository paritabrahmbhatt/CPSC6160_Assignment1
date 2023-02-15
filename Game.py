# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:31:05 2023

@author: parita
"""

import screen as s
import pygame
from pygame import mixer
import draw
class Game(s.Screen):
    def run(self):
        running = True
        mixer.music.load(r"Music/bgMusic.wav")
        mixer.music.play(-1)
        while running:
            s.Screen.scrn.fill((255,255,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            
            pygame.draw.line(s.Screen.scrn, ((255,255,255)), [349, 0], [349, 500], 5)
            
            #s.Screen.scrn.blit()
            draw.Draw.draw(self)
            pygame.display.flip()
            s.Screen.clock.tick(60)

        pygame.quit()
