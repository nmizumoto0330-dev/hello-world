def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    if not name:
        raise ValueError("Name must not be empty")
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    """Return a farewell message for the given name."""
    if not name:
        raise ValueError("Name must not be empty")
    return f"Goodbye, {name}!"
