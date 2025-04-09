# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #init screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()  
    dt = 0
    
    #init player
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

   
    updateable = pygame.sprite.Group()  # creates group 1
    drawable = pygame.sprite.Group() # creates group 2
    asteroid = pygame.sprite.Group() # creates group 3
    shots = pygame.sprite.Group() # crates group 4

    Player.containers = (updateable, drawable)
    Asteroid.containers =(asteroid,updateable,drawable)
    AsteroidField.containers =(updateable,)
    Shot.containers = (updateable, drawable, shots)

    player = Player(x,y)
    asteroid_field = AsteroidField()

    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0)) # fills screen with black

        for entity in updateable:
            if isinstance(entity, Player):
                entity.update(dt, shots)
            else:
                entity.update(dt)

        for check in asteroid:
            if isinstance(check, CircleShape) and isinstance(player, CircleShape): # check to make sure both are instances
                if check.collisions(player):
                    running = False
                    print("Game Over")

        for hit_asteroid in asteroid:
            if isinstance(hit_asteroid, CircleShape ) and isinstance(player, CircleShape): # check to make sure both are instances
                for bullet in shots:
                    if hit_asteroid.collisions(bullet):
                        hit_asteroid.split()
                        bullet.kill()

        for thing in drawable:
            thing.draw(screen) # draw triangle
        
        pygame.display.flip()
        
        dt = time.tick(60)/1000
       
        
if __name__ == "__main__":
    main()
