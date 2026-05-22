"""Main game loop for Pong."""
import pygame

import constants
from paddle import Paddle
from ball import Ball
from render import draw
from physics import handle_collision, handle_paddle_movement


def main():
    """Run the Pong game."""

    pygame.init()
    window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Pong")

    score_font = pygame.font.SysFont("comicsans", 50)

    clock = pygame.time.Clock()

    left_paddle = Paddle(10, constants.HEIGHT // 2 - constants.PADDLE_HEIGHT // 2, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
    right_paddle = Paddle(constants.WIDTH - 10 - constants.PADDLE_WIDTH, constants.HEIGHT // 2 - constants.PADDLE_HEIGHT // 2, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)
    ball = Ball(constants.WIDTH // 2, constants.HEIGHT // 2, constants.BALL_RADIUS)

    left_score = 0
    right_score = 0

    running = True
    while running:
        clock.tick(constants.FPS)
        draw(window, [left_paddle, right_paddle], ball, left_score, right_score, score_font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        pressed = pygame.key.get_pressed()
        keys = {
            "w": pressed[pygame.K_w],
            "s": pressed[pygame.K_s],
            "up": pressed[pygame.K_UP],
            "down": pressed[pygame.K_DOWN],
        }

        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > constants.WIDTH:
            left_score += 1
            ball.reset()

        winner_text = None
        if left_score >= constants.WINNING_SCORE:
            winner_text = f"Left Player Won! {left_score} - {right_score}"
        elif right_score >= constants.WINNING_SCORE:
            winner_text = f"Right Player Won! {left_score} - {right_score}"

        if winner_text:
            text = score_font.render(winner_text, 1, constants.WHITE)
            window.blit(text, (constants.WIDTH // 2 - text.get_width() // 2, constants.HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == "__main__":
    main()
