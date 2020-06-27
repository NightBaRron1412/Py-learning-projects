'''
My First Self-Programmed Simple Stuff Calculator
'''

def add():
    '''
    Used to find the sum of two entered numbers
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
    Used to find the substract of two entered numbers
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
    Used to find the multiplication of two entered numbers
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
    Used to find the divion of two entered numbers
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

while True:

    print('''
For addition enter "add" 
For substract enter "substract" 
For multiply enter "multiply" 
For divion enter "divide"
    	''')
    USER_INPUT = str(input(': '))
    if USER_INPUT.lower() == 'add':
        print(add())
    elif USER_INPUT.lower() == 'substract':
        print(substract())
    elif USER_INPUT.lower() == 'multiply':
        print(multiplication())
    elif USER_INPUT.lower() == 'divide':
        print(divion())
    else:
        print('Wrong Entry .. Please Read Instructions Above')
