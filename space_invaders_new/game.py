import math
import random

import pygame
from pygame import mixer

from entities import Bullet, Enemy, Player
from resources import load_image, load_music, load_sound
from settings import (
    BACKGROUND_IMAGE,
    BULLET_IMAGE,
    ENEMY_IMAGE,
    ICON_IMAGE,
    EXPLOSION_SOUND,
    LASER_SOUND,
    MUSIC_FILE,
    PLAYER_IMAGE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WHITE,
    NUM_ENEMIES,
    OVER_FONT_SIZE,
    SCORE_FONT_SIZE,
)


class SpaceInvadersGame:
    def __init__(self) -> None:
        pygame.init()
        mixer.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = load_image(BACKGROUND_IMAGE)

        self.player = Player(load_image(PLAYER_IMAGE))
        self.enemies = self._create_enemies()
        self.bullet = Bullet(load_image(BULLET_IMAGE))

        load_music(MUSIC_FILE)
        mixer.music.play(-1)

        self.laser_sound = load_sound(LASER_SOUND)
        self.explosion_sound = load_sound(EXPLOSION_SOUND)

        pygame.display.set_caption("Space Invader")
        pygame.display.set_icon(load_image(ICON_IMAGE))

        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", SCORE_FONT_SIZE)
        self.over_font = pygame.font.Font("freesansbold.ttf", OVER_FONT_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

    def _create_enemies(self):
        enemy_image = load_image(ENEMY_IMAGE)
        return [
            Enemy(
                enemy_image,
                random.randint(0, SCREEN_WIDTH - enemy_image.get_width()),
                random.randint(50, 150),
            )
            for _ in range(NUM_ENEMIES)
        ]

    def run(self) -> None:
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif event.key == pygame.K_SPACE and not self.bullet.active():
                    self.laser_sound.play()
                    self.bullet.fire(self.player.x)
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.player.stop()

    def _update(self) -> None:
        if self.game_over:
            return

        self.player.update()
        self.bullet.update()

        for enemy in self.enemies:
            if enemy.y > 440:
                self.game_over = True
                break

            enemy.update()

            if self._is_collision(enemy, self.bullet):
                self.explosion_sound.play()
                self.score += 1
                self.bullet.reset()
                enemy.reset(
                    random.randint(0, SCREEN_WIDTH - enemy.image.get_width()),
                    random.randint(50, 150),
                )

    def _draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        self.bullet.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        self._draw_score()

        if self.game_over:
            self._draw_game_over()

        pygame.display.update()

    def _draw_score(self) -> None:
        score_surface = self.font.render(f"Score : {self.score}", True, WHITE)
        self.screen.blit(score_surface, (10, 10))

    def _draw_game_over(self) -> None:
        over_surface = self.over_font.render("GAME OVER", True, WHITE)
        self.screen.blit(over_surface, (200, 250))

    def _is_collision(self, enemy: Enemy, bullet: Bullet) -> bool:
        if not bullet.active():
            return False
        distance = math.hypot(enemy.x - bullet.x, enemy.y - bullet.y)
        return distance < 27
