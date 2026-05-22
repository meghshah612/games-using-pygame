import pygame

from .config import SCREEN_WIDTH, SCREEN_HEIGHT
from .grid import check_lost, clear_rows, create_grid, valid_space
from .pieces import convert_shape_format, get_shape
from .render import draw_next_shape, draw_text_middle, draw_window
from .score import max_score, update_score


def main(win):
    last_score = max_score()
    locked_positions = {}
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()

    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0
    change_piece = False
    run = True

    while run:
        grid = create_grid(locked_positions)
        delta_time = clock.get_rawtime()
        fall_time += delta_time
        level_time += delta_time
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
            else:
                change_piece = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)

        for x, y in shape_pos:
            if y > -1:
                grid[y][x] = current_piece.color

        if 'change_piece' in locals() and change_piece:
            for pos in shape_pos:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            score += clear_rows(grid, locked_positions) * 10
            change_piece = False

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(list(locked_positions)):
            draw_text_middle(win, "YOU LOST!", 80, (255, 255, 255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)


def main_menu(win):
    run = True

    while run:
        win.fill((0, 0, 0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255, 255, 255))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()


def run():
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    main_menu(win)
