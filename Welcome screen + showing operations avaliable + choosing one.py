import math
import os

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
    elif desired_calculation == '4':        #Volume!
        print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
        enter_line()
#Lists avaliable volumes
        print('\033[1m' + 'Shape volumes avaliable: ')
        enter_line()

        print('\033[0m' + '1. Cuboid')
        print('2. Cube')
        print('3. Cylinder')
        print('4. Cone')
        print('5. Sphere')
        enter_line()

        #needed math imports:
        math.pi == math.pi
        
#Uses while true so that the continue statement and break can work
        while True:
            what_shape = input("What shape's volume would you like to calculate from the list? ")
            os.system('cls')        #Clwars the terminal as the code is 'playing'
            if what_shape == '1':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Cuboid volume selected: ')
                enter_line()
                height = float(input('\033[0m' + 'What is the height of the cuboid? ')) #'float' allows for decimals as builders work to decimals to be specific
                enter_line()
                width = float(input('What is the width of the cuboid? '))
                enter_line()
                depth = float(input('What is the depth of the cuboid? '))
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Cuboid volume selected: ')
                enter_line()
        
                cuboid_volume = height * width * depth
                cuboid_volume_rounded = round(cuboid_volume, 3)     #rounds the answer to 3 decimal places for efficiency and makes it easier for reading

                print(f'\033[0m' + "Your cuboid's volume is: " '\033[1m' f'{cuboid_volume_rounded}')
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')

                break                               #'break' stops the 'continue' and prevents it from repeating infinitily
            elif what_shape == '2':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Cube volume selected: ')
                enter_line()
                measurement = float(input('\033[0m' + 'What is the side measurement of the cube? '))
                enter_line()
    
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Cube volume selected: ')
                enter_line()
    
                cube_volume = measurement * 3
                cube_volume_rounded = round(cube_volume, 3)

                print(f'\033[0m' + "Your cube's volume is: " '\033[1m' f'{cube_volume_rounded}')
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                break
            elif what_shape == '3':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Cylinder volume selected: ')
                enter_line()
                height = float(input('\033[0m' + 'What is the height of the cylinder? '))
                enter_line()
                radius = float(input('What is the radius of the cylinder? '))
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Cylinder volume selected: ')
                enter_line()
                
                cylinder_volume = math.pi * (radius ** 2) * height
                cylinder_volume_rounded = round(cylinder_volume, 3)

                print(f'\033[0m' + "Your cylinders's volume is: " '\033[1m' f'{cylinder_volume_rounded}')
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                break
            elif what_shape == '4':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()       
                print('\033[1m' + 'Cone volume selected: ')
                enter_line()
                height = float(input('\033[0m' + 'What is the height of the cone? '))
                enter_line()
                radius = float(input('What is the radius of the cone? '))
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Cone volume selected: ')
                enter_line()
                
                cone_volume = math.pi * (radius ** 2) * (height/3)
                cone_volume_rounded = round(cone_volume, 3)

                print(f'\033[0m' + "Your cones's volume is: " '\033[1m' f'{cone_volume_rounded}')
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                break
            elif what_shape == '5':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Sphere volume selected: ')
                enter_line()
                radius = float(input('What is the radius of the sphere? '))
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('\033[1m' + 'Sphere volume selected: ')
                enter_line()
                
                sphere_volume = (4/3) * math.pi * (radius ** 3)
                sphere_volume_rounded = round(sphere_volume, 3)

                print(f'\033[0m' + "Your sphere's volume is: " '\033[1m' f'{sphere_volume_rounded}')
                enter_line()
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                break
            else:
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                enter_line()
                print('Invalid input, try a number between 1 and 5')
                enter_line()
                continue
                break
    elif desired_calculation == '5':
        print('placeholder')
        break
    else:
        print('Invalid input, try a number between 1 and 5')
        enter_line()
        continue


