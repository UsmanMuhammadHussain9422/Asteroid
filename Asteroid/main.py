import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Exiting game.")
                return

        screen.fill((0, 0, 0))  # Clear the screen with black
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second

if __name__ == "__main__":
    main()
