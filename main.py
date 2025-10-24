import pygame
from constants import *
import player 
import asteroid
import asteroidfield
import shot
import circleshape

def main():

    updatable   =   pygame.sprite.Group()
    drawable    =   pygame.sprite.Group()
    asteroids   =   pygame.sprite.Group()
    shots       =   pygame.sprite.Group()

    player.Player.containers                = (updatable, drawable)
    asteroid.Asteroid.containers            = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers  = (updatable,)
    shot.Shot.containers                    = (updatable, drawable, shots) 


    player_one = player.Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    asteroid_field_o = asteroidfield.AsteroidField()

    clock = pygame.time.Clock()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    

        for rock in asteroids:
            if player_one.check_collisions(rock):
                print("Game over!")
                pygame.quit()
                raise SystemExit
            
        for rock in list(asteroids):
            for bullet in list(shots):
                if bullet.check_collisions(rock):
                    bullet.kill()
                    rock.split()
                    break  
        


        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
