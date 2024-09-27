from re import search


def string(value: str) -> bool:
    return not value.isdigit() and not only_specials(value)


def only_specials(value: str) -> bool:
    return not search(r"\w", value)
