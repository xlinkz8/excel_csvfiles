import os
import sys 


phone_num = ["07060961267\n" , "0904532178\n" , "08111362311\n" , "08037431094\n"]
phone_num2 = ["0912343545\n" , "07067431097\n" ,"08022374576\n", "09043217894\n"]

with open(os.path.join(sys.path[0], "phone_num.csv"), "w") as phone:
     phone_num_write = phone.writelines(phone_num)
     phone_num_write2 = phone.writelines(phone_num2)

print("successfully written csv file")