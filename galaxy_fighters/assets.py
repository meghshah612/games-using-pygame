import os
import pygame

pygame.font.init()
try:
    pygame.mixer.init()
except Exception:
    pass

# Window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Background
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "space.png")), (WIDTH, HEIGHT)
)

# Fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Sounds (best-effort; mixer may not be available)
try:
    BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("assets", "Grenade+1.mp3"))
    BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("assets", "Gun+Silencer.mp3"))
    WIN_SOUND = pygame.mixer.Sound(os.path.join("assets", "win.mp3"))
except Exception:
    BULLET_HIT_SOUND = BULLET_FIRE_SOUND = WIN_SOUND = None

# Ship / bullet constants
SHIP_WIDTH, SHIP_HEIGHT = 50, 40
SHIP_VELOCITY = 5

BULLET_VELOCITY = 7
BULLET_WIDTH = 4
BULLET_HEIGHT = 2
MAX_BULLETS = 3

SHIP1_HIT = pygame.USEREVENT + 1
SHIP2_HIT = pygame.USEREVENT + 2

# Load images
SHIP1 = pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load(os.path.join("assets", "spaceship_red.png")), (SHIP_WIDTH, SHIP_HEIGHT)
    ),
    90,
)
SHIP2 = pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load(os.path.join("assets", "spaceship_yellow.png")), (SHIP_WIDTH, SHIP_HEIGHT)
    ),
    270,
)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
