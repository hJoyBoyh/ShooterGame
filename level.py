import pygame,sys
import random
import time
from player import Player
from enemy import Enemy
from enemy2 import Enemy2
from enemy3 import Enemy3

class Level():
    def __init__(self,screen,display,background,player,list_enemy,objectif,niveau):
        self.screen = screen
        self.display = display
        self.background = background
        self.player = player
        self.list_enemy = list_enemy
        self.score = 0
        self.objectif = objectif
        self.niveau = niveau
        #font
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.font2 = pygame.font.Font('freesansbold.ttf',64)

        #timer
        self.counter, self.text = 3, '3'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font1 = pygame.font.SysFont('Consolas', 30)
        #clock
        self.clock = pygame.time.Clock()

    def show_score(self):
        
        score = self.font.render("Score: "+ str(self.score),True,(255,255,255))
        self.display.blit(score,(10,10))

    def show_score_objectif(self):
        
        score = self.font.render("Objectif: "+ str(self.score_objectif),True,(255,255,255))
        self.display.blit(score,(550,10))
    def show_niveau(self):
        niveau = self.font.render("Niveau: "+ self.niveau,True,(255,255,255))
        self.display.blit(niveau,(300,10))

    def game_over_text(self):
        over_text = self.font2.render("GameOver",True,(255,255,255))
        self.display.blit(over_text,(300,240))
    def win_text(self):
        over_text = self.font2.render("Win",True,(255,255,255))
        self.display.blit(over_text,(300,240))
    def show_timer(self):
        self.display.blit(self.font1.render(self.text, True, (0, 0, 0)), (300, 350))


    def timer(self):
        
        
        self.counter -= 1
        self.text = str(self.counter).rjust(3) if self.counter > 0 else ''
    

    #def update(self):
     #   self.show_score()
      #  self.show_score_objectif()

    def run(self):
        while True:
            for event in pygame.event.get():
		
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT: 
                    self.timer()

            self.display.fill((0,0,0))
            self.display.blit(self.background,(0,0))


            self.show_timer()
            pygame.draw.line(self.display, (255,0,0),(0,350),(720,350))

            #show decompte
            if  self.counter > 0:
                self.screen.blit(self.display,(0,0))
                pygame.display.update()
                self.clock.tick(60)
            if  self.counter < 0:
                for enemy in self.list_enemy:
                    enemy.update()

                self.player.update()
              
                for enemy in self.list_enemy:
                    if self.player.bullet.isCollision(enemy.rect):
                        enemy.posX = random.randint(0,680)
                        enemy.posY = random.randint(50,100)
                        self.score += 1
                        print(self.score)

                self.show_score()
                self.show_score_objectif()
                for enemy in self.list_enemy:
                    if enemy.posY >=300:
                        self.game_over_text()
                        for enemy in self.list_enemy:
                            enemy.posY = 2000


                
                self.screen.blit(self.display,(0,0))

            pygame.display.update()
            self.clock.tick(60)
        