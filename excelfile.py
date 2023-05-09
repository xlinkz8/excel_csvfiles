import os
import sys


names = ["lion\n" , "beast\n", "leopard\n", "wild\n" , "monkey\n"]
names2 = ["movie\n" ,"music\n", "animal\n", "software\n", "benz\n"]


with open(os.path.join(sys.path[0],"books_name.xls"), "w") as book:
    names_write = book.writelines(names)
    names_write2 = book.writelines(names2)

    print("excel file created successfully")