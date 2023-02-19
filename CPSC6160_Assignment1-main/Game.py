# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:31:05 2023

@author: parita
"""
import paddle
import screen as s
import pygame
from pygame import mixer
import draw as d




class Game(s.Screen):
    def run(self):
        running = True
        mixer.music.load(r"Music/bgMusic.wav")
        mixer.music.play(-1)

        player1 = 0
        player2 = 0

        all_sprites = pygame.sprite.Group()
        all_sprites.add(d.Draw.p1)
        all_sprites.add(d.Draw.p2)
        all_sprites.add(d.Draw.ball)

        while running:
            s.Screen.scrn.fill((255,255,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                d.Draw.p1.moveUp(10)
            if keys[pygame.K_s]:
                d.Draw.p1.moveDown(10)
            if keys[pygame.K_UP]:
                d.Draw.p2.moveUp(10)
            if keys[pygame.K_DOWN]:
                d.Draw.p2.moveDown(10)

            all_sprites.update()

            if d.Draw.ball.rect.x >= 690:
                player1 += 1
                d.Draw.ball.vel[0] = -d.Draw.ball.vel[0]
            if d.Draw.ball.rect.x <= 0:
                player2 += 1
                d.Draw.ball.vel[0] = -d.Draw.ball.vel[0]
            if d.Draw.ball.rect.y > 490:
                d.Draw.ball.vel[1] = -d.Draw.ball.vel[1]
            if d.Draw.ball.rect.y < 0:
                d.Draw.ball.vel[1] = -d.Draw.ball.vel[1]

            if pygame.sprite.collide_mask(d.Draw.ball, d.Draw.p1) or pygame.sprite.collide_mask(d.Draw.ball, d.Draw.p2):
                d.Draw.ball.bounce()


            all_sprites.draw(s.Screen.scrn)

            pygame.draw.line(s.Screen.scrn, ((255,255,255)), [349, 0], [349, 500], 5)
            
            #s.Screen.scrn.blit()
            # d.Draw.draw(self)

            font = pygame.font.Font(None, 74)
            text = font.render(str(player1), 1, (0,0,0))
            s.Screen.scrn.blit(text, (250, 10))
            text = font.render(str(player2), 1, (0,0,0))
            s.Screen.scrn.blit(text, (420, 10))


            pygame.display.flip()
            s.Screen.clock.tick(60)

        pygame.quit()
