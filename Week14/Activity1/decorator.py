from functools import wraps

"""
EXPLANATION (Week 14 – Decorator):
A decorator is a higher-order function that takes a function, adds extra behavior
before/after it runs, and returns a new callable—without changing the original
function’s core logic. Here, @log_decorator wraps the target function with
'wrapper'. When 'add' is called, Python actually calls 'wrapper': it logs the
function name and the arguments, invokes the real function (via func(*args, **kwargs)),
captures the return value, logs it, and then returns it. Using @wraps preserves
the original function’s __name__ and docstring, which is important for debugging,
introspection, and tooling.
"""

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

if __name__ == "__main__":
    add(3, 5)
