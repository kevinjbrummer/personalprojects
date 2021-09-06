from tkinter import *
import tkinter
import address_book_gui
import address_main
from tkinter import messagebox

class Add_Contact():
    def __init__ (self, dictionary, root):
        self.dictionary = dictionary
        self.new_entry = {}
        self.entries = []
        self.variables = ['Name', 'Address 1', 'Address 2',
                'City', 'State', 'Zip Code',
                'Country', 'Home Phone', 'Cell Phone',
                'Email', 'Birthday', 'Notes']
        self.name = ''
        self.initialize(root)

    def initialize(self, root):
        self.root = tkinter.Toplevel(root)
        self.root.title('Add Contact')
        self.root.grid()
        for i in range(len(self.variables)):
            lbl = tkinter.Label(self.root, text=self.variables[i])
            lbl.grid(row=i, column=0)
            entry = tkinter.Entry(self.root)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        clsbtn = tkinter.Button(self.root,
                                text='Close',
                                command=self.root.destroy)
        clsbtn.grid(row=12, column=0)

        addbtn = tkinter.Button(self.root,
                                text='Add',
                                command = self.add)
        addbtn.grid(row=12, column=1)


    def add(self):
        if self.entries[0].get() == '':
            messagebox.showinfo('Error',
                                'Missing Required Information: Name')
            self.root.lift()
        elif self.entries[0].get() in self.dictionary.keys():
            messagebox.showinfo('Error',
                                'Name Already Registered')
            self.root.lift()
        else:
            temp_dict = {}
            for i in range(len(self.entries)):
                temp_dict.update({self.variables[i] : self.entries[i].get()})
            self.root.destroy()
            
