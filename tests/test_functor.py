"""Test the functor module"""

from fmappy.functor import fmap
from itertools import chain
import pytest


def twice(x):
    return x * 2


SUPPORTED_TYPES = (
    (tuple, (tuple(), (1, 2, 3))),
    (dict, (dict(), dict(one=1, two=2, three=3))),
)


@pytest.mark.parametrize(
    ("type_", "value"),
    tuple((t, v) for t, values in SUPPORTED_TYPES for v in values),
)
def test_fmap_returns_same_type(type_, value):
    """When giving fmap an object, it returns an object of the same type."""
    assert isinstance(fmap(twice, value), type_)
