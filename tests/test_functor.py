"""Test the functor module"""

from fmappy.functor import fmap


def twice(x):
    return x * 2


def test_fmap_tuple_yields_tuple():
    assert isinstance(fmap(twice, tuple()), tuple)
