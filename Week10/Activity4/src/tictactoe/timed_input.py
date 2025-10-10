
from __future__ import annotations
import sys
import threading
import time
from queue import Queue, Empty

class TimedInput:  # pylint: disable=too-few-public-methods
    def __init__(self, seconds: int = 10) -> None:
        self.seconds = seconds
    def get(self, prompt: str) -> str | None:
        q: Queue[str] = Queue()
        def reader() -> None:
            try:
                text = input(prompt)
                q.put(text)
            except EOFError:
                q.put("")
        t = threading.Thread(target=reader, daemon=True)
        t.start()
        for remaining in range(self.seconds, 0, -1):
            try:
                return q.get_nowait()
            except Empty:
                pass
            if remaining <= 5:
                print(f"{remaining} seconds left...", file=sys.stderr)
            time.sleep(1)
        try:
            return q.get_nowait()
        except Empty:
            return None
