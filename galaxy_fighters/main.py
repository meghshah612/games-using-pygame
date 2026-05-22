import pygame
import time
import random

# Import package modules if available; fall back to local imports when run as script
try:
    from . import assets, entities, ui
except Exception:
    import assets
    import entities
    import ui


def main():
    # rectangles used for player positions (same layout as original)
    ship1 = pygame.Rect(0, (assets.HEIGHT - assets.SHIP1.get_height()) / 2, assets.SHIP_WIDTH, assets.SHIP_HEIGHT)
    ship2 = pygame.Rect(assets.WIDTH - assets.SHIP2.get_width(), (assets.HEIGHT - assets.SHIP2.get_height()) / 2, assets.SHIP_WIDTH, assets.SHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    ship1_bullets = []
    ship2_bullets = []
    ship1_health = 10
    ship2_health = 10

    while run:
        clock.tick(assets.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(ship1_bullets) < assets.MAX_BULLETS:
                    bullet = pygame.Rect(ship1.x + ship1.width, ship1.y + ((ship1.height - assets.BULLET_HEIGHT) / 2), assets.BULLET_WIDTH, assets.BULLET_HEIGHT)
                    ship1_bullets.append(bullet)
                    if assets.BULLET_FIRE_SOUND:
                        assets.BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(ship2_bullets) < assets.MAX_BULLETS:
                    bullet = pygame.Rect(ship2.x - assets.BULLET_WIDTH, ship2.y + ((ship2.height - assets.BULLET_HEIGHT) / 2), assets.BULLET_WIDTH, assets.BULLET_HEIGHT)
                    ship2_bullets.append(bullet)
                    if assets.BULLET_FIRE_SOUND:
                        assets.BULLET_FIRE_SOUND.play()

            if event.type == assets.SHIP1_HIT:
                ship1_health -= 1
                if assets.BULLET_HIT_SOUND:
                    assets.BULLET_HIT_SOUND.play()

            if event.type == assets.SHIP2_HIT:
                ship2_health -= 1
                if assets.BULLET_HIT_SOUND:
                    assets.BULLET_HIT_SOUND.play()

        winner_text = ""
        if ship1_health <= 0:
            winner_text = "Player 2 Won!"
        elif ship2_health <= 0:
            winner_text = "Player 1 Won!"

        if winner_text:
            ui.draw_winner(winner_text)
            break

        keys = pygame.key.get_pressed()
        ui.handle_ship1_movement(keys, ship1)
        ui.handle_ship2_movement(keys, ship2)

        ui.handle_bullets(ship1_bullets, ship2_bullets, ship1, ship2)

        ui.draw(ship1, ship2, ship1_bullets, ship2_bullets, ship1_health, ship2_health)

    pygame.quit()


if __name__ == "__main__":
    main()
