
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple
from .board import Board
class Player(ABC):  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark
    @abstractmethod
    def choose_move(self, board: Board) -> Tuple[int, int]:
        ...
class HumanPlayer(Player):  # pylint: disable=too-few-public-methods
    def choose_move(self, board: Board) -> Tuple[int, int]:
        while True:
            raw = input(f"{self.name} ({self.mark}) 'row col' 1-3 1-3: ").strip()
            parts = raw.split()
            if len(parts) != 2 or not all(p.isdigit() for p in parts):
                print("Invalid format. e.g., '2 3'")
                continue
            row, col = int(parts[0]) - 1, int(parts[1]) - 1
            if not (0 <= row < board.size and 0 <= col < board.size):
                print("Out of range (1..3).")
                continue
            if not board.is_empty(row, col):
                print("Cell occupied.")
                continue
            return row, col
