import pygame
import math
class blue_object:
    def __init__(self, mass, x, y, vx, vy, color):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.time = pygame.time.get_ticks()



    def update(self):
        now = pygame.time.get_ticks()
        dt = (now - self.time) / 50
        self.time = now
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(math.log2(self.mass/math.pi)))
