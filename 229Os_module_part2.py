import os
#print(os.chdir(r"E:\programing's tutorial\seen"))
print(os.listdir(r"E:\programing's tutorial\seen"))
fileiter = os.walk(r"E:\programing's tutorial\seen")
#print(os.getcwd())

for current_path,folder_name,file_names in fileiter:
    print(f'current path: {current_path}')
    print(f'folder name: {folder_name}')
    print(f'file name: {file_names}')

# to remove empty folder
#os.rmdir(r"E:\programing's tutorial\seen\New folder\New folder")

# to create a folder in a folder
#os.makedirs(r"E:\programing's tutorial\seen\New folder\Newfolder")


import shutil

# to remove a folder
#shutil.rmtree(r"E:\programing's tutorial\seen\New folder\Newfolder")

# to copy a folder from other foder
#shutil.copytree(r"E:\programing's tutorial\seen\New folder\New folder\new",r"E:\programing's tutorial\seen\new")
#shutil.copy(r"E:\programing's tutorial\seen\New folder\New folder\file.txt",r"E:\programing's tutorial\seen\file1.txt")
shutil.move(r"E:\programing's tutorial\seen\New folder\New folder\file.txt",r"E:\programing's tutorial\seen\file2.txt")

