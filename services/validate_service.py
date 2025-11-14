from exceptions.custom_exceptions import TooShortError


def validate_length(text: str) -> str:
    if len(text) < 3:
        raise TooShortError("Text is too short")
    return text
