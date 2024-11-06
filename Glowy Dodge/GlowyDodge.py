import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_run1 = pygame.image.load('graphics/player/run/run1.png').convert_alpha()
		player_run2 = pygame.image.load('graphics/player/run/run2.png').convert_alpha()
		player_run3 = pygame.image.load('graphics/player/run/run3.png').convert_alpha()
		player_run4 = pygame.image.load('graphics/player/run/run4.png').convert_alpha()
		player_run5 = pygame.image.load('graphics/player/run/run5.png').convert_alpha()
		player_run6 = pygame.image.load('graphics/player/run/run6.png').convert_alpha()
		player_run7 = pygame.image.load('graphics/player/run/run7.png').convert_alpha()
		player_run8 = pygame.image.load('graphics/player/run/run8.png').convert_alpha()
		player_run9 = pygame.image.load('graphics/player/run/run9.png').convert_alpha()
		player_run10 = pygame.image.load('graphics/player/run/run10.png').convert_alpha()
		player_run11 = pygame.image.load('graphics/player/run/run11.png').convert_alpha()
		player_run12 = pygame.image.load('graphics/player/run/run12.png').convert_alpha()
		self.player_run = [player_run1,player_run2,player_run3,player_run4,player_run5,player_run6,player_run7,player_run8,player_run9,player_run10,player_run11,player_run12]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/player/jump/jump.png').convert_alpha()
		self.player_slide = pygame.image.load('graphics/player/slide/slide.png').convert_alpha()

		self.image = self.player_run[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,575))
		self.gravity = 0
		self.floor = 580
		self.isSliding = False

		self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= self.floor:
			self.gravity = -20
			self.jump_sound.play()
		if keys[pygame.K_DOWN] and self.rect.bottom >= self.floor:
			self.isSliding = True
			self.floor = 600
		else:
			self.isSliding = False
			self.floor = 580



	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= self.floor:
			self.rect.bottom = self.floor

	def animation_state(self):
		if self.rect.bottom < self.floor: 
			self.image = self.player_jump
		elif self.isSliding:
			self.image = self.player_slide
		else:
			self.player_index += 0.25
			if self.player_index >= len(self.player_run):self.player_index = 0
			self.image = self.player_run[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'shark':
			shark1 = pygame.image.load('graphics/shark/shark1.png').convert_alpha()
			shark2 = pygame.image.load('graphics/shark/shark2.png').convert_alpha()
			shark3 = pygame.image.load('graphics/shark/shark3.png').convert_alpha()
			shark4 = pygame.image.load('graphics/shark/shark4.png').convert_alpha()
			shark5 = pygame.image.load('graphics/shark/shark5.png').convert_alpha()
			shark6 = pygame.image.load('graphics/shark/shark6.png').convert_alpha()
			self.frames = [shark1,shark2,shark3,shark4,shark5,shark6]
			y_pos = 510
		elif type == 'jerma':
			jerma1 = pygame.image.load('graphics/jerma/jerma1.png').convert_alpha()
			jerma2 = pygame.image.load('graphics/jerma/jerma2.png').convert_alpha()
			jerma3 = pygame.image.load('graphics/jerma/jerma3.png').convert_alpha()
			jerma4 = pygame.image.load('graphics/jerma/jerma4.png').convert_alpha()
			jerma5 = pygame.image.load('graphics/jerma/jerma5.png').convert_alpha()
			jerma6 = pygame.image.load('graphics/jerma/jerma6.png').convert_alpha()
			jerma7 = pygame.image.load('graphics/jerma/jerma7.png').convert_alpha()
			self.frames = [jerma1,jerma2,jerma3,jerma4,jerma5,jerma6,jerma7]
			y_pos = 480
		elif type == 'bomber':
			bomber1 = pygame.image.load('graphics/bomber/bomber1.png').convert_alpha()
			bomber2 = pygame.image.load('graphics/bomber/bomber2.png').convert_alpha()
			bomber3 = pygame.image.load('graphics/bomber/bomber3.png').convert_alpha()
			bomber4 = pygame.image.load('graphics/bomber/bomber4.png').convert_alpha()
			bomber5 = pygame.image.load('graphics/bomber/bomber5.png').convert_alpha()
			bomber6 = pygame.image.load('graphics/bomber/bomber6.png').convert_alpha()
			self.frames = [bomber1,bomber2,bomber3,bomber4,bomber5,bomber6]
			y_pos  = 580
		elif type == 'amogus':
			amogus1 = pygame.image.load('graphics/amogus/amogus1.png').convert_alpha()
			amogus2 = pygame.image.load('graphics/amogus/amogus2.png').convert_alpha()
			amogus3 = pygame.image.load('graphics/amogus/amogus3.png').convert_alpha()
			amogus4 = pygame.image.load('graphics/amogus/amogus4.png').convert_alpha()
			amogus5 = pygame.image.load('graphics/amogus/amogus5.png').convert_alpha()
			amogus6 = pygame.image.load('graphics/amogus/amogus6.png').convert_alpha()
			self.frames = [amogus1,amogus2,amogus3,amogus4,amogus5,amogus6]
			y_pos  = 580

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(1300,1500),y_pos))

	def animation_state(self):
		self.animation_index += 0.3
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 7
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = score_font.render('Score: ' + str(current_time),False,'white')
	score_rect = score_surf.get_rect(center = (640,50))
	screen.blit(score_surf,score_rect)
	return current_time

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		death_sound = pygame.mixer.Sound('audio/bleh.mp3')
		death_sound.set_volume(1)
		death_sound.play()
		return False
	else: return True


pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Glowy Dodge - Group 4')
clock = pygame.time.Clock()
title_font = pygame.font.Font('font/BACKTO1982.ttf', 50)
score_font = pygame.font.Font('font/slkscrb.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.mp3')
bg_music.set_volume(0.2)
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surf = pygame.image.load('graphics/background/sky.png').convert()
road_surf = pygame.image.load('graphics/background/road.png').convert_alpha()

star_surf = pygame.image.load('graphics/background/stars.png').convert_alpha()
star_rect = star_surf.get_rect(topleft = (0,0))
star_rect2 = star_surf.get_rect(topleft = (2560,0))
cloud_surf = pygame.image.load('graphics/background/clouds.png').convert_alpha()
cloud_rect = cloud_surf.get_rect(topleft = (0,0))
cloud_rect2 = cloud_surf.get_rect(topleft = (2560,0))
building_surf = pygame.image.load('graphics/background/buildings.png').convert_alpha()
building_rect = building_surf.get_rect(topleft = (0,0))
building_rect2 = building_surf.get_rect(topleft = (2560,0))

# Intro screen
game_name = title_font.render('Glowy Dodge',False,'white')
game_name_rect = game_name.get_rect(center = (640,80))

game_message = title_font.render('Press space to jump',False,'white')
game_message2 = title_font.render('down arrow to slide',False,'white')
game_message_rect = game_message.get_rect(center = (640,450))
game_message_rect2 = game_message2.get_rect(center = (640,530))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['shark','shark','jerma','bomber','bomber','bomber','amogus'])))
		
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)

	screen.blit(sky_surf,(0,0))
		
	star_rect.x -= 3
	if star_rect.right<=0: star_rect.left = 2560
	screen.blit(star_surf,star_rect)
	star_rect2.x -= 3
	if star_rect2.right<=0: star_rect2.left = 2560
	screen.blit(star_surf,star_rect2)

	cloud_rect.x -= 2
	if cloud_rect.right<=0: cloud_rect.left = 2560
	screen.blit(cloud_surf,cloud_rect)
	cloud_rect2.x -= 2
	if cloud_rect2.right<=0: cloud_rect2.left = 2560
	screen.blit(cloud_surf,cloud_rect2)

	building_rect.x -= 1
	if building_rect.right<=0: building_rect.left = 2560
	screen.blit(building_surf,building_rect)
	building_rect2.x -= 1
	if building_rect2.right<=0: building_rect2.left = 2560
	screen.blit(building_surf,building_rect2)
		
	screen.blit(road_surf,(0,0))

	if game_active:
		
		score = display_score()
		
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		game_active = collision_sprite()
		
	else:
		score_message = title_font.render(f'Your score: {score}',False,'white')
		score_message_rect = score_message.get_rect(center = (640,330))
		screen.blit(game_name,game_name_rect)

		if score == 0: 
			screen.blit(game_message,game_message_rect)
			screen.blit(game_message2,game_message_rect2)
		else: screen.blit(score_message,score_message_rect)

	pygame.display.update()
	clock.tick(60)