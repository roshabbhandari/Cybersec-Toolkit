# Architecture

Cybersec-Toolkit is organized around a small CLI layer and reusable defensive modules in `core/`.

- `main.py` handles menus and user interaction.
- `core/` contains security utilities.
- Each module should expose a focused API and return structured data where practical.
- New modules should avoid destructive actions and require explicit user input for local analysis.
