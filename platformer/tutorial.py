import pygame

import assets

pygame.display.set_caption("Platformer")
window = pygame.display.set_mode((assets.WIDTH, assets.HEIGHT))


import entities
import ui

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = assets.get_background("Blue.png")

    block_size = 96

    player = entities.Player(100, 100, 50, 50)
    fire = entities.Fire(100, assets.HEIGHT - block_size - 64, 16, 32)
    fire.on()
    floor = [entities.Block(i * block_size, assets.HEIGHT - block_size, block_size)
             for i in range(-assets.WIDTH // block_size, (assets.WIDTH * 2) // block_size)]
    objects = [*floor, entities.Block(0, assets.HEIGHT - block_size * 2, block_size),
               entities.Block(block_size * 3, assets.HEIGHT - block_size * 4, block_size), fire]

    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(assets.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(assets.FPS)
        fire.loop()
        ui.handle_move(player, objects)
        ui.draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= assets.WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
