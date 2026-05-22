from pathlib import Path

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_ENEMIES = 6
PLAYER_START_X = 370
PLAYER_START_Y = 480
BULLET_SPEED = 10
ENEMY_SPEED = 4
ENEMY_DROP = 40
SCORE_FONT_SIZE = 32
OVER_FONT_SIZE = 64
WHITE = (255, 255, 255)

ASSETS_DIR = Path(__file__).resolve().parent
BACKGROUND_IMAGE = "background.png"
ICON_IMAGE = "ufo.png"
PLAYER_IMAGE = "player.png"
ENEMY_IMAGE = "enemy.png"
BULLET_IMAGE = "bullet.png"
LASER_SOUND = "laser.wav"
EXPLOSION_SOUND = "explosion.wav"
MUSIC_FILE = "background.wav"
