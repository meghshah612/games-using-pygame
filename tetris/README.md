# Tetris

A refactored Tetris game using `pygame` with a modular package layout.

## Run the game

- `python -m tetris`
- `python main.py`

## Project structure

- `main.py` - lightweight entrypoint for backward compatibility
- `tetris/__init__.py` - package entrypoint
- `tetris/config.py` - game configuration and constants
- `tetris/pieces.py` - piece definitions, rotation logic, and shape generation
- `tetris/grid.py` - grid creation, collision checks, and row clearing
- `tetris/render.py` - rendering functions and screen drawing
- `tetris/score.py` - high-score persistence
- `tetris/game.py` - game loop and input handling
- `scores.txt` - persisted high score

## Notes

- The package now supports running with `python -m tetris`.
- High scores are stored in `scores.txt`.
- The code is split into separate modules for easier maintenance.
