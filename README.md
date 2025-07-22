# Python Handbook

This handbook documents core Python backend patterns and production-minded code structures using:

- Functional programming (closures, decorators, HOFs, etc.)
- OOP design (composition, strategy, factory)
- Clean code principles (modularity, typing, testing)
- Public libraries (Flask, SQLAlchemy, Pydantic, etc.)

---

## Topics

### [Functional Programming](./functional/functional.md)

- `first_class_functions/` — Inject behavior, strategy-like usage
- `closures/` — Local state management without globals
- `decorators/` — Wrap function behavior cleanly
- `hof_wrappers/` — Build reusable higher-order tools
- `partial_functions/` — Pre-bind args using `functools.partial`
- `function_pipelines/` — Compose processing stages with functional chaining

---

### Object-Oriented Patterns 

- `composition_vs_inheritance/` — Practical preference guide
- `strategy_pattern/` — Swap behavior at runtime
- `factory_pattern/` — Deferred instantiation
- `plugin_loader/` — Dynamic registry-based injection
- `dunder_methods/` — Write Pythonic classes

---

### Clean Code Practices

- `naming_conventions/`
- `typing_and_static_analysis/`
- `separation_of_concerns/`
- `refactor_patterns/`
- `docstrings_and_docs/`

---

### Public Library Usage

- `flask/` — REST APIs, middleware, blueprints
- `sqlalchemy/` — ORM vs Core, sessions, joins
- `pydantic/` — Typed models, validation
- `typer/` — CLI applications
- `pytest/` — Unit, integration, fixture best practices
- `rich/` — CLI formatting and logs
- `fastapi/` — Web API with typing and DI

---

### AsyncIO

- `task_groups/`
- `timeouts_and_cancellation/`
- `async_queues/`
- `producer_consumer/`

---
