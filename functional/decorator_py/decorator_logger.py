from typing import Callable
import time


def log_execution(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with {args} {kwargs}")
        start = time.time()
        result = func(*args, **kwargs)
        duration = (time.time() - start) * 1000
        print(f"[LOG] {func.__name__} returned {result} in {duration: .2f}ms")
        return result

    return wrapper


@log_execution
def compute_square(x: int, y: int) -> int:
    return x * x + y


def run_decorator_logger():
    print("\n-- Decorator: Logging --")
    compute_square(5, 1)
    compute_square(12, 1)
    compute_square_org = log_execution(compute_square)
    compute_square_org(3, 1)
