import pygame,sys
import random
import time
from player import Player
from enemy import Enemy
from enemy2 import Enemy2
from enemy3 import Enemy3
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((720,480))
display = pygame.Surface((720,480))
clock = pygame.time.Clock()

player = Player(300,400,display)
enemy = Enemy(300,100,display)
enemy2 = Enemy2(400,100,display)
enemy3 = Enemy3(500,80,display)

#timer
counter, text = 3, '3'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font1 = pygame.font.SysFont('Consolas', 30)
#------------------------------------------


background = pygame.image.load('images/background/0.jpg')

score_objectif = 3
point = 0

font = pygame.font.Font('freesansbold.ttf',32)
def show_score(x,y):
	global point
	score = font.render("Score: "+ str(point),True,(255,255,255))
	display.blit(score,(x,y))
def show_score_objectif(x,y):
	global score_objectif
	score = font.render("Objectif: "+ str(score_objectif),True,(255,255,255))
	display.blit(score,(x,y))

over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text = over_font.render("Win",True,(255,255,255))
    display.blit(over_text,(300,240))


def timer():
	global counter,text
	counter -= 1
	text = str(counter).rjust(3) if counter > 0 else ''


while True:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.USEREVENT: 
			timer()
			
	display.fill((0,0,0))
	display.blit(background,(0,0))

	display.blit(font1.render(text, True, (0, 0, 0)), (32, 48))

	pygame.draw.line(display, (255,0,0),(0,350),(720,350))

	if  counter > 0:
		screen.blit(display,(0,0))
		pygame.display.update()
		clock.tick(60)
		
	if  counter < 0:
		enemy.update()
		enemy2.update()
		enemy3.update()
		player.update()
		#pygame.draw.rect(display,(0,100,255),collider_area)
		#timer()
		#show_timer()
		

		if player.bullet.isCollision(enemy.rect):
			enemy.posX = random.randint(0,680)
			enemy.posY = random.randint(50,100)
			point += 1
			print(point)
		if player.bullet.isCollision(enemy2.rect):
			enemy2.posX = random.randint(0,680)
			enemy2.posY = random.randint(50,100)
			point += 1
			print(point)
		if player.bullet.isCollision(enemy3.rect):
			enemy3.posX = random.randint(0,680)
			enemy3.posY = random.randint(50,100)
			point += 1
			print(point)
		#player.bullet.isCollision(enemy2.rect)
		#player.bullet.isCollision(enemy3.rect)
		show_score(10,10)
		show_score_objectif(550,10)
		
		if enemy2.posY >= 300:
			game_over_text()
			enemy2.posY = 2000
			enemy.posY = 2000
			enemy3.posY = 2000
			#player.vie -= 1
		#show_vie()
		if point == score_objectif:
			game_over_text()
			enemy2.posY = 2000
			enemy.posY = 2000
			enemy3.posY = 2000
			
		
		

		screen.blit(display,(0,0))
		
		
		
		

		pygame.display.update()
		clock.tick(60)