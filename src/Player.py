import math, pygame

class Player():
    def __init__(self, pos, sprite, vel):
        self.pos = pos
        self.sprite = sprite
        self.angle = 0
        self.velm = vel
        self.velmh = vel / 2
        self.vel = [0, 0]

    def tick(self, keys):
        if((keys[0] - keys[1]) and (keys[2] - keys[3])):
            vel = self.velmh
        else:
            vel = self.velm

        self.vel[1] = (vel if keys[1] else 0) - (vel if keys[0] else 0)
        self.vel[0] = (vel if keys[3] else 0) - (vel if keys[2] else 0)

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def show(self, screen, mousepos):
        self.angle = (360 - math.atan2(mousepos[1] - (self.pos[1] + 50), mousepos[0] - (self.pos[0] + 75)) * 180 / math.pi +90) % 360
        print(self.angle)
        image = pygame.transform.rotate(self.sprite, self.angle)
        screen.blit(image, self.pos)
        