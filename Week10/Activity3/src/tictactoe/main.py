
from __future__ import annotations
from .player import HumanPlayer
from .game import Game
def main() -> None:
    print("Tic-Tac-Toe (OOP) — Week 10 Activity 3")
    name_x = input("Enter Player X name: ").strip() or "Player X"
    name_o = input("Enter Player O name: ").strip() or "Player O"
    game = Game(HumanPlayer(name_x, "X"), HumanPlayer(name_o, "O"))
    game.play()
if __name__ == "__main__":
    main()
