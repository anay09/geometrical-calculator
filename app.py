import math

print('------------------Geometrical Calculator-------------------')

print('\n\nChoose one of the following to continue...')
print('\n\n    - A - Triangle Geometry (including trigonometric problems)')
print('    - B - Details of Regular Shapes (interior angles)')
print('    - C - Area and Perimeter Calculator')
print('    - D - Graphical Area')
print('    - E - Volume Calculator')
print('    - F - Surface Area Calculator')
print('    - G - Find the Missing Angle')
print('    - X - Exit')

option = input('Please choose one of the following : ')

while True:
    if option == 'A':
        print('You have chosen triangle geometry. Please choose another one of the following...')
        print('    - A - Sine Rule')
        print('    - B - Cosine Rule')
        print('    - C - Area of Non-Right angle triangle')
        print('    - D - Find side from one angle and side')
        print('    - E - Find angle from 2 sides')
        print("    - F - Heron's Formula")
        print("    - G - Pythagoras Theorem")
    if option == 'B':
        print('You have chosen details of regular shapes.')
