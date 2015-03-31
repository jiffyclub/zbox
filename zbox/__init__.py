version = __version__ = '1.1.0dev'

try:
    import cytoolz as toolz
    import cytoolz.curried
except ImportError:
    import toolz
    import toolz.curried


def gen(i):
    """
    Convert any iterable into a generator object.

    """
    return (x for x in i)
