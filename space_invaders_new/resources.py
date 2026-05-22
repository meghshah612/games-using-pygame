from pathlib import Path
import pygame
from settings import ASSETS_DIR


def load_image(filename: str) -> pygame.Surface:
    return pygame.image.load(str(ASSETS_DIR / filename))


def load_sound(filename: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(str(ASSETS_DIR / filename))


def load_music(filename: str) -> None:
    pygame.mixer.music.load(str(ASSETS_DIR / filename))
