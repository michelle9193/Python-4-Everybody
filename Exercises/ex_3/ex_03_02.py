enter_hours = input('Enter hours: ')
enter_rate = input('Enter rate: ')
try:
    hours = float(enter_hours)
    rate = float(enter_rate)
    print(hours * rate)
except:
    print('Please enter a number')