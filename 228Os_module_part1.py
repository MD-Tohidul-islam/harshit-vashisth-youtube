import os

# fuctions: os.getcwd()
print(os.getcwd())
# to create a folder use os.mkdir
#os.mkdir('example_folder')
# to check exiting folder: os.path.exists('write path')
print(os.path.exists('example_folder'))

# to create a file
open('example_file.text','w').close()

# to create a file to other directory
#os.mkdir(r"E:\programing's tutorial\seen\harshit vashisth this is best\example_folder")

# to change current directory to other directory
# os.chdir("E:\programing's tutorial\seen\harshit vashisth this is best")

# to see all file in folder
# print(os.listdir())  # to see all file in folder in other directory use os.listdir(path)

# to see path of file in folder
# for item in os.listdir():
#     print(os.getcwd(),'\\',item)
for item in os.listdir():
    print(os.path.join(os.getcwd(),item))






