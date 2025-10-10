
from __future__ import annotations
from .player import HumanPlayer
from .game import Game
def _choose_symbol() -> tuple[str, str]:
    while True:
        pick = input("Player 1: choose your symbol (X/O): ").strip().upper()
        if pick in {"X", "O"}:
            return (pick, "O" if pick == "X" else "X")
        print("Please type X or O.")
def main() -> None:
    print("Tic-Tac-Toe (OOP) — Symbol selection + 10s timer")
    name1 = input("Enter Player 1 name: ").strip() or "Player 1"
    name2 = input("Enter Player 2 name: ").strip() or "Player 2"
    s1, s2 = _choose_symbol()
    print(f"{name1} is {s1}; {name2} is {s2}.")
    game = Game(HumanPlayer(name1, s1, seconds=10), HumanPlayer(name2, s2, seconds=10))
    game.play()
if __name__ == "__main__":
    main()
