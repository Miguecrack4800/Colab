import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

bck = (25, 25, 25)
run = True
mousepos = [0,0]
keys = [0, 0, 0, 0]
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

	screen.fill(bck)

	pygame.display.update()
