# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

hours = input('Enter hours: ')
rate = input('Enter rate: ')
fh = float(hours)
fr = float(rate)

if fh > 40:
    # print('Overtime')
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg, otp)
    xp = reg + otp
else:
    # print('Regular')
    xp = fh * fr
print("Pay: ", xp)
