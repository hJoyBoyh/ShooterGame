import pygame,sys,os
from bullet import Bullet
class  Player(pygame.sprite.Sprite):
    def __init__(self,x,y,display):
        super().__init__()
       
        # position
        self.playerX_change = 100
        
        self.posX = x
        self.posY = y

        #speed
        self.speed = 5

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

        #put image load in image 
        self.image.blit(self.imageLoad,(0,0))
        self.image.set_colorkey((0,0,0))

        self.flip_img = False

      
        #pygame rect
        self.rect = self.image.get_rect(topleft = (self.posX,self.posY))

         #bullet
        self.bullet = Bullet(0,self.posY,self.display)

        # vie
        self.vie = 3
        

        
    def box_collider_update(self):
        self.posX = self.playerX_change
        self.rect = self.image.get_rect(topleft = (self.posX,self.posY))

    def dessiner(self,img):
        self.display.blit(img,(self.posX,self.posY))
    
    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.playerX_change += self.speed
            self.flip_img = True
        if keys[pygame.K_LEFT]:
            self.playerX_change -= self.speed
            self.flip_img = False

        self.box_collider_update()
        self.check_mur_invicible()

        

        if self.flip_img == True:
            flipped_image = pygame.transform.flip(self.image,True,False)
          
            self.dessiner(flipped_image)
            

        if self.flip_img == False:
            flipped_image = pygame.transform.flip(self.image,False,False)
            self.dessiner(self.image)

    def tirer(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if self.bullet.bullet_etat is 'ready':
                self.bullet.posX = self.posX
                self.rect = self.bullet.image.get_rect(center = (self.bullet.posX,self.bullet.posY))
                self.bullet.fire_bullet(self.bullet.posX,self.bullet.posY)
            

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

        
        

        pass
   # def animate(self):
    #    self.imageLoad = self.image_run[int(self.current_image)]
     #   if self.animatePersonnage == True:
           
      #      self.current_image += 0.2

       #     if self.current_image >= len(self.image_run):
        #        self.current_image =0 

        #self.imageLoad = self.image_run[int(self.current_image)]
        
        
    def update(self):
        
        #self.dessiner()

        self.movement()
       
        self.bullet.update()
        self.tirer()
      #  self.animate()



