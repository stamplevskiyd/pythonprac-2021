import sys
import zlib

branch_name = sys.argv[1]
branch_file = '.git/refs/heads/' + branch_name
with open(branch_file) as file:
    branch_code = file.read()
commit_path = '.git/objects/' + branch_code[:2] + '/' + branch_code[2:]
with open(commit_path[:-1], 'rb') as objfile:
    fullobj = zlib.decompress(objfile.read())
    header, _, body = fullobj.partition(b'\x00')
    info_text = body.decode()
    tree_code = info_text.split()[1]  # Можно и по-другому, но структура все равно постоянная
    tree_path = '.git/objects/' + tree_code[:2] + '/' + tree_code[2:]

with open(tree_path, 'rb') as tree_file:
    treeobj = zlib.decompress(tree_file.read())
    header, _, body = treeobj.partition(b'\x00')
    while body:
        treehdr, _, tail = body.partition(b'\x00')
        gitid, body = tail[:20], tail[20:]
        print(f'{treehdr}, {gitid.hex()}')

