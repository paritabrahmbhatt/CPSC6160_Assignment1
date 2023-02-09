# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:19:03 2023

@author: parit
"""

import math
import random
import os
import pygame
from pygame import mixer
import sys


#Generalized block of screen
class Screen():
    pygame.init()
    size = (700,500)
    title = "Pong"
    icon = pygame.image.load(r'Images/pong.ico')
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    pygame.display.set_icon(icon)

    