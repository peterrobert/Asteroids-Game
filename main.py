import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return # Exit the program
                
        screen.fill("black")
        pygame.display.flip()



if __name__ == "__main__":
    main()
