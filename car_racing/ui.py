import pygame

try:
    from . import assets
    from .utils import blit_rotate_center, blit_text_center
except Exception:
    import assets
    from utils import blit_rotate_center, blit_text_center


def draw(win, images, player_car, computer_car, game_info):
    for img, pos in images:
        win.blit(img, pos)

    level_text = assets.MAIN_FONT.render(
        f"Level {game_info.level}", 1, (255, 255, 255))
    win.blit(level_text, (10, assets.HEIGHT - level_text.get_height() - 70))

    time_text = assets.MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    win.blit(time_text, (10, assets.HEIGHT - time_text.get_height() - 40))

    vel_text = assets.MAIN_FONT.render(
        f"Vel: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, assets.HEIGHT - vel_text.get_height() - 10))

    player_car.draw(win, blit_rotate_center)
    computer_car.draw(win, blit_rotate_center)
    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()


def handle_collision(win, player_car, computer_car, game_info):
    # bounce off track border
    if player_car.collide(assets.TRACK_BORDER_MASK) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(
        assets.FINISH_MASK, *assets.FINISH_POSITION)
    if computer_finish_poi_collide != None:
        blit_text_center(win, assets.MAIN_FONT, "You lost!")
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(
        assets.FINISH_MASK, *assets.FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            game_info.next_level()
            player_car.reset()
            computer_car.next_level(game_info.level)
