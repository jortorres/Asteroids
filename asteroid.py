from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        groups = self.groups()  # get all groups instances
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50) # get random angle
        vector_1 = pygame.math.Vector2.rotate(self.velocity, random_angle) #set vector 1
        vector_2 = pygame.math.Vector2.rotate(self.velocity, -random_angle) # set vector 2
        new_radius = self.radius - ASTEROID_MIN_RADIUS # new size
        asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius) #create new 
        asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius) # create new 2
        asteroid_1.velocity = vector_1 * 1.2 
        asteroid_2.velocity = vector_2 * 1.2

        for group in groups: # add new asteroids to groups
            group.add(asteroid_1,asteroid_2)




        
            
