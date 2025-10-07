# First task

def print_head(hair, eye):
    hair = hair
    eye = eye
    full_hair = hair*12
    
    print(full_hair)
    print(hair + '|        |'+ hair)
    print(hair + '|  ' + eye + '  ' + eye + '  |' + hair)
    print(' |   /\   |' )
    print(' |        |' )
    print(' \  \'--\'  /')
    print('   ------')


# Second task

def print_body(height, arm):
    print('    XX')
    print('#' + arm * 4 + 'XX' + arm *4 +'#')
    for i in range(height):
        print('    XXXX')

# Third task 

def reverse_shoe(shoe_string):
    new_shoe_string = ''
    for i in shoe_string[::-1]:
        new_shoe_string = new_shoe_string + i
        
    return new_shoe_string

# Fourth task

def print_legs(height, shoe):
    rreverse_shoe = reverse_shoe(shoe)
    print('    ====')
    for i in range(height):
        print('   ||  ||')
    print(f' {shoe}  {rreverse_shoe}')

def main():
    print('Welcome to the custom character creator tool!')
    height = int(input('Overall character height: '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe = input('4-character string for the shoes: ')
    segment = (height - 11) // 2
    print()
    print_head(hair, eye)
    print_body(segment, arm)
    print_legs(segment, shoe)
