import pytest

try:
    import cytoolz
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
    assert tz is cytoolz
    assert tz.curried is cytoolz.curried


@pytest.mark.skipif(HAVE_CYTOOLZ, reason='testing no cytoolz')
def test_get_toolz():
    from zbox import toolz as tz
    assert tz is toolz
    assert tz.curried is toolz.curried
