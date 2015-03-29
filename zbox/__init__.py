version = __version__ = '1.1.0'

try:
    import cytoolz as toolz
    import cytoolz.curried
except ImportError:
    import toolz
    import toolz.curried
