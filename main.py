import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame, screen and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Add objects to groups
    Player.containers = (updatable, drawable)
    
    # Set player position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
    # Game event loop
    while True:
        log_state()
        
        for event in pygame.event.get():
            # Enable the quit icon
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        # Limit fps to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
