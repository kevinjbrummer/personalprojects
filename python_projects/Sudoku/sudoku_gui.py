import pygame
import sys
import tkinter as tk
from tkinter import messagebox
import sudoku_maker

def sudoku_board():
    puzzle = sudoku_maker.sudoku_maker()
    solution = puzzle[1]
    puzzle = puzzle[0]
    pygame.init()
    grid = pygame.display.set_mode((450, 450))
    refresh_grid(grid, puzzle)
    FPS = pygame.time.Clock()
    FPS.tick()
    current = None
    root = tk.Tk()
    root.withdraw()
    play = True
    solved = False
    while play == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                x = int(pos[0]/50)
                y = int(pos[1]/50)
                if puzzle[y][x] == 0:
                    if current == None:
                        pygame.draw.polygon(grid, 'Pink', box((x,y)), width=4)
                        current = (x,y)
                    else:
                        refresh_grid(grid, puzzle)
                        pygame.draw.polygon(grid, 'Pink', box((x, y)), width=4)
                        current = (x, y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    add_number(grid, current, solution, puzzle, 1)
                elif event.key == pygame.K_2:
                    add_number(grid, current, solution, puzzle, 2)
                elif event.key == pygame.K_3:
                    add_number(grid, current, solution, puzzle, 3)
                elif event.key == pygame.K_4:
                    add_number(grid, current, solution, puzzle, 4)
                elif event.key == pygame.K_5:
                    add_number(grid, current, solution, puzzle, 5)
                elif event.key == pygame.K_6:
                    add_number(grid, current, solution, puzzle, 6)
                elif event.key == pygame.K_7:
                    add_number(grid, current, solution, puzzle, 7)
                elif event.key == pygame.K_8:
                    add_number(grid, current, solution, puzzle, 8)
                elif event.key == pygame.K_9:
                    add_number(grid, current, solution, puzzle, 9)
                elif event.key == pygame.K_RETURN:
                    refresh_grid(grid, solution)
                    solved = True

                if puzzle == solution:
                    solved = True

        pygame.display.update()
        if solved == True:
            play = messagebox.askyesno('Game Over', 'Play again?')
        if solved == True and play == True:
            puzzle = sudoku_maker.sudoku_maker()
            solution = puzzle[1]
            puzzle = puzzle[0]
            refresh_grid(grid, puzzle)
            solved = False

def add_number(grid, current, solution, puzzle, num):
    if solution[current[1]][current[0]] == num:
        puzzle[current[1]][current[0]] = num
        fill_num(num, grid, current)

def refresh_grid(grid, matrix):
    grid.fill('White')
    for i in range(0, 465, 50):
        if i % 150 == 0:
            pygame.draw.line(grid, 'Black', (i, 0), (i, 450), width=3)
            pygame.draw.line(grid, 'Black', (0, i), (450, i), width=3)
        else:
            pygame.draw.line(grid, 'Black', (i, 0), (i, 450))
            pygame.draw.line(grid, 'Black', (0, i), (450, i))
    num_font = pygame.font.Font('freesansbold.ttf', 30)
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] != 0:
                text = num_font.render(str(matrix[r][c]), True, 'Black')
                textRect = text.get_rect()
                textRect.center = (((c + 1) * 50) - 25, ((r + 1) * 50) - 25)
                grid.blit(text, textRect)

def fill_num(number, grid, pos):
    num_font = pygame.font.Font('freesansbold.ttf', 30)
    text = num_font.render(str(number), True, 'Black')
    textRect = text.get_rect()
    textRect.center = (((pos[0] + 1) * 50) - 25, ((pos[1] + 1) * 50) - 25)
    grid.blit(text, textRect)

def box(tuple):
    x = tuple[0]
    y = tuple[1]
    new_tuple = [(x * 50, y * 50),
                (x * 50 + 50, y * 50),
                (x * 50 + 50, y* 50 + 50),
                (x * 50, y* 50 + 50)]
    return new_tuple


