import os
import sys

files = open(os.path.join(sys.path[0], "phone_list.txt"), "r")
   

read_file = files.read()
print(read_file)


files.close()