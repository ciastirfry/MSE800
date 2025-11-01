# file: timed_decorator_demo.py
from functools import wraps
from time import sleep, perf_counter

"""
EXPLANATION (Week 14 – Execution-Time Decorator: What I Understand)

A decorator lets me wrap extra behavior around a function without changing the
function’s core logic. Here, I use a timing decorator to measure how long a
function runs. The decorator records the start time, calls the real function,
records the end time, and reports the elapsed duration. This approach keeps my
business logic (e.g., calculations, API calls) clean while centralizing cross-cutting
concerns (like timing, logging, caching, or authentication) in one place. I use
@wraps to preserve the original function’s name and docstring.

Why use a decorator here?
• Reusability: I can time any function just by adding @timeit.
• Separation of concerns: Timing logic stays separate from business code.
• Consistency: One implementation gives consistent measurement across the codebase.

When to use decorators:
• When I need common pre/post behavior for many functions (e.g., timing, logging,
  retry, caching, permission checks).
• When I want a clean, minimal function body and avoid copy-pasting the same
  boilerplate around multiple functions.
"""

def timeit(unit: str = "ms"):
    """
    Measure execution time of the decorated function.
    unit: "s" for seconds, "ms" for milliseconds, "us" for microseconds.
    """
    factor = {"s": 1.0, "ms": 1e3, "us": 1e6}.get(unit, 1e3)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed = (perf_counter() - start) * factor
                print(f"[timeit] {func.__name__} took {elapsed:.3f} {unit}")
        return wrapper
    return decorator


@timeit("ms")
def simulate_io(seconds: float) -> str:
    """Simulates an I/O-like wait using time.sleep."""
    sleep(seconds)
    return f"Slept for {seconds} second(s)."


@timeit("us")
def add(a: int, b: int) -> int:
    """A simple operation to show very fast timings."""
    return a + b


if __name__ == "__main__":
    print(simulate_io(0.3))  # uses time.sleep under the hood
    print(add(3, 5))
