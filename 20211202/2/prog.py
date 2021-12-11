class check(type):
    def __init__(self, name, parents, ns):
        def check_annotations(self):
            res = True
            for elem in self.__annotations__.keys():
                if not hasattr(self, elem) or not isinstance(getattr(self, elem), self.__annotations__[elem]):
                    res = False
            return res
        setattr(self, "check_annotations", check_annotations)
        super().__init__(name, parents, ns)


import sys
exec(sys.stdin.read())
