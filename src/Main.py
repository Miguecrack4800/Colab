import pygame, math
from Player import Player
from Bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((1280, 720))

bck = (25, 25, 25)
run = True
mousepos = [0,0]
md = 0
lastmd = 0
keys = [0, 0, 0, 0]
image = pygame.image.load("sprites\\tanqueA1.png")
bullet = pygame.image.load("sprites\\bullet.png")
p = Player([0,0], image, 1)
objects = []

while run:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False
		if(event.type == pygame.MOUSEMOTION):
			mousepos = event.pos
		if(event.type == pygame.KEYDOWN):
			if(event.key == 119):
				keys[0] = 1
			elif(event.key == 115):
				keys[1] = 1
			elif(event.key == 97):
				keys[2] = 1
			elif(event.key == 100):
				keys[3] = 1
		if(event.type == pygame.KEYUP):
			if(event.key == 119):
				keys[0] = 0
			elif(event.key == 115):
				keys[1] = 0
			elif(event.key == 97):
				keys[2] = 0
			elif(event.key == 100):
				keys[3] = 0
		if(event.type == pygame.MOUSEBUTTONDOWN):
			if(event.button == 1):
				md = 1
		if(event.type == pygame.MOUSEBUTTONUP):
			if(event.button == 1):
				md = 0
				lastmd = 0

	screen.fill(bck)

	p.tick(keys)
	p.show(screen, mousepos)

	if(md and not lastmd):
		b = Bullet([p.pos[0] + 75, p.pos[1] + 50], p.angle, bullet)
		objects.append(b)
		lastmd = 1

	nobjects = objects
	for x in objects:
		x.tick()
		x.show(screen)
		if(x.pos[0] < -100 or x.pos[0] > 1380 or x.pos[1] < -100 or x.pos[1] > 820):
			nobjects.remove(x)
	objects = nobjects

	pygame.display.update()
