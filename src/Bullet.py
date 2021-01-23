import math, pygame

class Bullet:
    def __init__(self, pos, dir, image):
        self.pos = pos
        self.vel = [5 * math.cos(math.pi * (90 - dir) / 180), 5 * math.cos(math.pi * dir / 180)]
        self.image = pygame.transform.rotate(image, dir - 90)

    def tick(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def show(self, screen):
        screen.blit(self.image, self.pos)