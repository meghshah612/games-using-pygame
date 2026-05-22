"""Rendering helpers for Pong."""
import constants


def draw(win, paddles, ball, left_score, right_score, score_font):
    """Draw the game state to the provided surface."""

    win.fill(constants.BLACK)

    left_score_text = score_font.render(f"{left_score}", 1, constants.WHITE)
    right_score_text = score_font.render(f"{right_score}", 1, constants.WHITE)
    win.blit(left_score_text, (constants.WIDTH // 4 - left_score_text.get_width() // 2, 20))
    win.blit(
        right_score_text,
        (constants.WIDTH * (3 / 4) - right_score_text.get_width() // 2, 20),
    )

    for paddle in paddles:
        paddle.draw(win)

    dash_height = constants.HEIGHT // 20
    for i in range(10, constants.HEIGHT, dash_height):
        if i % 2 == 1:
            continue
        pygame_rect = (constants.WIDTH // 2 - 5, i, 10, dash_height)
        # draw center divider
        win.fill(constants.WHITE, pygame_rect)

    ball.draw(win)
    import pygame

    pygame.display.update()
