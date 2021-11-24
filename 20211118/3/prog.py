import string

class Alpha:
    __slots__ = list(string.ascii_lowercase)

    def __init__(self, **kwargs):
        for i, j in kwargs.items():
            setattr(self, i, j)

    def __str__(self):
        data = ''
        for letter in string.ascii_lowercase:
            if hasattr(self, letter):
                data += letter + ': ' + str(getattr(self, letter, None)) + ', '
        return data[:-2]

class AlphaQ:
    #далее не успел. Alpha - рабочий

alp = Alpha(c=10, z=2, a=42)
alp.e = 123
print(alp)
