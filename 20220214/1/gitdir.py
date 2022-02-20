import sys
import zlib


def printer(name, gitid, height):
    type, filename = name.split()[0], name.split()[1]
    print('--- ' * height + str(filename)[2:-1] + ', [' + gitid + ']')
    if type == b'40000':  # папка
        tree_path = '.git/objects/' + gitid[:2] + '/' + gitid[2:]
        with open(tree_path, 'rb') as tree_file:
            treeobj = zlib.decompress(tree_file.read())
            header, _, body = treeobj.partition(b'\x00')
            while body:
                treehdr, _, tail = body.partition(b'\x00')
                gitid, body = tail[:20], tail[20:]
                printer(treehdr, gitid.hex(), height + 1)


branch_name = sys.argv[1]
branch_file = '.git/refs/heads/' + branch_name
with open(branch_file) as file:
    branch_code = file.read()
branch_code = branch_code[:-1]
parent_commit = True  # заведомо бессиысленное значение для входа в цикл
while parent_commit:
    commit_path = '.git/objects/' + branch_code[:2] + '/' + branch_code[2:]
    with open(commit_path, 'rb') as objfile:
        fullobj = zlib.decompress(objfile.read())
        header, _, body = fullobj.partition(b'\x00')
        info_text = body.decode()
        info_list = info_text.split()
        try:
            index = info_list.index('parent')  # поиск родительского коммита в описании самого коммита
            parent_commit = info_list[index + 1]  # выход за пределы массива невозможен
        except ValueError:
            parent_commit = False
        tree_code = info_text.split()[1]  # Можно и по-другому, но структура все равно постоянная
        tree_path = '.git/objects/' + tree_code[:2] + '/' + tree_code[2:]

    with open(tree_path, 'rb') as tree_file:
        treeobj = zlib.decompress(tree_file.read())
        header, _, body = treeobj.partition(b'\x00')
        while body:
            treehdr, _, tail = body.partition(b'\x00')
            gitid, body = tail[:20], tail[20:]
            printer(treehdr, gitid.hex(), 0)
    print('\n', '=' * 20, '\n', sep='')
    branch_code = parent_commit

