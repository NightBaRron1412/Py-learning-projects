'''
My First Self-Programmed Calculator
'''

def add():
    '''
    Performs sum calculation on entered numbers
    '''
    while True:
        try:
            first_num = float(input('\nEnter first number: '))
            second_num = float(input('Enter second number: '))
        except ValueError:
            print('\nOnly Numbers Are Allowed You Idiot !!\n')
            continue
        result = first_num+second_num
        return '\nThe result is ' + str(result)

def substract():
    '''
    Performs substract calculation on entered numbers
    '''
    while True:
        try:
            first_num = float(input('\nEnter first number: '))
            second_num = float(input('Enter second number: '))
        except ValueError:
            print('\nOnly Numbers Are Allowed You Idiot !!\n')
            continue
        result = first_num-second_num
        return '\nThe result is ' + str(result)

def multiplication():
    '''
    Performs multiplication calculation on entered numbers
    '''
    while True:
        try:
            first_num = float(input('\nEnter first number: '))
            second_num = float(input('Enter second number: '))
        except ValueError:
            print('\nOnly Numbers Are Allowed You Idiot !!\n')
            continue
        result = first_num*second_num
        return '\nThe result is ' + str(result)

def divion():
    '''
    Performs divion calculation on entered numbers
    '''
    while True:
        try:
            first_num = float(input('\nEnter first number: '))
            second_num = float(input('Enter second number: '))
        except ValueError:
            print('\nOnly Numbers Are Allowed You Idiot !!\n')
            continue
        try:
            result = first_num/second_num
        except ZeroDivisionError:
            print('\nYou Can\'t Divide on Zero You Piece Of Shit !!')
            continue
        return '\nThe result is ' + str(result)

def exponent():
    '''
    Performs exponential (power) calculation on entered numbers
    '''
    while True:
        try:
            first_num = float(input('\nEnter first number: '))
            second_num = float(input('Enter second number: '))
        except ValueError:
            print('\nOnly Numbers Are Allowed You Idiot !!\n')
            continue
        result = first_num**second_num
        return '\nThe result is ' + str(result)

class Rectangle():
    '''
    A square class that length an width as arrtibutes
    '''
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def circumference(self):
        '''Finds circumference of a shape'''
        result = 2*(self.length + self.length)
        return result

    def area(self):
        '''Finds area of a shape'''
        result = self.length * self.width
        return result

def rectangle():
    '''
    Performs rectangle calculations
    '''
    while True:
        print('\nFor Circumference enter "c"\nFor Area enter "a"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'a' and shape_options.lower() != 'c':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    length = float(input('\nEnter length: '))
                    width = float(input('Enter width: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                rectangle_shape = Rectangle(length, width)
                if shape_options.lower() == 'c':
                    return '\nThe result is ' + str(rectangle_shape.circumference())
                return '\nThe result is ' + str(rectangle_shape.area())

class Square():
    '''A square class that takes side length as an arrtibute'''
    def __init__(self, side):
        self.side = side

    def circumference(self):
        '''Finds circumference of a shape'''
        result = 4*(self.side)
        return result

    def area(self):
        '''Finds area of a shape'''
        result = self.side ** 2
        return result

def square():
    '''
    Performs square calculations
    '''
    while True:
        print('\nFor Circumference enter "c"\nFor Area enter "a"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'a' and shape_options.lower() != 'c':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    side_length = float(input('\nEnter side length: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                square_shape = Square(side_length)
                if shape_options.lower() == 'c':
                    return '\nThe result is ' + str(square_shape.circumference())
                return '\nThe result is ' + str(square_shape.area())

class Triangle():
    """A triangle class that takes sides lengths
    (1st side = b, 2nd side = h when calculating area) as arrtibutes"""
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def circumference(self):
        '''Finds circumference of a shape'''
        result = (self.first_side + self.second_side + self.third_side)
        return result

    def area(self):
        '''Finds area of a shape'''
        result = 0.5*self.first_side*self.second_side
        return result

def triangle():
    '''
    Performs triangle calculations
    '''
    while True:
        print('\nFor Circumference enter "c"\nFor Area enter "a"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'a' and shape_options.lower() != 'c':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    if shape_options.lower() == 'c':
                        first_side_len = float(input('\nEnter first side length: '))
                        second_side_len = float(input('Enter second side length: '))
                        third_side_len = float(input('Enter third side length: '))
                    else:
                        first_side_len = float(input('\nEnter base length: '))
                        second_side_len = float(input('Enter height: '))
                        third_side_len = 1.0
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                triangle_shape = Triangle(first_side_len, second_side_len, third_side_len)
                if shape_options.lower() == 'c':
                    return '\nThe result is ' + str(triangle_shape.circumference())
                return '\nThe result is ' + str(triangle_shape.area())

class Trapezoid():
    """A trapezoid class that takes sides and bases lengths
    (1st side = h when calculating area) as arrtibutes"""
    def __init__(self, first_side, second_side, first_base, second_base):
        self.first_side = first_side
        self.second_side = second_side
        self.first_base = first_base
        self.second_base = second_base

    def circumference(self):
        '''Finds circumference of a shape'''
        result = (self.first_side + self.first_base + self.second_side + self.second_base)
        return result

    def area(self):
        '''Finds area of a shape'''
        result = 0.5*self.first_side*(self.first_base+self.second_base)
        return result

def trapezoid():
    '''
    Performs trapezoid calculations
    '''
    while True:
        print('\nFor Circumference enter "c"\nFor Area enter "a"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'a' and shape_options.lower() != 'c':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    if shape_options.lower() == 'c':
                        first_side_len = float(input('\nEnter first side length: '))
                        second_side_len = float(input('Enter second side length: '))
                        first_base_len = float(input('Enter first base length: '))
                        second_base_len = float(input('Enter second base length: '))
                    else:
                        first_side_len = float(input('\nEnter height: '))
                        second_side_len = 1.0
                        first_base_len = float(input('\nEnter first base length: '))
                        second_base_len = float(input('Enter second base length: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                trapezoid_shape = Trapezoid(first_side_len, second_side_len, first_base_len, second_base_len) # pylint: disable=line-too-long
                if shape_options.lower() == 'c':
                    return '\nThe result is ' + str(trapezoid_shape.circumference())
                return '\nThe result is ' + str(trapezoid_shape.area())

class IsoscelesTrapezoid():
    """An isosceles trapezoid class that takes sides and bases lengths
    (sides = h when calculating area) as arrtibutes"""
    def __init__(self, sides, first_base, second_base):
        self.sides = sides
        self.first_base = first_base
        self.second_base = second_base

    def circumference(self):
        '''Finds circumference of a shape'''
        result = (2*self.sides + self.first_base + self.second_base)
        return result

    def area(self):
        '''Finds area of a shape'''
        result = 0.5*self.sides*(self.first_base+self.second_base)
        return result

def isosceles_trapezoid():
    '''
    Performs isosceles trapezoid calculations
    '''
    while True:
        print('\nFor Circumference enter "c"\nFor Area enter "a"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'a' and shape_options.lower() != 'c':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    if shape_options.lower() == 'c':
                        sides = float(input('\nEnter sides length: '))
                        first_base_len = float(input('Enter first base length: '))
                        second_base_len = float(input('Enter second base length: '))
                    else:
                        sides = float(input('\nEnter height: '))
                        first_base_len = float(input('\nEnter first base length: '))
                        second_base_len = float(input('Enter second base length: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                isosceles_trapezoid_shape = IsoscelesTrapezoid(sides, first_base_len, second_base_len) # pylint: disable=line-too-long
                if shape_options.lower() == 'c':
                    return '\nThe result is ' + str(isosceles_trapezoid_shape.circumference())
                return '\nThe result is ' + str(isosceles_trapezoid_shape.area())

class Cirlce():
    """A cicle class that takes radius as an arrtibute"""
    pi = 3.14159265359

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        '''Finds circumference of a shape'''
        result = (2*Cirlce.pi*self.radius)
        return result

    def area(self):
        '''Finds area of a shape'''
        result = Cirlce.pi*(self.radius**2)
        return result

def circle():
    '''
    Performs circle calculations
    '''
    while True:
        print('\nFor Circumference enter "c"\nFor Area enter "a"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'a' and shape_options.lower() != 'c':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    radius = float(input('\nEnter radius: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                circle_shape = Cirlce(radius)
                if shape_options.lower() == 'c':
                    return '\nThe result is ' + str(round(circle_shape.circumference(), 2))
                return '\nThe result is ' + str(round(circle_shape.area(), 2))

class Box():
    """A box class that takes length, width and height as arrtibutes"""
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        '''Finds surface area of a shape'''
        result = (2*self.length*self.width+2*self.length*self.height+2*self.width*self.height)
        return result

    def volume(self):
        '''Finds volume of a shape'''
        result = self.length*self.width*self.height
        return result

def box():
    '''
    Performs box calculations
    '''
    while True:
        print('\nFor Surface Area enter "sa"\nFor Volume enter "v"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'sa' and shape_options.lower() != 'v':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    length = float(input('\nEnter length: '))
                    width = float(input('Enter width: '))
                    height = float(input('Enter height: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                box_shape = Box(length, width, height)
                if shape_options.lower() == 'sa':
                    return '\nThe result is ' + str(box_shape.surface_area())
                return '\nThe result is ' + str(box_shape.volume())

class Sphere():
    """A sphere class that takes radius as an arrtibute"""
    pi = 3.14159265359
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        '''Finds surface area of a shape'''
        result = (4*Cirlce.pi*(self.radius**2))
        return result

    def volume(self):
        '''Finds volume of a shape'''
        result = (4/3)*Cirlce.pi*(self.radius**3)
        return result

def sphere():
    '''
    Performs sphere calculations
    '''
    while True:
        print('\nFor Surface Area enter "sa"\nFor Volume enter "v"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'sa' and shape_options.lower() != 'v':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    radius = float(input('\nEnter radius: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                sphere_shape = Sphere(radius)
                if shape_options.lower() == 'sa':
                    return '\nThe result is ' + str(round(sphere_shape.surface_area(), 2))
                return '\nThe result is ' + str(round(sphere_shape.volume(), 2))

class Cylinder():
    """A cylinder class that takes radius and height as arrtibutes"""
    pi = 3.14159265359
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        '''Finds surface area of a shape'''
        result = (2*Cirlce.pi*(self.radius)*(self.radius+self.height))
        return result

    def volume(self):
        '''Finds volume of a shape'''
        result = Cirlce.pi*(self.radius**2)*(self.height)
        return result

def cylinder():
    '''
    Performs cylinder calculations
    '''
    while True:
        print('\nFor Surface Area enter "sa"\nFor Volume enter "v"\n')
        shape_options = str(input(': '))
        if shape_options.lower() != 'sa' and shape_options.lower() != 'v':
            print('\nWrong Entry .. Please Read Instructions Above')
        else:
            while True:
                try:
                    radius = float(input('\nEnter radius: '))
                    height = float(input('Enter height: '))
                except ValueError:
                    print('\nOnly Numbers Are Allowed You Idiot !!\n')
                    continue
                cylinder_shape = Cylinder(radius, height)
                if shape_options.lower() == 'sa':
                    return '\nThe result is ' + str(round(cylinder_shape.surface_area(), 2))
                return '\nThe result is ' + str(round(cylinder_shape.volume(), 2))

while True:
    print('''
For Simple Calculations enter "simple"
For Two-Dimensional Shapes Calculations enter "2D"
For Three-Dimensional Shapes Calculations enter "3D"
To Exit enter "exit"
''')
    USER_INPUT1 = str(input(': '))

    if USER_INPUT1.lower() == 'simple':
        while True:
            print('''
For Addition enter "add" 
For Substract enter "substract" 
For Multiplication enter "multiply" 
For Divion enter "divide"
For Exponential enter "exponent"
For Previous Menu enter "back"
''')

    elif USER_INPUT1.lower() == '2d':
        while True:
            print('''
For Rectangle enter "rectangle" 
For Square enter "square" 
For Triangle enter "triangle" 
For Trapezoid enter "trapezoid"
For Isosceles Trapezoid  enter "isotrape"
For Cirlce enter "circle"
For Previous Menu enter "back"
''')
            USER_INPUT2 = str(input(': '))
            if USER_INPUT2 .lower() == 'rectangle':
                print(rectangle())
            elif USER_INPUT2 .lower() == 'square':
                print(square())
            elif USER_INPUT2 .lower() == 'triangle':
                print(triangle())
            elif USER_INPUT2 .lower() == 'trapezoid':
                print(trapezoid())
            elif USER_INPUT2 .lower() == 'isotrape':
                print(isosceles_trapezoid())
            elif USER_INPUT2 .lower() == 'circle':
                print(circle())
            elif USER_INPUT2 .lower() == 'back':
                break
            else:
                print('\nWrong Entry .. Please Read Instructions Above')

    elif USER_INPUT1.lower() == '3d':
        while True:
            print('''
For Box enter "box" 
For Sphere enter "sphere" 
For Cylinder enter "cylinder" 
For Previous Menu enter "back"
''')
            USER_INPUT2 = str(input(': '))
            if USER_INPUT2 .lower() == 'box':
                print(box())
            elif USER_INPUT2 .lower() == 'sphere':
                print(square())
            elif USER_INPUT2 .lower() == 'cylinder':
                print(cylinder())
            elif USER_INPUT2 .lower() == 'back':
                break
            else:
                print('\nWrong Entry .. Please Read Instructions Above')

    elif USER_INPUT1.lower() == 'exit':
        print('\nGoodBye Bitch !!\n')
        break

    else:
        print('\nWrong Entry .. Please Read Instructions Above')
