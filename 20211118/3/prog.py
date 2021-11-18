import string
print(string.ascii_lowercase)

class Alpha:
    __slots__ = list(string.ascii_lowercase)

    def __init__(self, **kwargs):
    #использовать для этого setattr. Или нет
