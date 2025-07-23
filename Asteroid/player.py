from shot import Shot
from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.time_since_last_shot = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.time_since_last_shot -= dt

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):            
        if self.time_since_last_shot > 0:
            return
        self.time_since_last_shot = PLAYER_SHOOT_COOLDOWN
        tip = self.triangle()[0]
        shot = Shot(tip.x, tip.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED