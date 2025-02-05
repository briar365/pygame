import pygame
from constants import *

def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock() 
    dt = 0
    while pygame.get_init():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        pygame.Surface.fill(screen, (0,0,1))
        pygame.display.flip()
        Clock.tick(60)
        dt = pygame.time.get_ticks()/1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()
