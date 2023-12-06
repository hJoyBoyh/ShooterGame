import pygame
from enemy import Enemy
from enum import Enum


    
class Bullet_etat(Enum):
    READY=1
    FIRE=2

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,display):
        super().__init__()
        
        #position
        self.posX = x
        self.posY = y

        self.x_change = 0
        self.y_change = 10


        # screen
        self.display = display

        #image 
        self.image = pygame.Surface((32,64))
        self.image = self.image.convert()
        self.image.blit(pygame.image.load('images/bullet/0.png'),(0,0))
        self.image.set_colorkey((0,0,0))

        #rect
        self.rect = self.image.get_rect(topleft = (self.posX,self.posY))

        #enemy list
        self.enemy = Enemy

        # etat
        self.etat = Bullet_etat.READY

    def fire_bullet(self,x,y):
        
        
        self.set_etat(Bullet_etat.FIRE)
        self.display.blit(self.image,(x+16,y+10))
        self.rect = self.image.get_rect(center = (x+16,y+10))
    
    def isCollision(self,rect_enemy):
       
        if self.rect.colliderect(rect_enemy):
            self.posY=400
            self.posX = 1000
            self.rect = self.image.get_rect(center = (400,1000))
            
            self.set_etat(Bullet_etat.READY)
            return True
        return False

    def set_etat(self,etat):
        self.etat= etat
        

    def update(self):
        if self.posY<=0:
            self.posY=400
            self.set_etat(Bullet_etat.READY)
        if self.etat == Bullet_etat.FIRE:
            self.fire_bullet(self.posX,self.posY)
            self.posY -= self.y_change