# Space Dodge

A simple Pygame dodge game where the player avoids falling stars while the difficulty increases over time.

## Project structure

- `main.py` - direct runner for the package
- `space_dogde/config.py` - game constants and assets
- `space_dogde/render.py` - drawing and display update logic
- `space_dogde/game.py` - gameplay loop and input handling
- `space_dogde/__main__.py` - package entrypoint for `python -m space_dogde`
- `bg.jpeg` - background image asset required by the game

## Setup

1. Install dependencies:

```powershell
python -m pip install pygame
```

2. Ensure `bg.jpeg` is present in the project root.

## Run

- Directly:

```powershell
python main.py
```

- As a package:

```powershell
python -m space_dogde
```

## Notes

- The game increases star spawn rate, star speed, and player speed over time.
- Player movement is limited to the left and right edges of the window.
