import paddle
import screen as s
import pygame
from pygame import mixer
import draw as d




class Game(s.Screen):
    def run(self):
        running = True
        game_over = False
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
            pygame.draw.line(s.Screen.scrn, ((255,0,0)), [349, 0], [349, 500], 5)
            #pygame.display.flip()
            
            #Drawing Paddles and ball on the screen.
            all_sprites.draw(s.Screen.scrn)
            
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
                if(player1 != 11):
                    d.Draw.ball.rect.x = 350
                    d.Draw.ball.rect.y = 250
                    d.Draw.p1.rect.x = 20
                    d.Draw.p1.rect.y = 200
                    d.Draw.p2.rect.x = 670
                    d.Draw.p2.rect.y = 200
                    
                    #pygame.time.delay(1000)
                    all_sprites.update()
                    #pygame.display.update()
                else:
                    game_over = True
                
                
                
            elif d.Draw.ball.rect.x <= 0:
                player2 += 1
                d.Draw.ball.vel[0] = -d.Draw.ball.vel[0]
                if(player2 != 11):
                    d.Draw.ball.rect.x = 350
                    d.Draw.ball.rect.y = 250
                    d.Draw.p1.rect.x = 20
                    d.Draw.p1.rect.y = 200
                    d.Draw.p2.rect.x = 670
                    d.Draw.p2.rect.y = 200
                    
                    all_sprites.update()
                    #pygame.time.delay(1000)
                    #pygame.display.update()
                    
                else:
                    game_over = True
               
            elif d.Draw.ball.rect.y > 490:
                d.Draw.ball.vel[1] = -d.Draw.ball.vel[1]
                
            elif d.Draw.ball.rect.y < 0:
                d.Draw.ball.vel[1] = -d.Draw.ball.vel[1]

            if pygame.sprite.collide_mask(d.Draw.ball, d.Draw.p1) or pygame.sprite.collide_mask(d.Draw.ball, d.Draw.p2):
                d.Draw.ball.bounce()

            #s.Screen.scrn.blit()
            # d.Draw.draw(self)

            if(game_over == False):
                font = pygame.font.Font(None, 74)
                text = font.render(str(player1), 1, (0, 0, 0))
                s.Screen.scrn.blit(text, (250, 10))
                text = font.render(str(player2), 1, (0, 0, 0))
                s.Screen.scrn.blit(text, (420, 10))
                

            else:
                font = pygame.font.Font(None, 74)
                text = font.render(str(player1), 1, (0, 0, 0))
                s.Screen.scrn.blit(text, (250, 10))
                text = font.render(str(player2), 1, (0, 0, 0))
                s.Screen.scrn.blit(text, (420, 10))
                pygame.display.update()

                if(player1==5):
                    font = pygame.font.Font(None, 74)
                    text = font.render("Player 1 wins", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(700 / 2, 500/ 2))
                    s.Screen.scrn.blit(text, text_rect)
                    pygame.display.update()
                    pygame.time.delay(2000)
                else:
                    font = pygame.font.Font(None, 74)
                    text = font.render("Player 2 wins", True, (0, 0, 0))
                    text_rect = text.get_rect(center=(700 / 2, 500 / 2))
                    s.Screen.scrn.blit(text, text_rect)
                    pygame.display.update()
                    pygame.time.delay(2000)

                running=False

            pygame.display.flip()
            s.Screen.clock.tick(60)

        pygame.quit()
