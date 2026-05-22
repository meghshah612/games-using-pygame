import pygame

from .config import TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT, BLOCK_SIZE


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, True, color)
    surface.blit(
        label,
        (
            TOP_LEFT_X + PLAY_WIDTH / 2 - label.get_width() / 2,
            TOP_LEFT_Y + PLAY_HEIGHT / 2 - label.get_height() / 2,
        ),
    )


def draw_grid(surface, grid):
    sx = TOP_LEFT_X
    sy = TOP_LEFT_Y

    for i in range(len(grid)):
        pygame.draw.line(
            surface,
            (128, 128, 128),
            (sx, sy + i * BLOCK_SIZE),
            (sx + PLAY_WIDTH, sy + i * BLOCK_SIZE),
        )
        for j in range(len(grid[i])):
            pygame.draw.line(
                surface,
                (128, 128, 128),
                (sx + j * BLOCK_SIZE, sy),
                (sx + j * BLOCK_SIZE, sy + PLAY_HEIGHT),
            )


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", True, (255, 255, 255))

    sx = TOP_LEFT_X + PLAY_WIDTH + 50
    sy = TOP_LEFT_Y + PLAY_HEIGHT / 2 - 100
    shape_format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(shape_format):
        for j, column in enumerate(line):
            if column == '0':
                pygame.draw.rect(
                    surface,
                    shape.color,
                    (sx + j * BLOCK_SIZE, sy + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0,
                )

    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface, grid, score=0, last_score=0):
    surface.fill((0, 0, 0))

    title_font = pygame.font.SysFont("comicsans", 60)
    title_label = title_font.render("Tetris", True, (255, 255, 255))
    surface.blit(
        title_label,
        (
            TOP_LEFT_X + PLAY_WIDTH / 2 - title_label.get_width() / 2,
            30,
        ),
    )

    score_font = pygame.font.SysFont("comicsans", 30)
    score_label = score_font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_label = score_font.render(f"High Score: {last_score}", True, (255, 255, 255))

    sx = TOP_LEFT_X + PLAY_WIDTH + 50
    sy = TOP_LEFT_Y + PLAY_HEIGHT / 2 - 100
    surface.blit(score_label, (sx + 20, sy + 160))

    sx = TOP_LEFT_X - 200
    sy = TOP_LEFT_Y + 200
    surface.blit(high_score_label, (sx + 20, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                surface,
                grid[i][j],
                (
                    TOP_LEFT_X + j * BLOCK_SIZE,
                    TOP_LEFT_Y + i * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                ),
                0,
            )

    pygame.draw.rect(
        surface,
        (255, 0, 0),
        (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT),
        5,
    )

    draw_grid(surface, grid)
