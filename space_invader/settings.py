import os
import pygame

pygame.font.init()

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

WIDTH = 750
HEIGHT = 750
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

MAIN_FONT = pygame.font.SysFont("comicsans", 50)
LOST_FONT = pygame.font.SysFont("comicsans", 60)


def load_image(filename):
    return pygame.image.load(os.path.join(ASSETS_DIR, filename))


RED_SPACE_SHIP = load_image("pixel_ship_red_small.png")
GREEN_SPACE_SHIP = load_image("pixel_ship_green_small.png")
BLUE_SPACE_SHIP = load_image("pixel_ship_blue_small.png")

YELLOW_SPACE_SHIP = load_image("pixel_ship_yellow.png")

RED_LASER = load_image("pixel_laser_red.png")
GREEN_LASER = load_image("pixel_laser_green.png")
BLUE_LASER = load_image("pixel_laser_blue.png")
YELLOW_LASER = load_image("pixel_laser_yellow.png")

BG = pygame.transform.scale(load_image("background-black.png"), (WIDTH, HEIGHT))
