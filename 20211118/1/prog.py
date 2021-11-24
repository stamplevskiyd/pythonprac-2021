def objcount(cls):
    class New(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            New.counter += 1

        def __del__(self):
            if hasattr(super(), "__del__"):
                super().__del__()
            New.counter -= 1
    return New

import sys
exec(sys.stdin.read())
