# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:30:47 2023

@author: parit
"""

import paddle
import screen as s
import pygame


class Draw(paddle.Paddle,s.Screen):
    def draw(self):
        p1 = paddle.Paddle((255,0,0),100,10)
        p1.rect.x = 20
        p1.rect.y = 200

        #s.Screen.scrn.blit(p1, (x, y))
        
        #PADDLE 2
        
        p2 = paddle.Paddle((255,0,0), 100, 10)
        p2.rect.x = 670
        p2.rect.y = 200
        
        all_sprites = pygame.sprite.Group()
        all_sprites.add(p1)
        all_sprites.add(p2)

        all_sprites.update()
        all_sprites.draw(s.Screen.scrn)