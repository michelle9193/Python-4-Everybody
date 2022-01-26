# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
# print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

score = input('Enter a score between 0.0 and 1.0 ')
s = float(score)
try:
    if s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    else:
        print('You have Failed')
except:
    print('Please check the number you have printed ')
