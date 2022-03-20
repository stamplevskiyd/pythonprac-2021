import ast
import difflib
import sys
import re
import textdistance

def process(text: str) -> str:
    unified = ast.unparse(ast.parse(text))
    dump = ast.dump(ast.parse(unified), annotate_fields=False)
    process_list = re.findall(r"[A-Z]\w*\(|,|\)", dump)
    index = 0
    for i in range(len(process_list)):
        if process_list[i][0].isupper():
            process_list[i] = chr(index + ord('a'))  # таким образом заменим идентификаторы на уникальные
            index += 1

    return ''.join(process_list)


prog_1 = sys.argv[1]
prog_2 = sys.argv[2]
with open(prog_1, 'rt') as p:
    text_1 = p.read()
with open(prog_2, 'rt') as p:
    text_2 = p.read()

modified_1, modified_2 = process(text_1), process(text_2)
if (similarity := textdistance.damerau_levenshtein.normalized_distance(modified_1, modified_2)) <= 0.1:
    print(f"Plagiat is possible, similarity is {(1 - similarity) * 100} %")
    diff = difflib.HtmlDiff(tabsize=8, wrapcolumn=None, linejunk=None)
    html_diff = diff.make_file(ast.unparse(ast.parse(text_1)).split('\n'),
                               ast.unparse(ast.parse(text_2)).split('\n'),
                               prog_1, prog_2)
    with open(f"diff_{prog_1}_{prog_2}.html", 'w') as html:
        html.write(html_diff)
else:
    print(f"OK, similarity is {(1 - similarity) * 100} %")
