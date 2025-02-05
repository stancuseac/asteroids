# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants, player
from constants import *
from player import*

def main ():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player = Player(x, y)
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000 # convert milliseconds to seconds

if __name__ == "__main__":
    main()