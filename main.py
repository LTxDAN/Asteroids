import pygame
from constants import *

def main():
    #initialize pygame
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #create the widnow
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill the screen black
        screen.fill((0, 0, 0))
        # refresh display
        pygame.display.flip()


if __name__ == "__main__":
    main()
