import math
from math import cos, degrees, radians

math.pi == math.pi
math.cos == math.cos
math.degrees == math.degrees

print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')




height_outside_edge_lowest_wall = float(input(f'What is the height of the '
                                        f'lowest wall on the outside edge? '))
print(' ')

top_plate_thickness = float(input(f'What is the top plates thickness? '))
print(' ')

wall_angle = float(input('What is the angle of the wall? '))
print(' ')


#plumb_cut = top_plate_thickness / (math.degrees(math.cos(wall_angle)))
plumb_cut = (top_plate_thickness / math.sin((90-wall_angle)*(math.pi/180)))
plumb_cut = round(plumb_cut, 3)

bottom_plate_thickness = float(input('What is the bottom plate thickness? '))
print(' ')

FIRST_SHORTEST_stud_length = (height_outside_edge_lowest_wall 
                              - (plumb_cut + bottom_plate_thickness))

FIRST_SHORTEST_stud_length = round(FIRST_SHORTEST_stud_length, 3)

print(f"The 'plumb cut' is " + '\033[1m' + f"{plumb_cut}" + '\033[0m' )
print(f'The very first (shortest) stud length in the raked wall is '
      f'\033[1m' + f'{FIRST_SHORTEST_stud_length}' + '\033[0m' + ' long')

print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')

stud_space_running = float(input(f'What is the running stud spacing (the '
                                 f'distance between each of the studs)? '))
print(' ')
what_number_stud = input(f"What number stud along the bottom plate "
                         f"(excluding the very first one on "
                         f" the outside edge, so the miniumum input here is "
                         f"'2') is the one you're calculating the height of? ")
print(' ')
rise_of_stud = (math.tan(wall_angle*math.pi/180)*stud_space_running)
rise_of_stud = round(rise_of_stud, 3)

print(f'The rise of stud number ' + '\033[1m' + f'{what_number_stud}'
      + f'\033[0m' + ' is: '   + '\033[1m' + f'{rise_of_stud}' + '\033[0m')
print(' ')
calculated_stud_length = FIRST_SHORTEST_stud_length + rise_of_stud

print(f'The stud length for stud number ' + '\033[1m' + f'{what_number_stud}'
      + f'\033[0m' + ' is: '  + '\033[1m' 
      + f'{calculated_stud_length}' + '\033[0m')
print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')