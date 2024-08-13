print(f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲'
            f'☲☲')
print(' ')
print('\033[1m' + 'Linear Metres Of Decking Required Selected: ')
print('')           
print(f'\033[0m' + f'Next to the questions, units will be stated. '
      f'Please do not include the units in your input '
      f'it is simply to tell you what units the input '
      f'should be in.')     
print(' ')
width = float(input(f"What is the width of the decking boards "
                    f"you're going to be using (units: millimetres)? "))
print(' ')
gap = float(input(f'What is the width of the gap between the '
                  f'decking boards horizontally (units: '
                  f'millimetres)? '))
print('')
deck_width = float(input(f'What is the width of the overall '
                         f'(whole) deck (units: metres)? '))
print(' ')
deck_length = float(input(f'What is the length of the overall '
                          f'(whole) deck (units: metres)? '))
print(' ')
print(f'**A waste percentage is how much waste (extra) '
      f'are you allowing for. Between 5 - 15% is '
      f'recommended with 10% usually being a great allowance. '
      f'At least greater then '0'**')
print(' ')
waste_percentage_num = float(input(f'What is the waste percentage '
                               f'number you would like to allow '
                               f'(units: percentage)? '))
    #not 0

decking_area = deck_width * deck_length
decking_area_rounded = round(decking_area, 3)

waste_percentage = (waste_percentage_num / 100) + 1

#Amount in m^2 one linear metre (board??) takes up
decking_area_in_m2 = (gap + width) / 1000

quantity_linear_m = ((decking_area**2) / decking_area_in_m2) * waste_percentage



