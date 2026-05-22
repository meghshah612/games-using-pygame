import random
import time

import pygame

from .config import *
from .render import draw


WINDOW_TITLE = "Space Dodge"


def create_window() -> pygame.Surface:
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    return window


def create_player() -> pygame.Rect:
    return pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_HEIGHT, STAR_WIDTH * 2 + 10, PLAYER_HEIGHT)


def spawn_stars(stars: list[pygame.Rect], count: int) -> None:
    for _ in range(count):
        star_x = random.randint(0, WIDTH - STAR_WIDTH)
        stars.append(pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT))


def constrain_player(player: pygame.Rect) -> None:
    if player.x < 0:
        player.x = 0
    elif player.x > WIDTH - PLAYER_WIDTH:
        player.x = WIDTH - PLAYER_WIDTH

    if player.y < 0:
        player.y = 0
    elif player.y > HEIGHT - PLAYER_HEIGHT:
        player.y = HEIGHT - PLAYER_HEIGHT


def update_stars(stars: list[pygame.Rect], player: pygame.Rect, star_velocity: int) -> bool:
    for star in stars[:]:
        star.y += star_velocity
        if star.y > HEIGHT:
            stars.remove(star)
        elif star.colliderect(player):
            stars.remove(star)
            return True
    return False


def calculate_difficulty(elapsed: float) -> tuple[int, int, int]:
    count = STAR_COUNT + min(round(elapsed / 10), 17)
    star_velocity = STAR_VELOCITY + min(round(elapsed / 10), 8)
    player_velocity = PLAYER_VELOCITY + min(round(elapsed / 10), 11)
    return count, star_velocity, player_velocity


def show_game_over(window: pygame.Surface) -> None:
    lost_text = FONT.render("Game Over!", True, (255, 0, 0))
    window.blit(
        lost_text,
        ((WIDTH - lost_text.get_width()) / 2, (HEIGHT - lost_text.get_height()) / 2),
    )
    pygame.display.update()
    pygame.time.delay(4000)


def main() -> None:
    pygame.init()
    window = create_window()
    player = create_player()
    clock = pygame.time.Clock()

    start_time = time.time()
    star_timer = 0
    star_add_interval = 2000
    stars: list[pygame.Rect] = []

    running = True
    while running:
        delta_ms = clock.tick(60)
        star_timer += delta_ms
        elapsed = time.time() - start_time

        count, star_velocity, player_velocity = calculate_difficulty(elapsed)

        if star_timer > star_add_interval:
            spawn_stars(stars, count)
            star_add_interval = max(800, star_add_interval - 50)
            star_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_velocity
        elif keys[pygame.K_RIGHT]:
            player.x += player_velocity

        constrain_player(player)

        if update_stars(stars, player, star_velocity):
            show_game_over(window)
            break

        draw(window, player, elapsed, stars)

    pygame.quit()
