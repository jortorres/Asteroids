# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

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
    player = Player(x,y)



    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) # fills screen with black
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = time.tick(60)/1000
       
        
if __name__ == "__main__":
    main()
