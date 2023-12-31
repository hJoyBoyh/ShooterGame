import pygame
from enum import Enum

class Enemy_event(Enum):
    RIGHT =0
    LEFT =1
  
class Enemy_etat(Enum):
        IDLE =0
        RUN_D =1
        RUN_G=2
       

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,display):
        super().__init__()
        #position
        self.posX = x
        self.posY = y

        self.enemyX_change = 7
        self.enemyY_change = 40

        #speed
        self.speed = 7

        # screen
        self.display = display

        #image
        self.image = pygame.Surface((32,64))
        self.image = self.image.convert()

        #image load
        self.imageLoad = pygame.image.load('images/enemy/0.png')
        self.imageLoad = pygame.transform.scale(self.imageLoad, self.image.get_size())
        self.imageLoad = self.imageLoad.convert()

        #put image load in image 
        self.image.blit(self.imageLoad,(0,0))
        self.image.set_colorkey((0,0,0))

        #pygame rect
        self.rect = self.image.get_rect(topleft = (self.posX,self.posY))

    def dessiner(self,img):
        self.display.blit(img,(self.posX,self.posY))

    def movement(self):
        self.posX += self.enemyX_change 
        self.rect = self.image.get_rect(center = (self.posX,self.posY))
        if self.posX <= 0:
            self.enemyX_change = self.speed
            self.posY =  self.posY+self.enemyY_change
            self.rect = self.image.get_rect(topleft = (self.posX,self.posY))
            
        elif self.posX >= 680:
            self.enemyX_change = -self.speed
            self.posY =  self.posY+self.enemyY_change
            self.rect = self.image.get_rect(topleft = (self.posX,self.posY))

        self.dessiner(self.image)
        

            


    def update(self):
        self.movement()

