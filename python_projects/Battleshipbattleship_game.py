import random

def make_array():
    zero_array = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(0, 10):
        zero_array[i] = zero_array[i] + [0] * 10
    return zero_array

def ran_pos():
    ran_x = random.randint(0, 9)
    ran_y = random.randint(0, 9)
    ran_hv = random.randint(0,1)

    return [ran_x, ran_y, ran_hv]

def place_two(array):
    valid = False
    
    while not valid:
        pos = ran_pos()
        x = pos[0]
        y = pos[1]
        hv = pos[2]
        spot = array[y][x]
        
        if hv == 0:
            if x < 9 and (array[y][x] == 0 and array[y][x+1] == 0):
                array[y][x] = 'P'
                array[y][x+1] = 'P'
                valid = True
        elif hv == 1:
            if y < 9 and (array[y][x] == 0 and array[y+1][x] == 0):
                array[y][x] = 'P'
                array[y+1][x] = 'P'
                valid = True
    return array
        
    

def place_three_one(array):
    valid = False
    
    while not valid:
        pos = ran_pos()
        x = pos[0]
        y = pos[1]
        hv = pos[2]
        spot = array[y][x]
        
        if hv == 0:
            if x < 8 and (array[y][x] == 0 and array[y][x+1] == 0
                        and array[y][x+2] == 0):
                array[y][x] = 'S'
                array[y][x+1] ='S'
                array[y][x+2] = 'S'
                valid = True
        elif hv == 1:
            if y < 8 and (array[y][x] == 0 and array[y+1][x] == 0
                        and array[y+2][x] == 0):
                array[y][x] = 'S'
                array[y+1][x] = 'S'
                array[y+2][x] = 'S'
                valid = True
    return array

def place_three_two(array):
    valid = False
    
    while not valid:
        pos = ran_pos()
        x = pos[0]
        y = pos[1]
        hv = pos[2]
        spot = array[y][x]
        
        if hv == 0:
            if x < 8 and (array[y][x] == 0 and array[y][x+1] == 0
                        and array[y][x+2] == 0):
                array[y][x] = 'D'
                array[y][x+1] = 'D'
                array[y][x+2] = 'D'
                valid = True
        elif hv == 1:
            if y < 8 and (array[y][x] == 0 and array[y+1][x] == 0
                        and array[y+2][x] == 0):
                array[y][x] = 'D'
                array[y+1][x] = 'D'
                array[y+2][x] = 'D'
                valid = True
    return array

def place_four(array):
    valid = False
    
    while not valid:
        pos = ran_pos()
        x = pos[0]
        y = pos[1]
        hv = pos[2]
        spot = array[y][x]
        
        if hv == 0:
            if x < 7 and (array[y][x] == 0 and array[y][x+1] == 0
                        and array[y][x+2] == 0 and array[y][x+3] == 0):
                array[y][x] = 'B'
                array[y][x+1] = 'B'
                array[y][x+2] = 'B'
                array[y][x+3] = 'B'
                valid = True
        elif hv == 1:
            if y < 7 and (array[y][x] == 0 and array[y+1][x] == 0
                          and array[y+2][x] == 0 and array[y+3][x] == 0):
                array[y][x] = 'B'
                array[y+1][x] = 'B'
                array[y+2][x] = 'B'
                array[y+3][x] = 'B'
                valid = True
    return array

def place_five(array):
    valid = False
    
    while not valid:
        pos = ran_pos()
        x = pos[0]
        y = pos[1]
        hv = pos[2]
        spot = array[y][x]
        
        if hv == 0:
            if x < 6 and (array[y][x] == 0 and array[y][x+1] == 0
                        and array[y][x+2] == 0 and array[y][x+3] == 0
                        and array[y][x+4] == 0):
                array[y][x] = 'C'
                array[y][x+1] = 'C'
                array[y][x+2] = 'C'
                array[y][x+3] = 'C'
                array[y][x+4] = 'C'
                valid = True
        elif hv == 1:
            if y < 6 and (array[y][x] == 0 and array[y+1][x] == 0
                          and array[y+2][x] == 0 and array[y+3][x] == 0
                          and array[y+4][x] == 0):
                array[y][x] = 'C'
                array[y+1][x] = 'C'
                array[y+2][x] = 'C'
                array[y+3][x] = 'C'
                array[y+4][x] = 'C'
                valid = True
    return array

def place_ships(array):
    place_two(array)
    place_three_one(array)
    place_three_two(array)
    place_four(array)
    place_five(array)

def main():
    com_array = make_array()
    place_ships(com_array)
    return com_array

if __name__ == '__main__':
    print(main())

