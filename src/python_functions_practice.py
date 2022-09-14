def return_10():
    return 10

def add(num1, num2):
    add_result = num1 + num2
    return add_result

def subtract(num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2

def length_of_string(str):
    return len(str)

def join_string(str1, str2):
    return str1 + str2

def add_string_as_number(str1, str2):
    return int(str1) + int(str2)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(num):
    for month in months:
        if month == months[num]:
            return months[num - 1]
# Is this the correct way to run this test?
# I've created a function above and then used 
# The values provided to pass as arguments
# To the function.

number_to_full_month_name(3)

number_to_full_month_name(9)

def number_to_short_month_name(num):
    for month in months:
        if month == months[num]:
            # Use the index of a string to slice the first three letters.
            return months[num - 1][0:3]

number_to_short_month_name(4)

number_to_short_month_name(10)

def calc_volume_of_cube(length):
    return length ** 3

def reverse_string(str):
    return str[::-1]

def convert_farenheit_to_celsius(temp):
    return round((temp - 32) * 0.5556, 1)

   





