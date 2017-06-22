"""
 More on using 'global' amd 'nonlocal' objects with local
 functions.
"""
import time

def make_timer():
    """
        A function to return the elapsed time between function calls
    """
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()

        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed




