
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
    """Counts uppercase letters A–Z across the input."""
    def analyze(self, data: InputData) -> Dict[str, int]:
        upper = 0
        for chunk in data.as_list():
            upper += sum(1 for ch in chunk if ch.isalpha() and ch == ch.upper() and ch != ch.lower())
        return {"uppercase_chars": upper}

class DigitAnalyzer(Analyzer):
    """Counts 0–9 digits across the input."""
    def analyze(self, data: InputData) -> Dict[str, int]:
        count = 0
        for chunk in data.as_list():
            count += sum(1 for ch in chunk if ch.isdigit())
        return {"digits": count}

class SpecialCharAnalyzer(Analyzer):
    """Counts special (non-alphanumeric, non-whitespace) characters across the input."""
    def analyze(self, data: InputData) -> Dict[str, int]:
        special = 0
        for chunk in data.as_list():
            special += sum(1 for ch in chunk if (not ch.isalnum()) and (not ch.isspace()))
        return {"special_chars": special}
