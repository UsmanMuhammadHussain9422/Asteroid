import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius=5):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)