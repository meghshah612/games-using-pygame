import random
import pygame

import settings
from entities import Enemy, Player
from utils import collide


def main():
    run = True
    level = 0
    lives = 5

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        settings.WIN.blit(settings.BG, (0, 0))

        lives_label = settings.MAIN_FONT.render(f"Lives: {lives}", 1, settings.WHITE)
        level_label = settings.MAIN_FONT.render(f"Level: {level}", 1, settings.WHITE)

        settings.WIN.blit(lives_label, (10, 10))
        settings.WIN.blit(level_label, (settings.WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(settings.WIN)

        player.draw(settings.WIN)

        if lost:
            lost_label = settings.LOST_FONT.render("You Lost!!", 1, settings.WHITE)
            settings.WIN.blit(
                lost_label,
                (settings.WIDTH / 2 - lost_label.get_width() / 2, 350),
            )

        pygame.display.update()

    while run:
        clock.tick(settings.FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > settings.FPS * 3:
                run = False
            continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5

            for _ in range(wave_length):
                enemy = Enemy(
                    random.randrange(50, settings.WIDTH - 100),
                    random.randrange(-1500, -100),
                    random.choice(["red", "blue", "green"]),
                )
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < settings.WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < settings.HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > settings.HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

    pygame.quit()


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True

    while run:
        settings.WIN.blit(settings.BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin...", 1, settings.WHITE)
        settings.WIN.blit(
            title_label,
            (settings.WIDTH / 2 - title_label.get_width() / 2, 350),
        )
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()
