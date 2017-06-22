"""
    In this example we will apply multiple decorators to one
    function. Be cautious with your use of decorators though,
    as naively placed decorators may lose important metadata.
"""


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


class Trace:

    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()


@tracer
@escape_unicode
def norwegian_island_maker(name):
    # Function will return to closest decorator
    # which will return it to the next in line
    # all the way to the top of the chain
    return name + 'øy'
