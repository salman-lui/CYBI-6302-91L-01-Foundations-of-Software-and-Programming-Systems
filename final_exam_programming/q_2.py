# Author: Md Salman Rahman


def main():
    keyboard_input = int(input("Please enter an integer between 1 and 10: "))
    while (keyboard_input < 1 or keyboard_input > 10):
        print("The integer from the user is not between 1 and 10")
        keyboard_input = int(input("Please enter another integer between 1 and 10: "))

    print(str(keyboard_input) + "'s Multiplication Table")
    print("--------------------")
    for i in range(1, 11):
        output = i * keyboard_input
        print(str(i) + " x " + str(keyboard_input) + " = " + str(output))
    print("--------------------")


# Call the main function.
if __name__ == '__main__':
    main()