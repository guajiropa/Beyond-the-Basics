"""
    This file shows how important metadata can be lost when using
    decorators and wrappers and what you can do to preserve this
    metadata.
"""
import functools

# Please note that the parameter 'f' is th function that is decorated
# by the 'noop' function
def noop(f):
    @functools.wraps(f)  # This decorator will preserve thee metadata of the enclosed function
    def noop_wrapper():
        return f()

    """ Although this will work, it violates the
        ZEN of python as it is pretty ugly and there
        is a much better way to accomplish this,
        'functools.wraps()'
    """
    '''
    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    '''
    return noop_wrapper


@noop
def hello():
    """Prints a well known message"""
    print('Hello Python World')
