import math
from math import cos, degrees, radians

math.pi == math.pi
math.cos == math.cos
math.degrees == math.degrees

print(f'\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
          f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲')
height_outside_edge_lowest_wall = float(input(f'What is the height of the '
                                        f'lowest wall on the outside edge? '))
print(' ')

top_plate_thickness = float(input(f'What is the top plates thickness? '))
print(' ')

wall_angle = float(input('What is the angle of the wall? '))
print(' ')


#print(math.radians(height_outside_edge_lowest_wall))
#print(math.radians(top_plate_thickness))
#print(math.radians(wall_angle))


#plumb_cut = top_plate_thickness / (math.degrees(math.cos(wall_angle)))
plumb_cut = (top_plate_thickness / math.sin((90-wall_angle)*(math.pi/180)))
print(plumb_cut)


bottom_plate_thickness = float(input('What is the bottom plate thickness? '))
print(' ')

FIRST_SHORTEST_stud_length = height_outside_edge_lowest_wall - (plumb_cut + bottom_plate_thickness)

print(FIRST_SHORTEST_stud_length)