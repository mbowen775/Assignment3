# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    newString = ''

    for i in range(len(grid)):
        newString += str(grid[i][0])

    newString1 = '\n'
    for i in range(len(grid)):
        newString1 += str(grid[i][1])

    newString2 = '\n'
    for i in range(len(grid)):
        newString2 += str(grid[i][2])

    newString3 = '\n'
    for i in range(len(grid)):
        newString3 += str(grid[i][3])

    newString4 = '\n'
    for i in range(len(grid)):
        newString4 += str(grid[i][4])

    newString5 = '\n'
    for i in range(len(grid)):
        newString5 += str(grid[i][5])

    print(newString + newString1 + newString2 + newString3 + newString4 + newString5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
