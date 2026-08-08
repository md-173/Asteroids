import pygame

from drawtext import draw_text
from constants import SCREEN_WIDTH

# TODO: Move the score, high-score, lives into player class

class ScoreBoard(pygame.sprite.Sprite):

    containers: pygame.sprite.Group
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.text_font = pygame.font.SysFont("Arial", 50)
        self.score = 0
        self.high_score = 0
        self.lives = 3

    def draw(self, screen):
        # Draw current game score
        draw_text(screen, f"Score", self.text_font, (255,255,255), SCREEN_WIDTH - 160, 10)
        draw_text(screen, f"{self.score}", self.text_font, (255,255,255), SCREEN_WIDTH - 110, 70)

        # Draw High Score
        draw_text(screen, f"High Score", self.text_font, (255,255,255), 30, 10)
        draw_text(screen, f"{self.high_score}", self.text_font, (255,255,255), 110, 70)

        # Draw Lives
        draw_text(screen, f"Lives: {self.lives}", self.text_font, (255,255,255), SCREEN_WIDTH / 2, 10)
