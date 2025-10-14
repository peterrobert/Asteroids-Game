import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from short import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # --- Groups ---
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shorts = pygame.sprite.Group()

    # --- player instance ---
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # --- Asteroid Group and instance ---
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    # --- Shot Group ---
    Shot.containers = (shorts, updatable, drawable)

    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return # Exit the program

        updatable.update(dt)
        for a in asteroids:
            for b in shorts:
                if a.collide(b):
                    a.split()
                    b.kill()

            if a.collide(player):
                print("Game over!")
                sys.exit()


        screen.fill("black")

        for i in drawable:
            i.draw(screen)
        
        # -- Refresh the display ---
        pygame.display.flip()
        time = clock.tick(60)
        dt = time / 1000  # Convert milliseconds to seconds
        



if __name__ == "__main__":
    main()
