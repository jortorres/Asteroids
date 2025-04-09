# this allows us to use code from
# the open-source pygame library
# throughout this file
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

    Player.containers = (updateable, drawable)
    Asteroid.containers =(asteroid,updateable,drawable)
    AsteroidField.containers =(updateable,)

    player = Player(x,y)
    asteroid_field = AsteroidField()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) # fills screen with black
        updateable.update(dt)  # rotate player left or right

        for thing in drawable:
            thing.draw(screen) # draw triangle
        pygame.display.flip()
        dt = time.tick(60)/1000
       
        
if __name__ == "__main__":
    main()
