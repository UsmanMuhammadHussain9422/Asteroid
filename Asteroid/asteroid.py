import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Remove the current asteroid
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Calculate the new radius for the split asteroids
        new_radius = self.radius // 2
        random_angle = random.uniform(20, 50)
        a1_v = self.velocity.rotate(random_angle)
        a2_v = self.velocity.rotate(-random_angle)

        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = a1_v * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = a2_v * 1.2