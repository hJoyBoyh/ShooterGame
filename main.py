import pygame,sys
from player import Player
from enemy import Enemy
from enemy2 import Enemy2
from enemy3 import Enemy3
from level import Level
from utils import *
from pygame import mixer
from button import Button

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((720,480))
display = pygame.Surface((720,480))
clock = pygame.time.Clock()

#background sound
mixer.music.load('music/backgroundMusic.mp3')
mixer.music.play(-1)



player = Player(300,400,display)
# first enemys
enemy = Enemy(300,100,display)
enemy2 = Enemy(400,100,display)
enemy3 = Enemy(500,80,display)
enemy4 = Enemy(300,100,display)
enemy5 = Enemy(400,100,display)

list_enemy = []

list_enemy.append(enemy)
list_enemy.append(enemy2)
list_enemy.append(enemy3)
list_enemy.append(enemy4)
#-----------------------------------------
#second round enemys
enemy7 = Enemy(300,100,display)
enemy8 = Enemy(400,100,display)
enemy9 = Enemy(500,80,display)
enemy10 = Enemy(400,100,display)
enemy11 = Enemy2(500,80,display)
list_enemy2 = []

list_enemy2.append(enemy7)
list_enemy2.append(enemy8)
list_enemy2.append(enemy9)
list_enemy2.append(enemy10)
list_enemy2.append(enemy11)

#third round enemys
enemy12 = Enemy(300,100,display)
enemy13= Enemy3(400,100,display)
enemy14 = Enemy3(500,80,display)
enemy15 = Enemy2(400,100,display)
enemy16 = Enemy(500,80,display)
list_enemy3 = []

list_enemy3.append(enemy12)
list_enemy3.append(enemy13)
list_enemy3.append(enemy14)
list_enemy3.append(enemy15)
list_enemy3.append(enemy16)
#last round enemys
enemy17 = Enemy3(300,100,display)
enemy18= Enemy3(400,100,display)
enemy19 = Enemy3(500,80,display)
enemy20 = Enemy2(400,100,display)
enemy21 = Enemy3(500,80,display)
enemy22 = Enemy2(500,80,display)
enemy23 = Enemy2(400,100,display)
enemy24 = Enemy2(500,80,display)


list_enemy4 = []

list_enemy4.append(enemy17)
list_enemy4.append(enemy18)
list_enemy4.append(enemy19)
list_enemy4.append(enemy20)
list_enemy4.append(enemy21)
list_enemy4.append(enemy22)
list_enemy4.append(enemy23)


background = pygame.image.load('images/background/0.jpg')
background2 = pygame.image.load('images/background/1.jpg')
background3 = pygame.image.load('images/background/2.jpg')
background4 = pygame.image.load('images/background/4.jpg')

level4 = Level(screen,display,background4,player,list_enemy4,50,"Finale",None)
level3 = Level(screen,display,background3,player,list_enemy3,25,"3",level4)
level2 = Level(screen,display,background2,player,list_enemy2,10,"2",level3)
level = Level(screen,display,background,player,list_enemy,5,"1",level2)
#level4 = Level(screen,display,background4,player,list_enemy4,30,"Finale",None)

def main_menu():
    
    while True:
       
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 250), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(350, 400), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                   level.run()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    
        pygame.display.update()
main_menu()