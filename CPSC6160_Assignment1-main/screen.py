# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:19:03 2023

@author: parita
"""

import math
import random
import os
import pygame
from pygame import mixer
import sys


#Generalized block of screen
class Screen():
    __instance = None
    pygame.init()
    size = (700,500)
    title = "Pong"
    icon = pygame.image.load(r'Images/pong.ico')
    scrn = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    
    pygame.display.set_caption(title)
    pygame.display.set_icon(icon)
    
