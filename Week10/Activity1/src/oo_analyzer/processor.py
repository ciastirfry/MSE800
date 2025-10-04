
from __future__ import annotations
from typing import Dict, Iterable, List
from .inputs import InputData
from .analyzers import Analyzer

class Processor:
    """Coordinates analyzers and aggregates their results."""
    def __init__(self, analyzers: Iterable[Analyzer]) -> None:
        self._analyzers: List[Analyzer] = list(analyzers)

    def run(self, input_data: InputData) -> Dict[str, int]:
        result: Dict[str, int] = {}
        for analyzer in self._analyzers:
            result.update(analyzer.analyze(input_data))
        return result
