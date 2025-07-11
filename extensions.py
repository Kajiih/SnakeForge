"""Extensions for copier.yaml."""

from __future__ import annotations

import os
import re
import subprocess  # noqa: S404
import unicodedata
import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, LiteralString

from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2 import Environment


def _get_git_config(key: LiteralString) -> str:
    """Read a given key from local git config."""
    # Command is a LiteralString but is not detected by ruff: https://github.com/astral-sh/ruff/issues/18622
    command = f"/usr/bin/git config {key}"
    return subprocess.getoutput(command).strip()  # noqa: S605


def git_user_name(default: str) -> str:
    """Get the github username from local git config."""
    return _get_git_config("user.name") or default


def git_user_email(default: str) -> str:
    """Get the github user email from local git config."""
    return _get_git_config("user.email") or default


class GitConfigExtension(Extension):
    """Information from git config."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email


def slugify(value: str, separator: str = "-") -> str:
    """Slugify input given a separator."""
    value = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


class SlugifyExtension(Extension):
    """Slugify input."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["slugify"] = slugify


class CurrentYearExtension(Extension):
    """Current year."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.globals["CURRENT_YEAR"] = datetime.now(tz=UTC).year  # pyright: ignore[reportArgumentType]


def is_pascal_case(expression: str, /) -> bool:
    """Return true if the expression is in PascalCase."""
    pascal_case_regex = r"^[A-Z][a-z0-9]*(?:[A-Z][a-z0-9]*)*(?:[A-Z]?)$"
    return bool(re.match(pascal_case_regex, expression))


def is_snake_case(expression: str, /) -> bool:
    """Return true if the expression is in snake_case."""
    snake_case_regex = r"^[a-z]+(_[a-z]+)*$"
    return bool(re.match(snake_case_regex, expression))


def is_kebab_case(expression: str, /) -> bool:
    """Return true if the expression is in kebab-case."""
    snake_case_regex = r"^[a-z]+(-[a-z]+)*$"
    return bool(re.match(snake_case_regex, expression))


class CodingCaseExtension(Extension):
    """Coding case (snake_case, PascalCase, etc) validation filters."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["is_pascal_case"] = is_pascal_case  # pyright: ignore[reportArgumentType]
        environment.filters["is_snake_case"] = is_snake_case  # pyright: ignore[reportArgumentType]
        environment.filters["is_kebab_case"] = is_kebab_case  # pyright: ignore[reportArgumentType]


def is_valid_email(value: str) -> bool:
    """Basic email address validation."""
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value))


class EmailValidationExtension(Extension):
    """Email address validation filter."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["is_valid_email"] = is_valid_email  # pyright: ignore[reportArgumentType]


def is_valid_package_name(name: str) -> bool:
    """Return true if then name is a valid python package name.

    Based on: https://packaging.python.org/en/latest/specifications/name-normalization/
    """
    pattern = r"^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$"
    return re.match(pattern, name, re.IGNORECASE) is not None


def normalize_package_name(name: str) -> str:
    """
    Normalize the name python package name.

    Based on: https://packaging.python.org/en/latest/specifications/name-normalization/#name-normalization,
    but also replaces spaces.
    """
    return re.sub(r"[-_.]+", "-", name).lower()


def is_normalized_package_name(name: str) -> bool:
    """Return true if then name is a normalized python package name.

    Based on: https://packaging.python.org/en/latest/specifications/name-normalization/
    """
    return is_valid_package_name(name) and name == normalize_package_name(name)


class PackageNameExtension(Extension):
    """Valid and normalized package name filters."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["is_normalized_package_name"] = is_normalized_package_name  # pyright: ignore[reportArgumentType]


def version_to_tuple(version: str) -> tuple[int, ...]:
    """Convert version string to tuple of ints."""
    return tuple(int(part) for part in version.split("."))


def version_higher_than(version1: str, version2: str) -> bool:
    """Return True if version1 > version2."""
    return version_to_tuple(version1) >= version_to_tuple(version2)


def version_between(version: str, version_min: str, version_max: str) -> bool:
    """Return True if version_min <= version <= version_max."""
    v = version_to_tuple(version)
    return version_to_tuple(version_min) <= v <= version_to_tuple(version_max)


class SemverExtension(Extension):
    """Semver filters."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["version_higher_than"] = version_higher_than  # pyright: ignore[reportArgumentType]
        environment.filters["version_between"] = version_between  # pyright: ignore[reportArgumentType]


def is_uuid(value: str) -> bool:
    """Check if value is a valid UUID string."""
    try:
        _ = uuid.UUID(value)
        return True  # noqa: TRY300
    except (ValueError, TypeError):
        return False


class UUIDExtension(Extension):
    """UUID validation filter."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["is_uuid"] = is_uuid  # pyright: ignore[reportArgumentType]


class EnvExtension(Extension):
    """Expose environment variables to Jinja context."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.globals["env"] = os.environ  # pyright: ignore[reportArgumentType]
