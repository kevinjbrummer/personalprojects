import random
import sudoku_solver
import copy
import time


def sudoku_maker():
    puzzle = []
    for r in range(9):
        temp = []
        for c in range(9):
            temp.append(0)
        puzzle.append(temp)


    puzzle = middle_boxes(puzzle, 0)
    puzzle = sudoku_solver.solve_sudoku(puzzle)
    solution = copy.deepcopy(puzzle)

    removed = 0
    while removed < 46:
        r = random.randint(0,8)
        c = random.randint(0,8)
        while puzzle[r][c] == 0:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
        guess = random.randint(1,9)
        puzzle[r][c] = 0
        removed += 1

    test = copy.deepcopy(puzzle)

    unique = check_uniquieness(test)
    if not unique:
        sudoku_maker()
    return [puzzle, solution]

def middle_boxes(matrix, counter):
    if counter == 3:
        return matrix
    else:
        for r in range(counter * 3,counter * 3 +3):
            for c in range(counter * 3,counter * 3 + 3):
                pos = (r,c)
                while matrix[pos[0]][pos[1]] == 0:
                    guess = random.randint(1,9)
                    if sudoku_solver.check_pos(pos,guess, matrix):
                        matrix[pos[0]][pos[1]] = guess
        counter += 1
        return middle_boxes(matrix, counter)


def answers(puzzle, pos):
    guesses = []
    for i in range(1,10):
        if sudoku_solver.check_pos(pos, i, puzzle):
            guesses.append(i)
    return guesses

def check_uniquieness(puzzle):
    empty = []
    for x in range(len(puzzle)):
        for y in range(len(puzzle[x])):
            if puzzle[x][y] == 0:
                empty.append((x, y))

    while empty != []:
        for i in range(len(empty)):
            pos = empty[i]
            guesses = answers(puzzle, pos)
            if len(guesses) == 1:
                puzzle[pos[0]][pos[1]] = guesses[0]
                empty.pop(i)
                break
            elif len(empty) > 0 and empty[-1] == pos:
                return False
    return True






