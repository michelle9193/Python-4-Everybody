score = input('Enter a score between 0.0 and 1.0 ')
try:
    if score >= 0.9:
        print('A');
    if score >= 0.8:
        print('B');
    if score >= 0.7:
        print('C');
    if score >= 0.6:
        print('D');
    if score < 0.6:
        print('You have Failed');
except:
    print('Please check the number you have printed ')
