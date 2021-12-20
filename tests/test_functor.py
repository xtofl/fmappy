"""Test the functor module"""

from fmappy.functor import fmap
from itertools import chain
import pytest
from unittest.mock import MagicMock


def twice(x):
    return x * 2


SUPPORTED_TYPES = (
    (tuple, (tuple(), (1, 2, 3))),
    (dict, (dict(), dict(one=1, two=2, three=3))),
    (list, ([], [1, 2, 3])),
    (int, (1, 2, 3)),
    (str, ("", "ab", "abc")),
)


@pytest.mark.parametrize(
    ("type_", "value"),
    tuple((t, v) for t, values in SUPPORTED_TYPES for v in values),
)
def test_fmap_returns_same_type(type_, value):
    """When giving fmap an object, it returns an object of the same type."""
    assert isinstance(fmap(twice, value), type_)


def test_raises_when_functor_type_is_unknown():
    class X:
        pass

    with pytest.raises(TypeError):
        fmap(twice, X())


@pytest.mark.parametrize(
    ("function", "data", "result"),
    (
        (twice, 1, 2),
        (twice, "ab", "abab"),
        (twice, tuple(), tuple()),
        (twice, (1, 2, 3), (2, 4, 6)),
        (twice, dict(), dict()),
        (twice, dict(a=1, b=2, c=3), dict(a=2, b=4, c=6)),
        (twice, [], []),
        (twice, [1, 2], [2, 4]),
    ),
)
def test_fmap_applies_the_function(data, function, result):
    assert fmap(function, data) == result



def test_none_is_not_an_optional():
    """fmap(f, None) has to forward its argument to f"""
    spy = MagicMock()
    fmap(spy, None)
    spy.assert_called_with(None)
