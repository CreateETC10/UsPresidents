## Display presidents with a specified first name.
from operator import truediv


first_name = input("Enter a fisrt name: ")
found_flag = False
infile = open("USPres.txt",'r')
for line in infile:
    if line.startswith(first_name + ' '):
        print(line.rstrip())
        found_flag = True
if not found_flag:
    print("NO president had the first name", first_name + '.')

