from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
import os

class Asteroid(CircleShape):
    asteroid_img = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Optionally resize image based on radius
        scale = int(radius * 2)  # diameter

        if Asteroid.asteroid_img is None:
            Asteroid.asteroid_img = pygame.image.load(os.path.join("assets", "asteroid.png")).convert_alpha()        
        self.image = pygame.transform.scale(Asteroid.asteroid_img, (scale, scale))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        self.rect.center = (self.position.x, self.position.y)
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        groups = self.groups()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        vector_2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector_1 * 1.2
        asteroid_2.velocity = vector_2 * 1.2

        for group in groups:
            group.add(asteroid_1, asteroid_2)

