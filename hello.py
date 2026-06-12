def greet(name: str, lang: str = "en") -> str:
    """Return a greeting message for the given name."""
    if not name:
        raise ValueError("Name must not be empty")
    if lang == "ja":
        return f"こんにちは、{name}！"
    return f"Hello, {name}!"


def farewell(name: str, lang: str = "en") -> str:
    """Return a farewell message for the given name."""
    if not name:
        raise ValueError("Name must not be empty")
    if lang == "ja":
        return f"さようなら、{name}！"
    return f"Goodbye, {name}!"
