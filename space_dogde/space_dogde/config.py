from pathlib import Path
import pygame

pygame.font.init()

BASE_DIR = Path(__file__).resolve().parent.parent
WIDTH = 900
HEIGHT = 700
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 4
STAR_WIDTH = 15
STAR_HEIGHT = 15
STAR_VELOCITY = 2
STAR_COUNT = 3

FONT = pygame.font.SysFont("comicsans", 30)
BG = pygame.transform.scale(
    pygame.image.load(str(BASE_DIR / "bg.jpeg")), (WIDTH, HEIGHT)
)
