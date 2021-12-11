class Num:
    def __set__(self, obj, value):
        if hasattr(value, "real"):
            obj._value = value.real
        else:
            obj._value = len(value)

    def __get__(self, obj, cls):
        if hasattr(obj, "_value"):
            return obj._value
        else:
            return 0


import sys
exec(sys.stdin.read())

