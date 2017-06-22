"""
    This is an exercise in using function decorators. Please note that
     the function executes and then returns to the decorator before
     returning to the code that called it. Also note tha functions are
     not the only objects that can be decorators.
"""
# Setup the function to use as a decorator
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

# Now to use the decorator function
@escape_unicode
def northern_city():
    return 'Tromsø'
