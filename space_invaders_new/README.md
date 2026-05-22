# Space Invaders (New)

This project is a refactored Pygame Space Invaders clone with separate modules for game logic, entities, resources, and settings.

## Run the game

- Directly from the repository: `python main.py`

## Project structure

- `main.py` - application entrypoint
- `game.py` - main game loop and screen management
- `entities.py` - player, enemy, and bullet classes
- `resources.py` - asset loading helpers
- `settings.py` - shared configuration values and asset names
- `README.md` - project documentation

## Notes

Keep the asset files (`background.png`, `ufo.png`, `player.png`, `enemy.png`, `bullet.png`, `background.wav`, `laser.wav`, `explosion.wav`) in the same folder as the Python files so the game can load them correctly.
