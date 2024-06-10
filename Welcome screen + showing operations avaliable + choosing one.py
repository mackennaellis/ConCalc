#from math import

def enter_line():                   #to leave an 'enter' space between lines 
    print(' ')                       #to make it easier for users to read
    return

print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
enter_line()

print('Welcome to the program!!')
enter_line()

print('How to use the program: You’ll notice that all items in the lists shown are numbered, when asked for what you’d like to complete please enter the corresponding number to the operation you’d like.')
enter_line()
print('Operations avaliable: ')
enter_line()

print('\033[1m' + 'Complex: ')
print('\033[0m' + '1. Linear Metres Of Decking Required ')
print('2. Stud Length (/Raked Wall) ')
enter_line()

print('\033[1m' + 'Simple: ')
print('\033[0m' + '3. Area Of A Shape ')
print('4. Volume Of A Shape ')
print('5. Basic Mathematic Calculations ')
enter_line()


#AFTER

while True:
    desired_calculation = input('What calculation would you like to complete from the list/s? ')
    #desired_calculation = int(desired_calculation)
    enter_line()

    if desired_calculation == '1':
        print('hello')
        break                               #'break' stops the 'continue' and prevents i from repeating infinitily
    elif desired_calculation == '2':
        print('bye')
        break
    elif desired_calculation == '3':
        print('place')
        break
    elif desired_calculation == '4':
        print('holder')
        break
    elif desired_calculation == '5':
        print('placeholder')
        break
    else:
        print('Invalid input, try a number between 1 and 5')
        enter_line()
        continue


