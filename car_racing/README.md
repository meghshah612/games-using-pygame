# Car Racing

This folder contains a simple Pygame car racing demo.

How to run

- From the workspace root run:

```bash
python -m car_racing
```

- Or run directly:

```bash
python car_racing/main.py
```

Files

- `main.py` - game entrypoint that wires modules
- `assets.py` - images, masks and constants
- `entities.py` - game model classes (`GameInfo`, `PlayerCar`, `ComputerCar`)
- `ui.py` - drawing, input handling and collision helpers
- `utils.py` - small helper functions for image blitting/scaling
- `imgs/` - image assets

Notes

- This refactor reorganized the code into modules for readability and reuse; game behavior was kept unchanged.
- If you encounter issues loading fonts or audio, ensure pygame is installed and your environment supports display output.
