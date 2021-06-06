import os
import os.path
ext_from = ".gif"
ext_to = '.png'
read_file_dir =input('请输入要修改文件扩展名得路径： ')
files = os.listdir(read_file_dir)
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1]==ext_from:
        newname = portion[0]+ext_to
        os.chdir(read_file_dir)
        os.rename(filename,newname)
import matplotlib

