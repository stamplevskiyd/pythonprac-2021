import os
import sys
import zlib

branch_name = sys.argv[1]
branch_file = '.git/refs/heads/' + branch_name
with open(branch_file) as file:
    branch_code = file.read()
commit_path = '.git/objects/'+ branch_code[:2] + '/'+ branch_code[2:]
with open(commit_path[:-1], 'rb') as objfile:
    fullobj = zlib.decompress(objfile.read())
    header, _, body = fullobj.partition(b'\x00')
    print(body.decode())
