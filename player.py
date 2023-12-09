import pygame,sys,os
from bullet import *
from enum import Enum

class Player_event(Enum):
    K_LEFT_DN =0
    K_RIGHT_DN =1
    K_RIGHT_LEFT_UP =2
    K_SPACE_DN=3
    K_SPACE_UP=4
class Player_etat(Enum):
        IDLE =0
        RUN_D =1
        RUN_G=2
        NO_SHOOT=3
        SHOOT=4

class  Player(pygame.sprite.Sprite):
    def __init__(self,x,y,display):
        super().__init__()
       
        # position
        self.playerX_change = 100
        
        self.posX = x
        self.posY = y

        #ETAT
        self.etat_X = Player_etat.IDLE
        self.etat_shoot = Player_etat.NO_SHOOT


        #speed
        self.speed = 8

        # screen
        self.display = display

        #image
        self.image = pygame.Surface((32,64))
        self.image = self.image.convert()

        self.image_idle = []
        self.image_run = []
        self.get_image_player()

        self.current_image = 0
    

        #image load
        self.imageLoad = self.image_run[self.current_image]
        self.imageLoad = pygame.transform.scale(self.imageLoad, self.image.get_size())
        self.imageLoad = self.imageLoad.convert()

        #img height widtdh
        self.imageH = self.image.get_height()
        self.imageW = self.image.get_width()

        #put image load in image 
        self.image.blit(self.imageLoad,(0,0))
        self.image.set_colorkey((0,0,0))
        
        #avec animation ici
        #for img in self.image_run:
        #   img =pygame.transform.scale(img, self.image.get_size())
        #    img.convert()
        #self.image = self.image_run[self.current_image]
        

        self.flip_img = False

        self.moving_img = pygame.sprite.Group()

      
        #pygame rect
        self.rect = self.image.get_rect(topleft = (self.posX,self.posY))

         #bullet
        self.bullet = Bullet(0,self.posY,self.display)

        
    

    #def animate(self,speed):
    #    self.current_image += speed
    #    if int(self.current_image) >= len(self.image_run):
    #        self.current_image = 0
           

    #   self.image = self.image_run[int(self.current_image)]
          
    def box_collider_update(self):
        self.posX = self.playerX_change
        self.rect = self.image.get_rect(topleft = (self.posX,self.posY))

        #pour monter avec animation enleve img de ce parametre
    def dessiner(self,img):
       self.display.blit(img,(self.posX,self.posY))
        
        #self.moving_img.draw(self.display)
        
    
    def movement(self):
        

        if self.etat_X == Player_etat.RUN_D:
            self.playerX_change += self.speed
            self.flip_img = True
           # self.animate(0.25)
        if self.etat_X == Player_etat.RUN_G:
            self.playerX_change -= self.speed
            self.flip_img = False
           # self.animate(0.25)
        if self.etat_X == Player_etat.IDLE:
            self.current_image = 0
            #self.animate(0.25)
            

        self.box_collider_update()
        self.check_mur_invicible()

        
        #flip au cas ou il retourne
        if self.flip_img == True:
            flip_img= pygame.transform.flip(self.image,True,False)
          
            self.dessiner(flip_img)
            
        if self.flip_img == False:
            flip_img=pygame.transform.flip(self.image,False,False)
            self.dessiner(flip_img)

    def tirer(self):
        if self.etat_shoot == Player_etat.SHOOT:
            if self.bullet.etat is Bullet_etat.READY:
                #garder position bullet
                self.bullet.posX = self.posX
                self.rect = self.bullet.image.get_rect(center = (self.bullet.posX,self.bullet.posY))
                self.bullet.fire_bullet(self.bullet.posX,self.bullet.posY)

                self.bullet_Sound = mixer.Sound('music/laser.wav')
                self.bullet_Sound.play()
            

    def check_mur_invicible(self):
        if self.posX <= 0:
            self.playerX_change = 0
            
        elif self.posX >= 695:
            self.playerX_change = 690

       
    def get_image_player(self):
        self.image_path = 'images/player/'

       
        
        fichiers = os.listdir(self.image_path + "idle")
        print(fichiers)
        fichiers.sort()
        for fichier in fichiers:
            img = pygame.image.load(self.image_path + "idle/" + fichier)
            #rect = img.get_rect()
            #rect.center(self.posX,self.posY)
            self.image_idle.append(img)

       # self.rect = self.image_idle[0].get_rect()
        #self.rect.center(self.posX,self.posY)
        
        self.image_run = []
        fichiers = os.listdir(self.image_path + "run")
        print(fichiers)
        fichiers.sort()
        for fichier in fichiers:
            img = pygame.image.load(self.image_path + "run/" + fichier)
            rect = img.get_rect()
          #  rect.center(self.posX,self.posY)
            self.image_run.append(img)

        
    def fonctionnementPlayer(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.set_etat(Player_event.K_SPACE_DN)
        elif not keys[pygame.K_SPACE]:
            self.set_etat(Player_event.K_SPACE_UP)
        
        

        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] :
            self.set_etat(Player_event.K_RIGHT_DN)
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] :
            self.set_etat(Player_event.K_LEFT_DN)
        else:
            self.set_etat(Player_event.K_RIGHT_LEFT_UP)

       
        
        
    
      


    def set_etat(self,event):
        if self.etat_X == Player_etat.IDLE and event == Player_event.K_RIGHT_DN:
            self.etat_X = Player_etat.RUN_D

        if self.etat_X == Player_etat.IDLE and event == Player_event.K_LEFT_DN:
            self.etat_X = Player_etat.RUN_G

        if self.etat_X == Player_etat.RUN_G and event == Player_event.K_RIGHT_LEFT_UP\
            or self.etat_X == Player_etat.RUN_D and event == Player_event.K_RIGHT_LEFT_UP:
            self.etat_X = Player_etat.IDLE

        if self.etat_shoot == Player_etat.NO_SHOOT and event == Player_event.K_SPACE_DN:
            self.etat_shoot = Player_etat.SHOOT
        if self.etat_shoot == Player_etat.SHOOT and event == Player_event.K_SPACE_UP:
            self.etat_shoot = Player_etat.NO_SHOOT

    def update(self):

        self.fonctionnementPlayer()
        #self.moving_img.add(self)
        self.movement()
        self.bullet.update()
        self.tirer()
        
        