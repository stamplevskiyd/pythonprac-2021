class D:
    def __get__(self, obj, cls):
        print("get")
        return obj._val
    def __set__(self, obj, value):
        print("set")
        obj._val = value
        return
    def __delete__(self, obj):
        obj._val = None
        print("delete")

class C:
    d = D()
    
    
