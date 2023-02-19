# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:30:47 2023

@author: parit
"""

import paddle
import ball
import screen as s
import pygame


class Draw(paddle.Paddle,ball.Ball,s.Screen):

   #PADDLE1

   p1 = paddle.Paddle((255, 0, 0), 100, 10)
   p1.rect.x = 20
   p1.rect.y = 200

   # s.Screen.scrn.blit(p1, (x, y))

   # PADDLE 2

   p2 = paddle.Paddle((255, 0, 0), 100, 10)
   p2.rect.x = 670
   p2.rect.y = 200

   #BALL

   ball = ball.Ball((54, 69, 79), 10, 10)
   ball.rect.x = 345
   ball.rect.y = 195

