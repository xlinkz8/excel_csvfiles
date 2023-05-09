import os
import sys





files = open(os.path.join(sys.path[0],"books_name.xls"), "r")


read_files = files.read()

print(read_files)

files()