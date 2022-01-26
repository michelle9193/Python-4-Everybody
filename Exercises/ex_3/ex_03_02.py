# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program.

hours = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    fh = float(hours)
    fr = float(rate)
    if fh > 40:
        reg = fh * fr
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
    else:
        xp = fh * fr
    print("Pay: ", xp)
except:
    print('Error, please enter numeric input')
