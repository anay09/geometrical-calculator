import math


def size_of_one_exterior_angle(no_of_sides):
    return 360/no_of_sides


def size_of_one_interior_angle(no_of_sides):
    return (no_of_sides-2)*180/no_of_sides


def total_size_of_interior_angles(no_of_sides):
    return (no_of_sides-2)*180


def sine_rule_side(ang1, ang2, sid1):
    return math.sin(ang2)*sid1/math.sin(ang1)

def sine_rule_angle(ang1, sid2, sid1):
    return math.asin(sid2*math.sin(ang1)/sid1)



print('------------------Geometrical Calculator-------------------')

print('\n\nChoose one of the following to continue...')
print('\n\n    - A - Triangle Geometry (including trigonometric problems)')
print('    - B - Details of Regular Polygon (interior angles)')
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
        print('    - A1 - Sine Rule(angle)')
        print('    - A2 - Sine Rule(side)')
        print('    - B1 - Cosine Rule(angle)')
        print('    - B2 - Cosine Rule(side)')
        print('    - C - Area of Non-Right angle triangle')
        print('    - D - Find side from one angle and side')
        print('    - E - Find angle from 2 sides')
        print("    - F - Heron's Formula")
        print("    - G - Pythagoras Theorem")
        tri_option = input('Choose one : ')
    if option == 'B':
        print('You have chosen details of regular shapes.')
        shape_type = int(input('Please enter the number of sides on the shape (only up to dodecagon i.e. 12 sides)  : '))
        if shape_type == 3:
            print('Shape Name = Triangle\n'
                  'Shape Types = Isosceles, right-angled, scalene, equilateral\n'
                  'Total Size of Interior Angles = '
                  '')
