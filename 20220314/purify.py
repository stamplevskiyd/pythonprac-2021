import ast
import sys

prog_name = sys.argv[1]
text = open(prog_name).read()
print(ast.unparse(ast.parse(text)))
