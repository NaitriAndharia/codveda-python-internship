
def print_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def is_safe(board, row, col, n):

    # Check upper column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


# Main Program
n = int(input("Enter number of Queens: "))

if n <= 0:
    print("Please enter a positive number.")

else:
    board = [[0 for col in range(n)] for row in range(n)]

    if solve_n_queens(board, 0, n):
        print("\nSolution Found!\n")
        print_board(board, n)
    else:
        print("No solution exists.")
