# Functional python


## Function Pipelines

A **function pipeline** is a sequence of functions where the output of one function becomes the input to the next.  
It’s often used to build clean, modular processing flows — especially for strings, requests, or data transformations.

### Anti-patterns to avoid
```python
def clean(text: str) -> str:
    return add_prefix(to_lowercase(strip_spaces(text)))
```
- Hard to test intermediate stages
- Cannot dynamically add/remove stages
- Not composable or extensible
```python
pipeline = make_pipeline([strip_spaces, to_lowercase, add_prefix])
```
- Easy to compose and modify
- Clear structure and order
- Resembles real middleware or ETL pipelines