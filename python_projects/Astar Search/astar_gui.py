import tkinter as tk
from tkinter import messagebox
import astar_grid


class Input:

    def __init__(self):
        self.start = None
        self.end = None
        self.show = False
        self.root = tk.Tk()
        self.setup()
        self.root.mainloop()


    def setup(self):
        global start_entry, end_entry, check

        start_label = tk.Label(self.root, text='Start Position')
        start_entry = tk.Entry(self.root)
        end_label = tk.Label(self.root, text='End Position')
        end_entry = tk.Entry(self.root)

        start_label.grid(row=0, column=0)
        start_entry.grid(row=0, column=1)

        end_label.grid(row=1, column=0)
        end_entry.grid(row=1, column=1)

        check=tk.IntVar()
        show_search = tk.Checkbutton(self.root, text='Show Search', variable=check)
        show_search.grid(row=2, columnspan=2)

        start_search = tk.Button(self.root, text='Start Search', command=self.start_button)
        start_search.grid(row=3, columnspan=2)

    def start_button(self):
        start_pos = start_entry.get()
        end_pos = end_entry.get()
        if start_pos == '' or end_pos == '':
            messagebox.showerror('Error', 'Empty Entry')
            return None
        start_pos = find_num(start_pos)
        end_pos = find_num(end_pos)
        if len(start_pos) != 2 or len(end_pos) != 2:
            messagebox.showerror('Error', '2 Inputs Required')
            return None
        elif (start_pos[0] < 0 or start_pos[0] > 49 or end_pos[0] < 0 or end_pos[0] > 49 or
              start_pos[1] < 0 or start_pos[1] > 49 or end_pos[1] < 0 or end_pos[1] > 49):
            messagebox.showerror('Error', 'Value is Too Large')
            return None
        else:
            self.start = (start_pos[0], start_pos[1])
            self.end = (end_pos[0], end_pos[1])
            if check.get() == 1:
                self.show = True
            else:
                self.show = False
            self.root.destroy()
            astar_grid.create_grid(self.start, self.end, self.show)





def find_num(string):
    inti = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numbers = []
    temp = ''
    for s in string:
        if s in inti:
            temp += s
        elif s == ',':
            numbers.append(int(temp))
            temp = ''
        else:
            continue
    numbers.append(int(temp))
    return numbers

if __name__ == '__main__':
    example = Input()