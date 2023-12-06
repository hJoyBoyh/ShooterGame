import pygame,sys

from player import Player
from enemy import Enemy
from enemy2 import Enemy2
from enemy3 import Enemy3
from level import Level

from button import Button
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((720,480))
display = pygame.Surface((720,480))
clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# detection click bouton
def click_dectection(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False

player = Player(300,400,display)

enemy = Enemy(300,100,display)
enemy2 = Enemy2(400,100,display)
enemy3 = Enemy3(500,80,display)
list_enemy = []

list_enemy.append(enemy)
list_enemy.append(enemy2)
list_enemy.append(enemy3)

enemy4 = Enemy(300,100,display)
enemy5 = Enemy2(400,100,display)
enemy6 = Enemy3(500,80,display)
list_enemy2 = []

list_enemy2.append(enemy4)
list_enemy2.append(enemy5)
list_enemy2.append(enemy6)

background = pygame.image.load('images/background/0.jpg')



level2 = Level(screen,display,background,player,list_enemy2,3,"2",None)
level = Level(screen,display,background,player,list_enemy,3,"1",level2)

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