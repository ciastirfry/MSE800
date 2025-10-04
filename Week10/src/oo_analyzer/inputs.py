
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence, Union, List

StringOrList = Union[str, Sequence[str]]

@dataclass(frozen=True)
class InputData:
    """Wrapper that normalizes input as either a string or a list of strings."""
    raw: StringOrList

    def is_string(self) -> bool:
        return isinstance(self.raw, str)

    def as_list(self) -> List[str]:
        """Return a list of strings for analysis.

        - If input is a string, returns [string].
        - If input is a sequence, ensures all items are strings.
        """
        if isinstance(self.raw, str):
            return [self.raw]
        if isinstance(self.raw, Sequence):
            for item in self.raw:
                if not isinstance(item, str):
                    raise TypeError("All items in the list must be strings.")
            return list(self.raw)
        raise TypeError("Input must be a string or a sequence of strings.")
