from string import ascii_lowercase

class Empty:
    pass

class Alpha:
    __slots__ = list(ascii_lowercase)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        data = ''
        for letter in string.ascii_lowercase:
            if hasattr(self, letter):
                data += letter + ': ' + str(getattr(self, letter, None)) + ', '
        return data[:-2]

class AlphaQ(Empty):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in string.ascii_lowercase:
                setattr(self, key, value)
            else:
                raise AttributeError

    def __str__(self):  # same as in Alpha
        data = ''
        for letter in ascii_lowercase:
            if hasattr(self, letter):
                data += letter + ': ' + str(getattr(self, letter, None)) + ', '
        return data[:-2]

    def __setattr__(self, key, value):
        if key in ascii_lowercase:
            super().__setattr__(key, value)
        else:
            raise AttributeError


import sys
exec(sys.stdin.read())
