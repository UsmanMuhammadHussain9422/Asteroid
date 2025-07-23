import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock()
    dt = 0
    running = True
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add player to the sprite groups
    Player.containers = (updatable, drawable)    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Exiting game.")
                return
            
        updatable.update(dt)  # Update the player's state

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                running = False
                return
            
            for shot in shots:
                    if shot.check_collision(asteroid):
                        print("Asteroid hit!")
                        asteroid.kill()

        screen.fill((0, 0, 0))  # Clear the screen with black

        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000 # Limit to 60 frames per second

if __name__ == "__main__":
    main()
