class Num:
    def __set__(self, obj, value):
        if hasattr(value, "real"):
            obj._value = value
        elif hasattr(value, "len"):
            obj._value = len(value)
        else:
            obj._value = "Nothing"

    def __get__(self, obj, cls):
        if hasattr(obj, "_value"):
            return obj._value
        else:
            return 0


class C:
    num = Num()

print(C().num)
c, d = C(), C()
c.num = d.num = 2
