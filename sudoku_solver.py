def take_input():
    print('Enter the element of the sudoku row-wise : ')
    # taking sudoku grid input from the user
    for i in range(9):
        grid.append([int(y) for y in input('Enter the ' + str(i) + ' row : ').split()])


def print_board():
    print('\n----------------------------')
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print("| ", end=' ')
            print(grid[i][j], end=' ')
        if i % 3 == 2:
            print("|\n----------------------------")
        else:
            print("|")


def find_empty():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def row_check(row, val):
    for i in range(9):
        if grid[row][i] == val:
            return False
    return True


def col_check(row, val):
    for i in range(9):
        if grid[i][row] == val:
            return False
    return True


def box_check(r, c, val):
    for i in range(3):
        for j in range(3):
            if grid[i+r][j+c] == val:
                return False
    return True


def valid(val, pos):
    row, col = pos
    return row_check(row, val) and col_check(col, val) and box_check(int(row/3)*3, int(col/3)*3, val)


def solve():
    find = find_empty()
    if find is None:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(i, (row, col)):
            grid[row][col] = i
            if solve():
                return True
            grid[row][col] = 0
    return False


grid = []
take_input()
if solve():
    print('The solved sudoku is :\n')
    print_board()
else:
    print('The sudoku is invalid and can not be solved')
