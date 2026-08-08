import pygame

from drawtext import draw_text
from constants import SCREEN_WIDTH


class ScoreBoard(pygame.sprite.Sprite):

    containers: pygame.sprite.Group
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.text_font = pygame.font.SysFont("Arial", 50)
        self.score = 0

    def draw(self, screen):
        draw_text(screen, f"Score", self.text_font, (255,255,255), SCREEN_WIDTH - 160, 10)
        draw_text(screen, f"{self.score}", self.text_font, (255,255,255), SCREEN_WIDTH - 110, 70)
