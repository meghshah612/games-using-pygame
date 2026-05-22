import pygame
import time
import random
import math
from ui import *
from utils import *
from assets import *

# Import package modules if available; fall back to local imports when run as script
try:
    from . import assets, entities, ui
except Exception:
    import assets
    import entities
    import ui

pygame.font.init()

WIDTH, HEIGHT = assets.WIDTH, assets.HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")


class GameInfo:
    LEVELS = 2

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)


class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel/2
        self.move()


class ComputerCar(AbstractCar):
    IMG = GREEN_CAR
    START_POS = (150, 200)

    def __init__(self, max_vel, rotation_vel, path=[]):
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)

    def draw(self, win):
        super().draw(win)
        # self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        super().move()

    def next_level(self, level):
        self.reset()
        self.vel = self.max_vel + (level - 1) * 0.2
        self.current_point = 0



def main():
    # instantiate entities
    player_car = entities.PlayerCar(4, 4)
    computer_car = entities.ComputerCar(2, 4, assets.PATH)
    game_info = entities.GameInfo()

    clock = pygame.time.Clock()
    run = True
    images = assets.IMAGES

    while run:
        clock.tick(assets.FPS)

        ui.draw(WIN, images, player_car, computer_car, game_info)

        while not game_info.started:
            try:
                blit = None
                # use utils helper if available
                try:
                    from .utils import blit_text_center as _btc
                except Exception:
                    from utils import blit_text_center as _btc
                _btc(WIN, assets.MAIN_FONT, f"Press any key to start level {game_info.level}!")
            except Exception:
                # fallback
                WIN.fill((0, 0, 0))
                pygame.display.update()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    game_info.start_level()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        ui.move_player(player_car)
        computer_car.move()

        ui.handle_collision(WIN, player_car, computer_car, game_info)

        if game_info.game_finished():
            try:
                from .utils import blit_text_center as _btc2
            except Exception:
                from utils import blit_text_center as _btc2
            _btc2(WIN, assets.MAIN_FONT, "You won the game!")
            pygame.display.update()
            pygame.time.wait(5000)
            game_info.reset()
            player_car.reset()
            computer_car.reset()


if __name__ == "__main__":
    main()


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
          (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
player_car = PlayerCar(4, 4)
computer_car = ComputerCar(2, 4, PATH)
game_info = GameInfo()

while run:
    clock.tick(FPS)

    draw(WIN, images, player_car, computer_car, game_info)

    while not game_info.started:
        blit_text_center(
            WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                game_info.start_level()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)
    computer_car.move()

    handle_collision(player_car, computer_car, game_info)

    if game_info.game_finished():
        blit_text_center(WIN, MAIN_FONT, "You won the game!")
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()


pygame.quit()
