
from __future__ import annotations
from typing import List
from .board import Board
from .player import Player
class Game:  # pylint: disable=too-few-public-methods
    def __init__(self, player_x: Player, player_o: Player) -> None:
        self.board = Board()
        self._players: List[Player] = [player_x, player_o]
        self._current_idx = 0
    def switch_player(self) -> None:
        self._current_idx = 1 - self._current_idx
    def play(self) -> None:
        print("Welcome to Tic-Tac-Toe!")
        while True:
            print()
            print(self.board)
            current = self._players[self._current_idx]
            try:
                row, col = current.choose_move(self.board)
                self.board.place_mark(row, col, current.mark)
            except ValueError as exc:
                print(f"Invalid move: {exc}")
                continue
            won, mark = self.board.has_winner()
            if won:
                print()
                print(self.board)
                print(f"{current.name} ({mark}) wins!")
                break
            if self.board.is_full():
                print()
                print(self.board)
                print("Draw.")
                break
            self.switch_player()
