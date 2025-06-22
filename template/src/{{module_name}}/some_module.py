"""Module description."""

from dataclasses import dataclass
from enum import Enum, auto

GLOBAL_VAR = 1


class Language(Enum):
    """Some description."""

    EN = auto()
    FR = auto()


def _private_function(language: Language) -> str:
    match language:
        case Language.EN:
            return "Hello"
        case Language.FR:
            return "Bonjour"


def public_function(name: str, n: int = GLOBAL_VAR, *, language: Language) -> str:
    """
    Greet name n times in a given language.

    The parameter types don't appear because there is no `Attributes` section.
    """
    greeting = _private_function(language)
    return f"{greeting} {name}" * n


class SomeClass:
    """
    Some description.

    Attributes:
        x: An attribute
    """

    def __init__(self, x: int):
        """
        Initialize SomeClass from some number.

        Parameters:
            x: Some number
        """
        # Attribute docstring has to be written in the class docstring unless
        # you use griffe-sphinx which is a paid feature
        self.x: int = x

    def some_method(self) -> int:
        """Return the value of the attribute x plus 1."""
        return 1 + self.x


@dataclass
class SomeDataClass:
    """
    Some description.

    Attributes:
        y: Description of y
        name: Description of name
        z: Description of z
    """

    y: int
    name: str
    z: int = 0
