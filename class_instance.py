class Foo(object):

    def __init__(self):
        print('foo __init__')
        return None

    def __tmp__(self):
        print('__tmp__')

    def __del__(self):
        print('foo __del__')

foo = Foo()
