import ast
import difflib
import sys
import re

prog_1 = sys.argv[1]
prog_2 = sys.argv[2]

with open(prog_1, 'rt') as p1:
    text_1 = p1.read()
with open(prog_2, 'rt') as p2:
    text_2 = p2.read()


unified_1 = ast.unparse(ast.parse(text_1))
unified_2 = ast.unparse(ast.parse(text_2))

dump_1 = ast.dump(ast.parse(unified_1), annotate_fields=False)
dump_2 = ast.dump(ast.parse(unified_2), annotate_fields=False)
process_list = re.findall(r"[A-Z]\w*\(|,|\)|\[|]", dump_1)

index = 0
for i in range(len(process_list)):
    if process_list[i][0].isupper():
        process_list[i] = chr(index + ord('a'))  # таким образом заменим идентификаторы на уникальные
        index += 1

print(''.join(process_list))
