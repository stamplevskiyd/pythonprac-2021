from os import listdir

branch_list = '.git/refs/heads'
for branch_name in listdir(branch_list):
    print(branch_name)
    
