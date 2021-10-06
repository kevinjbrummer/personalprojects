import sys
import astar_search
import pygame
import time

def create_grid(start, end, show=False):
    matrix = []
    for i in range(50):
        temp = []
        for j in range(50):
            temp.append(0)
        matrix.append(temp)
    matrix[start[1]][start[0]] = 'S'
    matrix[end[1]][end[0]] = 'E'
    pygame.init()
    grid = pygame.display.set_mode((500, 550))
    pygame.draw.polygon(grid, 'Pink', box(start))
    pygame.draw.polygon(grid, 'Pink', box(end))
    for i in range(0,510, 10):
        pygame.draw.line(grid, 'White', (i, 0), (i, 500))
        pygame.draw.line(grid, 'White', (0, i), (500, i))
        FPS = pygame.time.Clock()
        FPS.tick()
        found = False

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if ((event.type == pygame.MOUSEMOTION and event.buttons[0]) or
                event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                new_pos = (int(pos[0]/10), int(pos[1]/10))
                if (new_pos[1] < 50 and matrix[new_pos[0]][new_pos[1]] == 0 and
                    new_pos != start and new_pos != end):
                    pygame.draw.polygon(grid, 'White', box(new_pos))
                    pygame.draw.polygon(grid, 'Black', box(new_pos), width=2)
                    matrix[new_pos[0]][new_pos[1]] = 1

            if event.type == pygame.KEYUP:
                start_time = time.time()
                route = astar_search.astar_search(start, end, matrix, grid, show)
                end_time = time.time() - start_time
                if route != None:
                    for xy in route:
                        pygame.draw.polygon(grid, 'Pink ', box(xy))
                    font = pygame.font.Font('freesansbold.ttf', 10)
                    text = font.render('Goal found in %f seconds' % (end_time), True, 'White')
                    textRect = text.get_rect()
                    textRect.center = (250, 525)
                    grid.blit(text, textRect)


        pygame.display.update()

def box(tuple):
    x = tuple[0]
    y = tuple[1]
    new_tuple = [(x * 10, y * 10),
                (x * 10 + 10, y * 10),
                (x * 10 + 10, y* 10 + 10),
                (x * 10, y* 10 + 10)]
    return new_tuple
if __name__ == '__main__':
    create_grid((3,0), (45,10))