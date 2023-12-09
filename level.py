import pygame,sys
import random
from button import Button
from enum import Enum
from utils import *
from pygame import mixer


class Level_etat(Enum):
    PARTI_EN_COURS = 0
    PARTI_FINI = 1

    

class Level():
    def __init__(self,screen,display,background,player,list_enemy,objectif,niveau,next_level):
        self.screen = screen
        self.display = display
        self.background = background
        self.player = player
        self.list_enemy = list_enemy
        self.score = 0
        self.objectif = objectif
        self.niveau = niveau
        self.next_level = next_level
       
        #font
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.font2 = pygame.font.Font('freesansbold.ttf',64)

        #timer
        self.counter, self.text = 3, '3'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font1 = pygame.font.SysFont('Consolas', 30)
        #clock
        self.clock = pygame.time.Clock()

        #level etat
        self.level_etat = False
        self.etat = Level_etat.PARTI_EN_COURS

        #button next level
        self.button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 150), 
                            text_input="NEXT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        #mouse listener
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()

        #music compte pour le jouer une fois
        self.musicCount = 1

   
    
    def show_score(self):
        
        score = self.font.render("Score: "+ str(self.score),True,(255,255,255))
        self.display.blit(score,(10,10))
    def show_btn(self):
        self.button.changeColor(self.MENU_MOUSE_POS)
        self.button.update(self.display)

    def show_score_objectif(self):
        
        score = self.font.render("Objectif: "+ str(self.objectif),True,(255,255,255))
        self.display.blit(score,(520,10))
    def show_niveau(self):
        niveau = self.font.render("Niveau: "+ self.niveau,True,(255,255,255))
        self.display.blit(niveau,(250,10))

    def game_over_text(self):
        over_text = self.font2.render("GameOver",True,(255,255,255))
        self.display.blit(over_text,(250,240))
        #sound effect
        self.game_over_sound()

    def win_text(self):
        over_text = self.font2.render("Win",True,(255,255,255))
        self.display.blit(over_text,(300,240))

        #sound effect
        self.win_sound()
    def win_sound(self):
        if self.musicCount ==1:
            self.win_Sound = mixer.Sound('music/win.mp3')
            self.win_Sound.play()
            self.musicCount = 0
    def game_over_sound(self):
        if self.musicCount ==1:
            self.game_over_Sound = mixer.Sound('music/lose.mp3')
            self.game_over_Sound.play()
            self.musicCount = 0

    def show_timer(self):
        self.display.blit(self.font1.render(self.text, True, (0, 0, 0)), (300, 240))


    def timer(self):
        
        
        self.counter -= 1
        self.text = str(self.counter).rjust(3) if self.counter > 0 else ''
    def update(self):
        self.etat_level()
    
    
    #def update(self):
     #   self.show_score()
      #  self.show_score_objectif()
    def etat_level(self):
        if self.level_etat == True:
            return True
        return False
    
    def click_dectection(rect, pos):
        return True if rect.collidepoint(pos[0], pos[1]) else False

    def run(self):
            while True:

                self.MENU_MOUSE_POS = pygame.mouse.get_pos()

                for event in pygame.event.get():
            
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.USEREVENT: 
                        self.timer()

                self.display.fill((0,0,0))
                self.display.blit(self.background,(0,0))


                self.show_timer()
                pygame.draw.line(self.display, (255,0,0),(0,400),(720,400))

                #show decompte
                if  self.counter > 0:
                    self.show_niveau()
                    self.screen.blit(self.display,(0,0))
                    
                    pygame.display.update()
                    self.clock.tick(60)

                if  self.counter < 0:
                    #enemy load et update
                    for enemy in self.list_enemy:
                        enemy.update()
                    #player update
                    self.player.update()

                    #spwan enemy randomly si il ce font toucher and ++ le score
                    for enemy in self.list_enemy:
                        if self.player.bullet.isCollision(enemy.rect):
                            enemy.posX = random.randint(0,680)
                            enemy.posY = random.randint(50,100)
                            self.score += 1
                            print(self.score)

                    # affichage score et objectif
                    self.show_score()
                    self.show_score_objectif()
                
                    #if enemy depasse la base(ligne) c est game over et on mes tout les enemy en dehors du champ vision
                    for enemy in self.list_enemy:
                        if enemy.posY >=350:
                            if self.level_etat == False:
                                self.game_over_text()
                                for enemy in self.list_enemy:
                                    enemy.posY = 2000

                                self.button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 150), 
                                text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
                                self.show_btn()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if self.button.checkForInput(self.MENU_MOUSE_POS):
                                            pygame.quit()
                                            sys.exit()

                    # if score atteigne objectif c est win on mes tout les enemy en dehors du champ vision
                    if self.score == self.objectif:
                        self.level_etat = True
                        if self.level_etat == True:
                            self.win_text()
                        
                            for enemy in self.list_enemy:
                                    enemy.posY = 2000
                            #affichage du botton next
                            self.show_btn()

                        # si le btn est click on change de niveau si on a pas d autre niveau on quit
                        if self.next_level != None:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if self.button.checkForInput(self.MENU_MOUSE_POS):
                                        self.next_level.run()

                        if self.next_level == None:
                            self.button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 150), 
                            text_input="FIN", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if self.button.checkForInput(self.MENU_MOUSE_POS):
                                        pygame.quit()
                                        sys.exit()
                
                            


                    self.update()
                    self.screen.blit(self.display,(0,0))
                
                pygame.display.update()
                self.clock.tick(60)
            
                
            