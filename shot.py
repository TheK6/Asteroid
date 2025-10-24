import pygame
from constants import *
import circleshape  

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, velocity: pygame.Vector2):
        super().__init__(x, y, SHOT_RADIUS)
        # make sure to copy so we don't hold a reference that might mutate elsewhere
        self.velocity = pygame.Vector2(velocity)

    def update(self, dt: float):
        # move straight each frame
        self.position += self.velocity * dt

        # simple cleanup: remove when off-screen (prevents memory leaks)
        if (
            self.position.x < -self.radius or
            self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or
            self.position.y > SCREEN_HEIGHT + self.radius
        ):
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
