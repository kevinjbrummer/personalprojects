def solve_sudoku(puzzle):
    given = []
    for x in range(len(puzzle)):
        for y in range(len(puzzle[x])):
            if puzzle[x][y] != 0:
                given.append((x,y))

    solved = False
    pos = (0,0)
    while solved == False:
        while pos in given:
            pos = advance_pos(pos)

        if pos[0] > 8:
            return puzzle


        if puzzle[pos[0]][pos[1]] == 0:
            for guess in range(1,11):

                if guess == 10:
                    pos = back_track(pos)
                    while pos in given:
                        pos = back_track(pos)
                elif check_pos(pos,guess,puzzle):
                    puzzle[pos[0]][pos[1]] = guess
                    pos = advance_pos(pos)
                    break


        elif pos[0] >=0:
            if puzzle[pos[0]][pos[1]] == 9:
                puzzle[pos[0]][pos[1]] = 0
                pos = back_track(pos)
                while pos in given:
                    pos = back_track(pos)

            else:
                new_guess = puzzle[pos[0]][pos[1]] + 1
                for guess in range(new_guess, 11):
                    if guess == 10:
                        puzzle[pos[0]][pos[1]] = 0
                        pos = back_track(pos)
                        while pos in given:
                            pos = back_track(pos)
                    elif check_pos(pos,guess,puzzle):
                        puzzle[pos[0]][pos[1]] = guess
                        pos = advance_pos(pos)
                        break
        if pos[0] < 0:
            break
    return None

def advance_pos(tuple):
    row = tuple[0]
    column = tuple[1]
    if column == 8:
        column = 0
        row += 1
    else:
        column += 1
    return (row, column)

def back_track(tuple):
    row = tuple[0]
    col = tuple[1]
    if col == 0:
        col = 8
        row -= 1
    else:
        col -= 1
    return (row, col)

def get_box(tuple):
    box = 0
    r = tuple[0]
    c = tuple[1]
    if r < 3 and c < 3:
        box = 0
    elif r < 3 and c >= 3 and c < 6:
        box = 1
    elif r < 3 and c >= 6:
        box = 2
    elif r >= 3 and r < 6 and c < 3:
        box = 3
    elif r >= 3 and r < 6 and c >= 3 and c < 6:
        box = 4
    elif r >= 3 and r < 6 and c >=6:
        box = 5
    elif r >= 6 and c < 3:
        box = 6
    elif r >= 6 and c >= 3 and c < 6:
        box = 7
    else:
        box = 8

    return box


def check_row(tuple, num, matrix):
    if num not in matrix[tuple[0]]:
        return True
    else:
        return False

def check_col(tuple, num, matrix):
    valid = True
    for i in range(len(matrix)):
        if num == matrix[i][tuple[1]]:
            valid = False
    return valid

def check_box(tuple, num, matrix):
    box = get_box(tuple)
    if box < 3:
        r_range = (0,3)
        c_range = (box * 3, box * 3 + 3)
    elif box >= 3 and box < 6:
        r_range = (3,6)
        c_range = ((box-3) * 3, (box-3) * 3 + 3)
    else:
        r_range = (6,9)
        c_range = ((box-6) * 3, (box-6) * 3 + 3)
    for r in range(r_range[0], r_range[1]):
        for c in range(c_range[0], c_range[1]):
            if num == matrix[r][c]:
                return False
    return True

def check_pos(tuple, guess, matrix):
    valid = False
    if (check_row(tuple, guess, matrix) and
        check_col(tuple, guess, matrix) and
            check_box(tuple, guess, matrix)):
        valid = True
    return valid


if __name__ == '__main__':

    puzzle = [[0, 3, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 4, 1, 0, 0, 7, 2, 5],
              [2, 7, 0, 0, 0, 0, 0, 0, 0],
              [0, 9, 2, 3, 0, 1, 8, 0, 0],
              [0, 0, 0, 0, 0, 4, 3, 0, 0],
              [0, 8, 0, 2, 0, 6, 0, 0, 9],
              [0, 0, 1, 0, 0, 0, 0, 6, 0],
              [9, 4, 8, 6, 0, 5, 0, 0, 0],
              [6, 0, 0, 0, 0, 2, 9, 8, 0]]

    puzzle = solve_sudoku(puzzle)

    for i in puzzle:
        print(i)






