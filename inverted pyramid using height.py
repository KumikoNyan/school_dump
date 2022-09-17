# Inverted Pyramid where user_input = height

user_input = int(input("Height: "))

while user_input >= 1:
    value = user_input
    while value > 0:

        # to print out in horitzontal lines
        print(value, end='')
        value = value - 1
    user_input = user_input - 1
    print("")