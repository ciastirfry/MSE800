
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple
from .board import Board
from .timed_input import TimedInput
class Player(ABC):  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark
    @abstractmethod
    def choose_move(self, board: Board) -> Tuple[int, int] | None:
        ...
class HumanPlayer(Player):  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, mark: str, seconds: int = 10) -> None:
        super().__init__(name, mark)
        self._timer = TimedInput(seconds)
    def choose_move(self, board: Board) -> Tuple[int, int] | None:
        while True:
            raw = self._timer.get(f"{self.name} ({self.mark}) 'row col' (1-3 1-3): ")
            if raw is None:
                print(f"Time's up for {self.name}! Turn skipped.")
                return None
            parts = raw.strip().split()
            if len(parts) != 2 or not all(p.isdigit() for p in parts):
                print("Invalid format. e.g., '2 3'")
                continue
            r, c = int(parts[0]) - 1, int(parts[1]) - 1
            if not (0 <= r < board.size and 0 <= c < board.size):
                print("Out of range (1..3).")
                continue
            if not board.is_empty(r, c):
                print("Cell occupied.")
                continue
            return r, c
