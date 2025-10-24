import pygame
from constants import *
import circleshape
import random



class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):    

        self.kill()

        # if it's already the smallest size, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # choose a random angle between 20 and 50 degrees for the split
        random_angle = random.uniform(20, 50)

        # make two new velocity vectors rotated away from the original
        # (we assume self.velocity is a pygame.Vector2)
        v = pygame.Vector2(self.velocity)

        # If you want to be extra safe against zero-speed asteroids:
        # if v.length_squared() == 0:
        #     v = pygame.Vector2(0, 1)

        v1 = v.rotate( random_angle) * 1.2
        v2 = v.rotate(-random_angle) * 1.2

        # radius of the children
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # spawn the two new asteroids at the same position
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)

        # set their velocities
        child1.velocity = v1
        child2.velocity = v2
       