import math
import os

def enter_line():                   #to leave an 'enter' space between lines 
    print(' ')                       #to make it easier for users to read
    return

print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
enter_line()

print('\033[1m' + 'Basic calculations avaliable: ')
enter_line()

print('\033[0m' + '1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
enter_line()

while True:
    basic_calc = input('Which basic calculation from the list would you like to calculate? ')
    enter_line()
    os.system('cls')

    if basic_calc == '1':
        numerical_to_add = []

        print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
        enter_line()
        

        break
    elif basic_calc == '2':
        print(':)')
        break
    elif basic_calc == '3':
        print(':(')
        break   
    elif basic_calc == '4':
        #remainder = x%y        for remainder use '%' instead of '/'
        print(':3')
        break 
    else:
        print('Invalid input, try a number between 1 and 5')
        enter_line()
        continue