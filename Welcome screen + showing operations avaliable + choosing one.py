import math
import os


def calc_decking():     #DECKING OPTION (1) EXAMPLE/TEMPLATEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    answer1 = int(input('What is the length? '))
    sleep1 = input('what is the width? ')
    sleep1=int(sleep1)
    decking_result = answer1*sleep1  
    return decking_result

def calc_stud():        #STUD OPTION (2)
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    answer1 = input('What is the length? ')
    answer1=int(answer1)
    sleep1 = input('what is the width? ')
    sleep1=int(sleep1)
    stud_result = answer1*sleep1  
    return stud_result

#desired_calculation = 3 ('what shape' calculation functions) TESTED AND WORK
def calc_rectangle_area():
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Rectangle area selected: ')
    print('')                
    width = float(input('\033[0m' + 'What is the width of the rectangle? '))
    print('')
    length = float(input('What is the length of the rectangle? '))
    print('')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Rectangle volume selected: ')
    print('')
    
    rectangle_area = width * length
    rectangle_area_rounded = round(rectangle_area, 3)
    return rectangle_area_rounded
def calc_square_area():
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('') 
    print('\033[1m' + 'Square area selected: ')
    print('')
    measurement = float(input('\033[0m' + 'What is the side length of the square? '))
    print('')

    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print('')
    print('\033[1m' + 'Square area selected: ')
    print('')
    
    square_area = measurement * 2
    square_area_rounded = round(square_area, 3)
    return square_area_rounded
def calc_circle_area():
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Circle area selected: ')
    print(' ')
    radius = float(input('What is the radius of the circle? '))
    print(' ')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Circle area selected: ')
    print(' ')
    
    circle_area = math.pi * (radius ** 2)
    circle_area_rounded = round(circle_area, 3)
    return circle_area_rounded
def calc_cylinder_area():
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')       
    print('\033[1m' + 'Cylinder (Surface Area) selected: ')
    print(' ')
    radius = float(input('\033[0m' + 'What is the radius of the cylinder? ')) 
    print(' ')
    height = float(input('What is the height of the cylinder? '))
    print(' ')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Cylinder (Surface Area) selected: ')
    print(' ')
    
    cylinder_area = (2 * math.pi * radius * height) + (2 * math.pi * (radius **2))
    cylinder_area_rounded = round(cylinder_area, 3)
    return cylinder_area_rounded
def calc_triangle_area():
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Triangle area selected: ')
    print(' ')
    height = float(input('\033[0m' +'What is the height of the triangle? '))
    print(' ')
    base = float(input("What is the length of the triangle's base? "))
    print(' ')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    os.system('cls')
    print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
    print(' ')
    print('\033[1m' + 'Triangle area selected: ')
    print(' ')
    
    triangle_area = (height * base)/2
    triangle_area_rounded = round(triangle_area, 3)
    return triangle_area_rounded

#exit/goodbye ("6. Exit")
def goodbye_exit_screen():
    os.system('cls')
    print('★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ 　° :. ★　 * • ○ ° ★ .　 * 　.　. ° 　. ● . ★ ° . *　　　°　.　°☆')
    print(' ')
    print('You will be missed..')
    print(' ')
    print('    ／＞　  　フ')   #Cat and stars from "fonts" mobile app
    print('    | 　_　 _ |')
    print('   ／` ミ＿xノ')
    print('  /　　　 　 |')
    print(' /　 ヽ　　 ﾉ')
    print('│　　| | |')
    print(' ')
    print('Thank you for using ConCalc!! Goodluck on your project/s and return soon!')
    print(' ')
    print('★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ 　° :. ★　 * • ○ ° ★ .　 * 　.　. ° 　. ● . ★ ° . *　　　°　.　°☆')

#Main Program
print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
print(' ')

print('Welcome to the program!!')
print(' ')

print('How to use the program: You’ll notice that all items in the lists shown are numbered, when asked for what you’d like to complete please enter the corresponding number to the operation you’d like.')
print(' ')
print('Operations avaliable: ')
print(' ')

print('\033[1m' + 'Complex: ')
print('\033[0m' + '1. Linear Metres Of Decking Required ')
print('2. Stud Length (/Raked Wall) ')
print(' ')

print('\033[1m' + 'Simple: ')
print('\033[0m' + '3. Area Of A Shape ')
print('4. Volume Of A Shape ')
print('5. Basic Mathematic Calculations ')

print('6. Exit ')
print(' ')

desired_calculation = input('What calculation would you like to complete from the list/s? ')
desired_calculation = int(desired_calculation)
while desired_calculation != 6:     #as long as it isn't '6' it does this
    print(' ')
    os.system('cls')

    if desired_calculation == 1:  #works
        os.system('cls')
        decking_result = calc_decking()
        print(f'{decking_result}')                               #NOTE FROM B4:: 'break' stops the 'continue' and prevents i from repeating infinitily

    elif desired_calculation == 2:  #works
        os.system('cls')
        stud_result = calc_stud()
        print(f'{stud_result}')
        
    elif desired_calculation == 3:        #Area!
        os.system('cls')
        #display/list of operations
        print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
        print(' ')

        print('\033[1m' + 'Shape areas avaliable: ')
        print(' ')

        print('\033[0m' + '1. Rectangle')
        print('2. Square')
        print('3. Circle')
        print('4. Cylinder (Surface Area)')
        print('5. Triangle')
        print('6. Exit')
        print(' ')

        what_shape = input("What shape's area would you like to calculate from the list? ")
        what_shape = int(what_shape)
        
        #invalid ans        WORKS
        while what_shape < 1:
            print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
            print(' ')
            print('Invalid input, try a number between 1 and 5')
            print(' ')
            what_shape = input("What shape's area would you like to calculate from the list? ")
            what_shape = int(what_shape)

        #BUG FROM HERE SOMEWHERE?!?!!? 
            
        #needed math imports:
        math.pi == math.pi

        #while loop for 'area' option (SUB OPTIONS OF MAIN WHILE) (nested?!?!)
        while what_shape != 6:
            os.system('cls')
            #rectangle
            if what_shape == '1':

                rectangle_area_rounded = calc_rectangle_area()
        
                print(f'\033[0m' + "Your rectangle's area is: " '\033[1m' f'{rectangle_area_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                
            #square                           
            elif what_shape == '2':
                
                square_area_rounded = calc_square_area()

                print(f'\033[0m' + "Your cube's volume is: " '\033[1m' f'{square_area_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
            #circle    
            elif what_shape == '3':
                
                circle_area_rounded = calc_circle_area()

                print(f'\033[0m' + "Your circle's area is: " '\033[1m' f'{circle_area_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')

            #cylinder    
            elif what_shape == '4':
                
                cylinder_area_rounded = calc_cylinder_area()

                print(f'\033[0m' + "Your cylinder's surface area is: " '\033[1m' f'{cylinder_area_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')

            #triagle    
            elif what_shape == '5':
               
                triangle_area_rounded = calc_triangle_area()

                print(f'\033[0m' + "Your triangle's area is: " '\033[1m' f'{triangle_area_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
            
        while what_shape == 6: #works
            os.system('cls')
            print('★ ° . *　　　°　.　°☆ 　. * ● ¸ . 　　　★ 　° :. ★　 * • ○ ° ★ .　 * 　.　 . ° 　. ● . ★ ° . *　　　°　.　°☆')
            print(' ')
            another_calc = input('Would you like to complete another operation? ')
            print(' ')
            if another_calc == 'yes':
                print('CONINUE BUT FOR NOW PLACEHOLDERRRRRRR')
            elif another_calc == 'no':
                goodbye_exit_screen()


    elif desired_calculation == '4':        #Volume!
        os.system('cls')
        print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
        print(' ')
        #Lists avaliable volumes
        print('\033[1m' + 'Shape volumes avaliable: ')
        print(' ')

        print('\033[0m' + '1. Cuboid')
        print('2. Cube')
        print('3. Cylinder')
        print('4. Cone')
        print('5. Sphere')
        print(' ')

        #needed math imports:
        math.pi == math.pi

        #Uses while true so that the continue statement and break can work
        while True:
            what_shape = input("What shape's volume would you like to calculate from the list? ")
            os.system('cls')        #Clears the terminal as the code is 'playing'
            if what_shape == '1':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Cuboid volume selected: ')
                print(' ')
                height = float(input('\033[0m' + 'What is the height of the cuboid? ')) #'float' allows for decimals as builders work to decimals to be specific
                print(' ')
                width = float(input('What is the width of the cuboid? '))
                print(' ')
                depth = float(input('What is the depth of the cuboid? '))
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Cuboid volume selected: ')
                print(' ')
        
                cuboid_volume = height * width * depth
                cuboid_volume_rounded = round(cuboid_volume, 3)     #rounds the answer to 3 decimal places for efficiency and makes it easier for reading

                print(f'\033[0m' + "Your cuboid's volume is: " '\033[1m' f'{cuboid_volume_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')

                break                               #'break' stops the 'continue' and prevents it from repeating infinitily
            elif what_shape == '2':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Cube volume selected: ')
                print(' ')
                measurement = float(input('\033[0m' + 'What is the side length of the cube? '))
                print(' ')
    
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Cube volume selected: ')
                print(' ')
    
                cube_volume = measurement * 3
                cube_volume_rounded = round(cube_volume, 3)

                print(f'\033[0m' + "Your cube's volume is: " '\033[1m' f'{cube_volume_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                break
            elif what_shape == '3':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Cylinder volume selected: ')
                print(' ')
                height = float(input('\033[0m' + 'What is the height of the cylinder? '))
                print(' ')
                radius = float(input('What is the radius of the cylinder? '))
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Cylinder volume selected: ')
                print(' ')
                
                cylinder_volume = math.pi * (radius ** 2) * height
                cylinder_volume_rounded = round(cylinder_volume, 3)

                print(f'\033[0m' + "Your cylinders's volume is: " '\033[1m' f'{cylinder_volume_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                break
            elif what_shape == '4':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')       
                print('\033[1m' + 'Cone volume selected: ')
                print(' ')
                height = float(input('\033[0m' + 'What is the height of the cone? '))
                print(' ')
                radius = float(input('What is the radius of the cone? '))
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Cone volume selected: ')
                print(' ')
                
                cone_volume = math.pi * (radius ** 2) * (height/3)
                cone_volume_rounded = round(cone_volume, 3)

                print(f'\033[0m' + "Your cones's volume is: " '\033[1m' f'{cone_volume_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                break
            elif what_shape == '5':
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Sphere volume selected: ')
                print(' ')
                radius = float(input('What is the radius of the sphere? '))
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                os.system('cls')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('\033[1m' + 'Sphere volume selected: ')
                print(' ')
                
                sphere_volume = (4/3) * math.pi * (radius ** 3)
                sphere_volume_rounded = round(sphere_volume, 3)

                print(f'\033[0m' + "Your sphere's volume is: " '\033[1m' f'{sphere_volume_rounded}')
                print(' ')
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                break
            else:
                print('☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
                print(' ')
                print('Invalid input, try a number between 1 and 5')
                print(' ')
                continue
                break
    #elif desired_calculation == '5':
        print('placeholder')
        break

#while int(desired_calculation) < 1:
    print('Invalid input, try a number between 1 and 5')
    print(' ')
    desired_calculation = input('What calculation would you like to complete from the list/s? ')
    desired_calculation = int(desired_calculation)

while desired_calculation == 6: #EXIT works
    goodbye_exit_screen()
    break

