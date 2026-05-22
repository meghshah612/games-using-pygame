import pygame
from .config import BG, FONT, WIDTH, HEIGHT


def draw(window: pygame.Surface, player: pygame.Rect, elapsed: float, stars: list[pygame.Rect]) -> None:
    window.blit(BG, (0, 0))
    score_text = FONT.render(f"Score: {round(elapsed * 10)}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.draw.rect(window, (255, 255, 255), player)
    for star in stars:
        pygame.draw.rect(window, (255, 255, 0), star)

    pygame.display.update()
