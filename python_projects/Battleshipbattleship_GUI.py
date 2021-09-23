from tkinter import*
import random
import battleship_game

cell_size = 45
remaining_ships = 5

def setup():
    global root,com_map, com_array
    global status_label, win_label, frame, carrier_label
    global battleship_label, destroyer_label, submarine_label
    global patrol_boat_label

    root = Tk()
    root.title('Battleship')
    root.attributes('-fullscreen', True)
    bg_color = 'ghost white'
    root.configure(background=bg_color)
    


    com_array = battleship_game.main()    
    

    com_map = make_map()
    make_grid(com_map)
    com_map.bind('<Button-1>', com_grid_handler)

    status_label = Label(root, font=('', 35), text='', bg=bg_color)
    status_label.grid(row=0, column=2, rowspan=5, padx=10)

    
    carrier_label = Label(root, font=('', 35), text='Carrier',
                          bg=bg_color)
    carrier_label.grid(row=0, column=0)
    
    battleship_label = Label(root, font=('', 35), text='Battleship',
                             bg=bg_color)
    battleship_label.grid(row=1, column=0)
    
    destroyer_label = Label(root, font=('', 35), text='Destroyer',
                            bg=bg_color)
    destroyer_label.grid(row=2, column=0)
    
    submarine_label = Label(root, font=('', 35), text='Submarine',
                            bg=bg_color)
    submarine_label.grid(row=3, column=0)
    
    patrol_boat_label = Label(root, font=('', 35), text='Patrol Boat',
                            bg=bg_color)
    patrol_boat_label.grid(row=4, column=0)
    

    win_label = Label(root, font=('', 50), text='YOU WIN!', bg=bg_color)

    for col in range(0,3):
        root.grid_columnconfigure(col, minsize=450)
    for row in range(0,5):
        root.grid_rowconfigure(row, minsize = 200)
        

    com_map.grid(row=0, column=1, rowspan=10, padx=5, pady=5)

    root.bind('<Return>', stop)


def stop(event):
    root.destroy()

def make_grid(plane):
    global cell_size
    for i in range(1, 10):
        plane.create_line(i*cell_size, 0, i*cell_size, 10*cell_size)
        plane.create_line(0, i*cell_size, 10*cell_size, i*cell_size)
    
def make_map():
    return Canvas(root, width=450, height=450,
                        borderwidth=0,
                        highlightthickness=0,
                        bg='dodgerblue')


def com_grid_handler(event):
    global com_map, remaining_ships
    
    x = int(event.x/cell_size)
    y = int(event.y/cell_size)

    if com_array[y][x] == 0:
        make_x(x, y, 'black', com_map)
        com_array[y][x] = 'X'
        status_label.configure(text= 'Miss!')
    elif com_array[y][x] == 'X':
        status_label.configure(text= 'You already shot\n here!')
    else:
        make_x(x, y, 'red', com_map)
        ship = com_array[y][x]
        com_array[y][x] = 'X'
        destroyed = count_ships(ship)
        if destroyed:
            if ship == 'P':
                status_label.configure(text= 'You sunk my\n patrol boat!')
                patrol_boat_label.configure(text=
                                            strike('Patrol boat'))
            elif ship == 'D':
                status_label.configure(text= 'You sunk my\n destroyer!')
                destroyer_label.configure(text=
                                            strike('Destroyer'))
            elif ship == 'S':
                status_label.configure(text= 'You sunk my\n submarine!')
                submarine_label.configure(text=
                                            strike('Submarine'))
            elif ship == 'C':
                status_label.configure(text= 'You sunk my\n carrier')
                carrier_label.configure(text=
                                            strike('Carrier'))
            elif ship == 'B':
                status_label.configure(text= 'You sunk my\n battleship!')
                battleship_label.configure(text=
                                            strike('Battleship'))
                
            remaining_ships = remaining_ships-1
            if remaining_ships == 0:
                win()
        else:
            status_label.configure(text= 'Hit!')

def fill_square(row, column, color, grid):
    grid.create_rectangle(row*cell_size, column*cell_size,
                               row*cell_size + cell_size,
                                column*cell_size +cell_size,
                               fill=color, outline='black')

def make_x(x, y, color, grid):
    grid.create_line(x*cell_size,
                     y*cell_size,
                     x*cell_size + cell_size,
                     y*cell_size + cell_size, width = 5, fill = color)
    
    grid.create_line(x*cell_size+ cell_size,
                     y*cell_size,
                     x*cell_size,
                     y*cell_size + cell_size, width = 5, fill=color)

def count_ships(boat):
    destroyed = 0
    for i in range(0, 10):
        if boat in com_array[i]:
            destroyed = destroyed + 1
    if destroyed == 0:
        return True
    else:
        return False

def win():
    clear()
    win_label.pack(pady = 450)
    
def clear():
    list = root.grid_slaves()
    for l in list:
        l.grid_remove()
    

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

        
    
    

    
setup()
root.mainloop()
