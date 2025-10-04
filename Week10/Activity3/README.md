
# Week 10 - Activity 3: Tic‑Tac‑Toe (OOP) — Readability & Maintainability

## What’s inside
- `design/class-diagram.puml` — class relationships (Board, Player, HumanPlayer, Game)
- `design/sequence-main-turn.puml` — main turn interaction flow
- `src/tictactoe/board.py` — board state, winner/draw checks, safe `place_mark`
- `src/tictactoe/player.py` — abstract `Player`, `HumanPlayer` with robust input handling
- `src/tictactoe/game.py` — orchestrates the loop, validates moves, prints results
- `src/tictactoe/main.py` — CLI entrypoint
- `.pylintrc` — tuned for 100‑char lines and practical docstring rules
- `README.md` — run/test/Pylint instructions

## Run the game (CLI)
```bash
python -m tictactoe.main
```
- Enter moves as `row col` using 1..3 (e.g., `2 3`).
- Invalid inputs are explained and re‑prompted.
- It announces winner or draw and shows the board each turn.

## Manual testing checklist (as required)
- Try non‑numeric input (e.g., `a b`), out‑of‑range (e.g., `0 4`), and occupied cells.
- Quick‑win scenarios: first row/column/diagonals.
- Full‑board draw: fill nine moves without a three‑in‑a‑row.

## Code quality (Pylint)
```bash
pip install pylint
pylint src/tictactoe --fail-under=9.5
```
**Project follows:**
- Encapsulation (Board internals via methods)
- Single‑responsibility (Game orchestrates; Board validates & evaluates)
- Clear, small methods; type hints and docstrings; guard clauses
