# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program.

enter_hours = input('Enter hours: ')
enter_rate = input('Enter rate: ')
try:
    hours = float(enter_hours)
    rate = float(enter_rate)
    print(hours * rate)
except:
    print('Please enter a number')
