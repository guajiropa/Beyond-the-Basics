"""
This is an example of local funtions and enclosing functions, how python keeps
parent functions objects alive while executing the local function. It is a
dunder attribute defined as '__closure__'
"""
message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        # An example of the use of the keyword 'global'. Without
        # this keyword, the value of the global would remain the
        # same.
        #
        # global message
        #
        # The next example show how to access the enclosing functons
        # variable by the use of the keyword 'nonlocal'
        #
        nonlocal message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)


"""
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp
"""
