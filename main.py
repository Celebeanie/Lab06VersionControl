# Yaelsee Temes | 1716-5736

'''

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''

# function main that executes options based on user input
def main():
    global res


    while True:
        menu()
        option = int(input('Please enter an option: '))
        # encodes num
        if option == 1:
            num = input('Please enter your password to encode: ')
            encode(num)
            print('Your password has been encoded and stored!')
        # decodes num and prints original num and new num (now as res)
        elif option == 2:
            decode(num)
            print('The encoded password is ' + res + ', and the original password is ' + str(num) + '.')
        # exits code
        elif option == 3:
            exit()


# Variables that will be used to store user data in the following functions
res = []
result = []
num = ''

# Prints the menu
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

# Encodes user variable num
def encode(num):
    global res
    result = []

    x = list(num)

    # Extends variable list result with each number in num with +3. If a number in num is 7, 8, or 9 it will return 0, 1, or 2 respectively
    try:
        for char in num:
            if char == '9':
                result.extend([2])
            elif char == '8':
                result.extend([1])
            elif char == '7':
                result.extend([0])
            else:
                result.extend([int(char) + 3])

    except IndexError:
        pass
    # converts list back to string to print results
    result = '[%s]' % ', '.join(map(str, result))
    result = str(result)
    result = result.replace(', ', '')
    result = result.replace('[', '')
    result = result.replace(']', '')
    result = result.replace("'", '')
    res = result
    # print(res)
    return res, num

def decode(num):
    global res
    result = []

    x = list(num)

    # Extends variable list result with each number in num with -3. If a number in num is 0, 1, or 2 it will return 7, 8, or 9 respectively
    try:
        for char in num:
            if char == '2':
                result.extend([9])
            elif char == '1':
                result.extend([8])
            elif char == '0':
                result.extend([7])
            else:
                result.extend([int(char) - 3])

    except IndexError:
        pass
    # converts list back to string to print results
    result = '[%s]' % ', '.join(map(str, result))
    result = str(result)
    result = result.replace(', ', '')
    result = result.replace('[', '')
    result = result.replace(']', '')
    result = result.replace("'", '')
    res = res
    # print(res)
    return res, num

# runs function main()
if __name__ == '__main__':
    main()

