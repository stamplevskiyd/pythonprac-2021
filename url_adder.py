"""'Simplest url adder. But it's enough for this task"""

import os

directories = ['20210916', '20210930', '20210923', '20211007', '20211014', '20211021',
               '20211028', '20211111', '20211118', '20211125', '20211202', '20211213']

people = ["https://github.com/Uberariy/pythonprac/tree/main/",
          "https://github.com/Veniamin-Arefev/pythonprac-2021/tree/main/",
          "https://git.cs.msu.ru/s02190141/pythonprac-2021/-/tree/main/"]
untesting_tasks = ['20211014/2']

tasks = [str(i) for i in range(1, 5)]
combinations = [dir + '/' + t for dir in directories for t in tasks]
for name in combinations:
    if name in untesting_tasks:
        continue
    if os.path.exists(name):
        with open(name + '/URLS', "wt") as f:
            for i in range(3):
                f.write(people[i] + name + '/tests\n')
                
