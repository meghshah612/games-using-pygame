from pygame import Surface

from settings import BULLET_SPEED, ENEMY_SPEED, ENEMY_DROP, PLAYER_START_X, PLAYER_START_Y, SCREEN_WIDTH


class Player:
    def __init__(self, image: Surface) -> None:
        self.image = image
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.x_change = 0

    def move_left(self) -> None:
        self.x_change = -5

    def move_right(self) -> None:
        self.x_change = 5

    def stop(self) -> None:
        self.x_change = 0

    def update(self) -> None:
        self.x += self.x_change
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.image.get_width()))

    def draw(self, surface: Surface) -> None:
        surface.blit(self.image, (self.x, self.y))


class Enemy:
    def __init__(self, image: Surface, x: int, y: int) -> None:
        self.image = image
        self.x = x
        self.y = y
        self.x_change = ENEMY_SPEED
        self.y_change = ENEMY_DROP

    def update(self) -> None:
        self.x += self.x_change
        if self.x <= 0:
            self.x_change = ENEMY_SPEED
            self.y += self.y_change
        elif self.x >= SCREEN_WIDTH - self.image.get_width():
            self.x_change = -ENEMY_SPEED
            self.y += self.y_change

    def reset(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.x_change = ENEMY_SPEED

    def draw(self, surface: Surface) -> None:
        surface.blit(self.image, (self.x, self.y))


class Bullet:
    def __init__(self, image: Surface) -> None:
        self.image = image
        self.x = 0
        self.y = PLAYER_START_Y
        self.y_change = BULLET_SPEED
        self.state = "ready"

    def fire(self, x: int) -> None:
        if self.state == "ready":
            self.x = x
            self.state = "fire"

    def reset(self) -> None:
        self.y = PLAYER_START_Y
        self.state = "ready"

    def update(self) -> None:
        if self.state == "fire":
            self.y -= self.y_change
            if self.y <= 0:
                self.reset()

    def draw(self, surface: Surface) -> None:
        if self.state == "fire":
            surface.blit(self.image, (self.x + 16, self.y + 10))

    def active(self) -> bool:
        return self.state == "fire"
