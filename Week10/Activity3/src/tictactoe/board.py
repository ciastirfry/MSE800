
from __future__ import annotations
from typing import List, Tuple
class Board:
    def __init__(self, size: int = 3) -> None:
        self.size = size
        self._grid: List[List[str]] = [[" " for _ in range(size)] for _ in range(size)]
    def get_cell(self, row: int, col: int) -> str:
        return self._grid[row][col]
    def is_empty(self, row: int, col: int) -> bool:
        return self._grid[row][col] == " "
    def place_mark(self, row: int, col: int, mark: str) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise ValueError("Row/Col out of range.")
        if not self.is_empty(row, col):
            raise ValueError("Cell already occupied.")
        if mark not in {"X", "O"}:
            raise ValueError("Mark must be 'X' or 'O'.")
        self._grid[row][col] = mark
    def is_full(self) -> bool:
        for r in range(self.size):
            for c in range(self.size):
                if self._grid[r][c] == " ":
                    return False
        return True
    def has_winner(self) -> Tuple[bool, str]:
        lines = []
        for i in range(self.size):
            lines.append(self._grid[i])
            lines.append([self._grid[r][i] for r in range(self.size)])
        lines.append([self._grid[i][i] for i in range(self.size)])
        lines.append([self._grid[i][self.size-1-i] for i in range(self.size)])
        for line in lines:
            if line[0] != " " and all(cell == line[0] for cell in line):
                return True, line[0]
        return False, ""
    def __str__(self) -> str:
        rows = []
        for r_idx, row in enumerate(self._grid):
            rows.append(" | ".join(row))
            if r_idx < self.size - 1:
                rows.append("--+---+--")
        return "\n".join(rows)
