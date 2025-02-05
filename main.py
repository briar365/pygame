import pygame
from constants import *
from circleshape import *
from player import *

def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock() 
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while pygame.get_init():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        player.update(dt)
        dt = Clock.tick(60)/1000
    
if __name__ == "__main__":
    main()
