import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # --- player instance ---
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return # Exit the program

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        time = clock.tick(60)
        dt = time / 1000  # Convert milliseconds to seconds
       



if __name__ == "__main__":
    main()
