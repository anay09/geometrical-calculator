import math


def radian(degrees):
    return math.pi/180 * degrees


def degree(radians):
    return radians * 180 / math.pi


def size_of_one_exterior_angle(no_of_sides):
    return 360/no_of_sides


def size_of_one_interior_angle(no_of_sides):
    return (no_of_sides-2)*180/no_of_sides


def total_size_of_interior_angles(no_of_sides):
    return (no_of_sides-2)*180


def sine_rule_side(ang1, ang2, sid1):
    return math.sin(radian(ang2))*sid1/math.sin(radian(ang1))


def sine_rule_angle(ang1, sid2, sid1):
    return degree(math.asin(sid2*math.sin(radian(ang1))/sid1))


def cos_rule_side(sid1, sid2, ang3):
    return (sid1 ^ 2 + sid2 ^ 2) - 2*sid1*sid2*math.cos(radian(ang3))


def cos_rule_angle(sid1,sid2,sid3):
    return degree(math.acos((sid1 ^ 2 + sid2 ^ 2 - sid3 ^ 2)/2*sid1*sid2))


def area_non_right_angle_triangle(sid1, sid2, ang3):
    return 0.5*sid1*sid2*math.sin(ang3)


def simple_inverse_trigonometry(opp, adj, hyp, is_opp, is_adj, is_hyp):
    if (is_opp == True) and (is_hyp == True):
        return math.asin(opp/hyp)
    elif is_adj == True and is_hyp == True:
        return math.acos(adj/hyp)
    elif is_opp == True and is_adj == True:
        return math.atan(opp/adj)


def heron_formula(sid1, sid2, sid3):
    s = (sid1 + sid2 + sid3)/2
    return math.sqrt(s*(s-sid1)*(s-sid2)*(s-sid3))


def pythagoras_theorem(sid1, sid2, is_find_hyp):
    if is_find_hyp==True:
        return math.sqrt(sid1 ^ 2 + sid2 ^ 2)
    else:
        return math.sqrt(sid1 ^ 2 - sid2 ^ 2)


def rectangle_square_parallelogram_area(length, width):
    return length*width

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
print(math.sin(30))
option = input('\nPlease choose one of the following : ')
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
        if tri_option == 'A1':
            sid1 = float(input('Please enter the length of a side : '))
            ang1 = float(input('Please enter the opposite angle of this side :'))
            sid2 = float(input('Please enter the length of the desired side : '))
            print(sine_rule_angle(ang1, sid2, sid1))
        elif tri_option == 'A2':
            sid1 = float(input('Please enter the length of a side : '))
            ang1 = float(input('Please enter the opposite angle of this side :'))
            ang2 = float(input('Please enter the angle of the desired side : '))
            print(sine_rule_side(ang1, ang2, sid1))
        elif tri_option == 'B1':
            #sid1 = float(input('Please enter the length of a side : '))
            #sid2 = float(input('Please enter the length of another side :'))
            #sid3 = float(input('Please enter the length of the side opposite to the desired angle : '))
            #print(cos_rule_angle(sid1, sid2, sid3))

    elif option == 'B':
        print('You have chosen details of regular shapes.')
        shape_type = int(input('Please enter the number of sides on the shape (only up to 12 sides)  : '))
        if shape_type == 3:
            print('\nShape Name = Triangle'
                  '\nShape Types = Isosceles, right-angled, scalene, equilateral')
        elif shape_type == 4:
            print('\nShape Name : Quadrilateral'
                  '\nShape Types : Square, Rectangle, Kite, Trapezium, Parallelogram, Rhombus')
        elif shape_type == 5:
            print('Shape Name : Pentagon')
        elif shape_type == 6:
            print('Shape Name : Hexagon')
        elif shape_type == 7:
            print('Shape Name : Heptagon')
        elif shape_type == 8:
            print('Shape Name : Octagon')
        elif shape_type == 9:
            print('Shape Name : Nonagon')
        elif shape_type == 10:
            print('Shape Name : Decagon')
        elif shape_type == 11:
            print('Shape Name : Undecagon')
        elif shape_type == 12:
            print('Shape Name : Dodecagon')
        else:
            print('Invalid Number!!!')
        print('Total Size of Interior Angles = {a}'
              '\nSize of One Interior Angle (regular) = {b}'
              '\nSize of One Exterior Angle (regular) = {c}\n'.format(
            a=total_size_of_interior_angles(shape_type),
            b=size_of_one_interior_angle(shape_type),
            c=size_of_one_exterior_angle(shape_type)
        ))
        option = input('Please enter another option : ')
    elif option == 'C':

