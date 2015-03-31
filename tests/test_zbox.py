import types

import pytest

try:
    import cytoolz as toolz
except ImportError:
    HAVE_CYTOOLZ = False
else:
    HAVE_CYTOOLZ = True

try:
    import toolz
except ImportError:
    pass


@pytest.mark.skipif(not HAVE_CYTOOLZ, reason='requires cytoolz')
def test_get_cytoolz():
    from zbox import toolz as tz
    assert tz is toolz
    assert tz.curried is toolz.curried


@pytest.mark.skipif(HAVE_CYTOOLZ, reason='testing no cytoolz')
def test_get_toolz():
    from zbox import toolz as tz
    assert tz is toolz
    assert tz.curried is toolz.curried


def test_gen():
    from zbox import gen
    c = toolz.concat([[1], [2], [3]])
    g = gen(c)
    assert not isinstance(c, types.GeneratorType)
    assert isinstance(g, types.GeneratorType)
    assert list(g) == list(toolz.concat([[1], [2], [3]]))
