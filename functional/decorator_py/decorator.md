# Decorators

A **decorator** is a function that takes another function and extends or alters its behavior *without modifying the original function’s code*.

- Leverage closures to wrap behavior
- Accept and return callables
- Are widely used for logging, authorization, caching, timing, validation, etc.
  
## What i can do
- Cleanly wrap behavior without duplicating logic
- ADd reusable fetures(logging, validation, retries)
- Keep businees login separated from cross-cutting concerns

## Anti-pattern to avoid
### Manually adding logging to each function
```python
def compute_square(x: int) -> int:
    print(f"Computing square of {x}")
    result = x * x
    print(f"Result is {result}")
    return result
```
- Violates DRY
- Duplicates log logic across functions
- Mixing business logic and side-effects
  
### Solution
```python
@log_execution
def compute_square(x: int) -> int:
    return x * x
```
- Logs behavior without touching core logic
- Reuseable on any function
- Easy to layer with other decorators