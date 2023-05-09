import csv

input_file = "phone_number.txt"

output_file = "phone_number.csv"


with open(input_file, "r") as file:
    phone_numbers = file.read().splitlines()


phone_numbers_list = [[phone_number] for phone_number in phone_numbers ] 


with open(output_file, "w", newlines="") as file: