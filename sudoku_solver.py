class sudoku:
    def __init__(self):
        self.grid = []

    # function to take the input and form the grid
    def take_input(self):
        print('Enter the element of the sudoku row-wise : ')
        # taking sudoku grid input from the user
        for i in range(9):
            self.grid.append([int(y) for y in input('Enter the ' + str(i) + ' row : ').split()])

    # function to print the board
    def print_board(self):
        print('\n-------------------------')
        for i in range(9):
            for j in range(9):
                if j % 3 == 0:
                    print("|", end=' ')
                print(self.grid[i][j], end=' ')
            if i % 3 == 2:
                print("|\n-------------------------")
            else:
                print("|")

    # function to find a empty box in the sudoku
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    # function to check whether the value 'val' is already present in the row or not
    def row_check(self, row, val):
        for i in range(9):
            if self.grid[row][i] == val:
                return False
        return True

    # function to check whether the value 'val' is already present in the column or not
    def col_check(self, row, val):
        for i in range(9):
            if self.grid[i][row] == val:
                return False
        return True

    # function to check whether the value 'val' is already present in the 3x3 box or not
    def box_check(self, r, c, val):
        for i in range(3):
            for j in range(3):
                if self.grid[i+r][j+c] == val:
                    return False
        return True

    # function to check whether the value 'val' can be placed in the position 'pos' or not
    def valid(self, val, pos):
        row, col = pos
        return self.row_check(row, val) and self.col_check(col, val) and self.box_check(int(row/3)*3, int(col/3)*3, val)

    # function to solve the sudoku
    def solve(self):
        find = self.find_empty()
        if find is None:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(i, (row, col)):
                self.grid[row][col] = i
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False

    def __del__(self):
        del self.grid


s = sudoku()
s.take_input()
if s.solve():
    print('The solved sudoku is :\n')
    s.print_board()
else:
    print('The sudoku is invalid and can not be solved')
