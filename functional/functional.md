# First-Class functions

## Definition
In Python, functions are *first-class citizens*, meaning they can be:
- Assigned to variables
- Passed as arguments to other functions
- Returned from functions
- Stored in data structures

## What I can do

- Replace conditional logic with passed-in behaviors
- Write more reusable, testable, and composable functions
- Begin composing higher-order functions or decorators
- Inject dependencies without complex class hierarchies

## Anti-patterns to avoid

```python
def notify(name, method):
    if method == "email":
        return f"Email to {name}"
    elif method == "slack":
        return f"Slack to{name}"
    else:
        return f"Unkown for {name}"
```
- Tight coupling to method names
- Harder to extend(must modify the function for each new case)
- Difficult to test independently
- Violates Open/Closed Principle
  
### To This
```python
def notify(name: str, formatter: Callable[[str], str]) -> str:
    return formatter(name)
```
- Easy to reuse and test
- Open to extension: you can add a new formatter without changing notify
- Aligns with Python's functional capabilities
- Encourages separation of concerns and behavioral injection