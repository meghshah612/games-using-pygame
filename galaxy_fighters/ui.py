import pygame

import assets


def draw(ship1, ship2, ship1_bullets, ship2_bullets, ship1_health, ship2_health):
    assets.WIN.blit(assets.BG, (0, 0))

    ship1_health_text = assets.HEALTH_FONT.render(f"Health: {ship1_health}", 1, assets.WHITE)
    ship2_health_text = assets.HEALTH_FONT.render(f"Health: {ship2_health}", 1, assets.WHITE)
    assets.WIN.blit(ship1_health_text, (10, 10))
    assets.WIN.blit(ship2_health_text, (assets.WIDTH - ship2_health_text.get_width() - 10, 10))
    pygame.draw.rect(assets.WIN, assets.BLACK, assets.BORDER)
    assets.WIN.blit(assets.SHIP1, (ship1.x, ship1.y))
    assets.WIN.blit(assets.SHIP2, (ship2.x, ship2.y))

    for bullet in ship1_bullets:
        pygame.draw.rect(assets.WIN, assets.YELLOW, bullet)

    for bullet in ship2_bullets:
        pygame.draw.rect(assets.WIN, assets.YELLOW, bullet)

    pygame.display.update()


def draw_winner(text):
    winner_text = assets.WINNER_FONT.render(text, 1, assets.WHITE)
    assets.WIN.blit(winner_text, (assets.WIDTH/2 - winner_text.get_width()/2, assets.HEIGHT/2 - winner_text.get_height()/2))
    pygame.display.update()
    if assets.WIN_SOUND:
        assets.WIN_SOUND.play()
    pygame.time.delay(5000)


def handle_ship1_movement(keys, ship1):
    if keys[pygame.K_a] and ship1.x - assets.SHIP_VELOCITY >= 0:
        ship1.x -= assets.SHIP_VELOCITY
    elif keys[pygame.K_d] and ship1.x + assets.SHIP_VELOCITY + ship1.get_width() <= assets.BORDER.x:
        ship1.x += assets.SHIP_VELOCITY
    elif keys[pygame.K_w] and ship1.y - assets.SHIP_VELOCITY >= 0:
        ship1.y -= assets.SHIP_VELOCITY
    elif keys[pygame.K_s] and ship1.y + assets.SHIP_VELOCITY + ship1.get_height() <= assets.HEIGHT:
        ship1.y += assets.SHIP_VELOCITY


def handle_ship2_movement(keys, ship2):
    if keys[pygame.K_LEFT] and ship2.x - assets.SHIP_VELOCITY >= assets.BORDER.x + assets.BORDER.width:
        ship2.x -= assets.SHIP_VELOCITY
    elif keys[pygame.K_RIGHT] and ship2.x + assets.SHIP_VELOCITY + ship2.get_width() <= assets.WIDTH:
        ship2.x += assets.SHIP_VELOCITY
    elif keys[pygame.K_UP] and ship2.y - assets.SHIP_VELOCITY >= 0:
        ship2.y -= assets.SHIP_VELOCITY
    elif keys[pygame.K_DOWN] and ship2.y + assets.SHIP_VELOCITY + ship2.get_height() <= assets.HEIGHT:
        ship2.y += assets.SHIP_VELOCITY


def handle_bullets(ship1_bullets, ship2_bullets, ship1, ship2):

    for bullet in ship1_bullets[:]:
        bullet.x += assets.BULLET_VELOCITY
        if ship2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(assets.SHIP2_HIT))
            ship1_bullets.remove(bullet)

        elif bullet.x > assets.WIDTH:
            ship1_bullets.remove(bullet)

    for bullet in ship2_bullets[:]:
        bullet.x -= assets.BULLET_VELOCITY
        if ship1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(assets.SHIP1_HIT))
            ship2_bullets.remove(bullet)

        elif bullet.x < 0:
            ship2_bullets.remove(bullet)
