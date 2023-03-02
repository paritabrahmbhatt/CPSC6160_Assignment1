# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:30:47 2023

@author: parita and rintu
"""

import paddle
import ball
import screen as s


class Draw(paddle.Paddle,ball.Ball,s.Screen):

   #PADDLE1

   p1 = paddle.Paddle((255,255,255), 100, 10)
   p1.rect.x = 20
   p1.rect.y = 200

   # s.Screen.scrn.blit(p1, (x, y))

   # PADDLE 2

   p2 = paddle.Paddle((255, 255, 255), 100, 10)
   p2.rect.x = 670
   p2.rect.y = 200

   #BALL

   ball = ball.Ball((255, 255, 255), 10, 10)
   ball.rect.x = 350
   ball.rect.y = 250
