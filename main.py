import sys

import pygame  # pyright: ignore[reportMissingImports]

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from scoreboard import ScoreBoard
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    ScoreBoard.containers = (drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  # pyright: ignore[reportUnusedVariable]
    score_board = ScoreBoard()

    try:
        with open("high_score.txt", 'x') as f:
            f.write("1")
            print("writing new high score file")
    except FileExistsError:
        print("High score file already exists")

    with open("high_score.txt", "r") as f:
        high_score = f.read()
        score_board.high_score = int(high_score)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                if score_board.lives <= 0:
                    print("Game over!")
                    if int(score_board.score) >= int(score_board.high_score):
                        print("printing high score to file")
                        with open("high_score.txt", "w") as f:
                            f.write(f"{score_board.score}")
                            f.close()
                    sys.exit()
                else:
                    score_board.lives -= 1
                    player.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score_board.score += 10
                    score_board.high_score = max(score_board.high_score, score_board.score)
                    asteroid.split()
                    shot.kill()

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
