from typing import Callable
import time


def with_retry(attempts: int, delay: float = 0.1):
    def wrapper(fn: Callable) -> Callable:
        def wrapped(*args, **kwargs):
            last_error = None
            for i in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    print(f"[Retry] Attempt {i+1} failed: {e}")
                    last_error = e
                    time.sleep(delay)
            raise last_error  # type: ignore

        return wrapped

    return wrapper


def flaky_action(counter: dict) -> str:
    if counter["value"] < 2:
        counter["value"] += 1
        raise ValueError("Simulated failure")
    return "Success after retries"


def run_hof_retry():
    print("\n-- HOF: Retry Wrapper --")
    counter = {"value": 0}
    retryable = with_retry(3)(lambda: flaky_action(counter))
    result = retryable()
    print(f"Result: {result}")


def flaky_wrapper(counter: dict) -> str:
    return flaky_action(counter)


def run_hof_retry_origin():
    print("\n-- HOF: Retry Wrapper --")
    counter = {"value": 0}
    retryable = with_retry(3)(flaky_wrapper)
    result = retryable()
    print(f"Result: {result}")
