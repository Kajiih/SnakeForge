"""Some examples of tests."""

from time import sleep

import pytest


def test_simple():
    assert 1 + 1 == 2


@pytest.mark.skip("Reason why skipped")
def test_skipped():
    assert 1 + 1 == 2


@pytest.mark.xfail(reason="Reason why failed")
def test_xfailed():
    assert 1 + 1 == 3


@pytest.mark.slow("yeah")
def test_slow():
    sleep(1)
    assert 1 + 1 == 2


@pytest.mark.parametrize(("a", "b", "expected"), [(0, 0, 0), (-1, 1, 0), (3, 3, 6)])
def test_with_parameters(a: int, b: int, expected: int):
    assert a + b == expected
