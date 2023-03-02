# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:19:03 2023

@author: parita
"""

import pygame

#Generalized block of screen
class Screen():
    #__instance = None
    pygame.init()
    size = (700,500)
    
    #Giving the title
    title = "Pong"
    pygame.display.set_caption(title)
    
    #Puttong icon of Pong
    icon = pygame.image.load(r'Images/pong.ico')
    pygame.display.set_icon(icon)
    
    main_font = pygame.font.SysFont("cambria", 50)

    scrn = pygame.display.set_mode(size)
    
    clock = pygame.time.Clock()
    
