import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #initialize pygame
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #create the widnow
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    dt = 0
    running = True

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    # make Player auto-add itself to these groups in its __init__ via self.add(*self.containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # create player after setting containers
    x = int(SCREEN_WIDTH / 2)
    y = int(SCREEN_HEIGHT / 2)
    player = Player(x, y)

    field = AsteroidField()
    
    # game loop 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # update all updatables
        updatable.update(dt)

        # collision check: player vs asteroids 
        for a in asteroids:
            if player.collides_with(a):
                print("Game over!")
                pygame.quit()
                sys.exit()

        # collision check for player shot vs asteroid 
        for a in list(asteroids):
            for s in list(shots):
                if a.collides_with(s):
                    a.split()
                    s.kill()
                    break

        # fill the screen black and draw frame
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

    pygame.quit()

if __name__ == "__main__":
    main()
