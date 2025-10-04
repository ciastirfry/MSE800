
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
from .inputs import InputData

class Analyzer(ABC):
    """Abstract base class for analyzers."""

    @abstractmethod
    def analyze(self, data: InputData) -> Dict[str, int]:
        """Return a dictionary of metrics."""

class LengthAnalyzer(Analyzer):
    """Computes total length.
    - For string: number of characters.
    - For list: number of items.
    """
    def analyze(self, data: InputData) -> Dict[str, int]:
        if data.is_string():
            total_length = len(data.as_list()[0])
        else:
            total_length = len(data.as_list())
        return {"total_length": total_length}

class UppercaseAnalyzer(Analyzer):
    """Counts uppercase A–Z characters across the input."""
    def analyze(self, data: InputData) -> Dict[str, int]:
        upper = 0
        for chunk in data.as_list():
            upper += sum(1 for ch in chunk if ch.isalpha() and ch == ch.upper() and ch != ch.lower())
        return {"uppercase_chars": upper}
