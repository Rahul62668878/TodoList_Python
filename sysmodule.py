# ? write python program  to display current date and time

from datetime import date
# print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# find area of circle
""" def areaofcircle(r):
    return 3.14 *r*r
radius = float(input("enter radius of circle:"))
print(f"area of circle is:{areaofcircle(radius)}") """

# ? which accepts the user fistName and lastName and print them in reverse order

""" fist_name = input("enter your first name:")
last_name = input('enter yout last name:')
print(f"first name is - {fist_name[::-1]} and last name is - {last_name[::-1]}") """

# ?  write a python program to accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers 
""" values = input("enter some comma separedt values:")
list = values.split(",")
tuple= tuple(list)
print(f"list is {list}")
print(f"tuple is {tuple}") """

# ? write a python program to accepts a filename from user and print the extension of that
""" filename = input("enter filename:")
ext = filename.split('.')
print(f"{ext[-1]} is extension of {filename}") """

# ? write a python program to display the first and last colors from the following list
""" color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1]) """
# ?write a python program to display calendar
""" import calendar
month = int(input("enter month:"))
year = int(input("enter a year: "))

print(calendar.month(year,month)) """

# ?write a python program to calculate number of days between two dates

f_date = date(2014, 7, 2)
l_date = date(2014, 7, 10)

print(l_date - f_date)