def board(arr):
    for i in range(9):

        if i % 3 == 0:
            print("+", end="")
            print("-------+" * 3)

        for j in range(9):
            if j % 3 == 0:
                print("", end="| ")
            print(arr[i][j], end=" ")

        print("", end="|")
        print()

    print("+", end="")
    print("-------+" * 3)


def check_col(arr, num, col):
    if all([num != arr[i][col] for i in range(9)]):
        return True
    return False


def check_row(arr, num, row):
    if all([num != arr[row][i] for i in range(9)]):
        return True
    return False


def check_cell(arr, num, row, col):
    sectopx = 3 * (row // 3)
    sectopy = 3 * (col // 3)

    for i in range(sectopx, sectopx + 3):
        for j in range(sectopy, sectopy + 3):
            if arr[i][j] == num:
                return True
    return False


def empty_loc(arr, l):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def sudoku(arr):
    l = [0, 0]

    if not empty_loc(arr, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if check_row(arr, num, row) and check_col(arr, num, col) and not check_cell(arr, num, row, col):
            arr[row][col] = num

            if (sudoku(arr)):
                return True

            # failure, unmake & try again
            arr[row][col] = 0

    return False


# Driver main function to test above functions
if __name__ == "__main__":

    # creating a 2D array for the grid
    grid = [[0 for x in range(9)] for y in range(9)]

    # assigning values to the grid
    grid = [[1, 0, 0, 0, 5, 0, 7, 0, 2],
            [0, 0, 0, 6, 0, 3, 0, 0, 8],
            [0, 7, 6, 0, 1, 0, 3, 0, 0],
            [0, 4, 0, 3, 0, 7, 0, 5, 0],
            [8, 1, 0, 0, 6, 0, 4, 0, 7],
            [0, 9, 0, 0, 0, 5, 0, 0, 0],
            [2, 6, 0, 0, 0, 0, 8, 0, 5],
            [9, 0, 0, 8, 0, 1, 0, 0, 0],
            [0, 0, 3, 0, 9, 0, 0, 2, 0]]

    # if success print the solution
    if (sudoku(grid)):
        board(grid)
    else:
        print("There is no solution")

