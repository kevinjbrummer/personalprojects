from tkinter import *
import tkinter
import address_main
import pickle
from tkinter import messagebox

class Address_Book_GUI():
    def __init__ (self, dictionary):
        self.dictionary = dictionary
        self.variables = ['Name', 'Address 1', 'Address 2',
                'City', 'State', 'Zip Code',
                'Country', 'Home Phone', 'Cell Phone',
                'Email', 'Birthday', 'Notes']
        self.entries = []
        self.open_gui()

    def open_gui(self):
        self.root = tkinter.Tk()
        self.root.title('Address Book')
        self.root.grid()

        self.contacts = tkinter.Listbox(self.root,
                                        height=40,
                                        width=30)
        self.contacts.grid(rowspan=24,
                          column=1,
                           columnspan=3)
        for i in self.dictionary:
            self.contacts.insert(END, self.dictionary[i]['Name'])
            self.sort_contacts()
        self.contacts.bind('<<ListboxSelect>>', self.display_contact)

        temp = 0
        for i in self.variables:
            lbl = tkinter.Label(self.root, text=i)
            lbl.grid(row=temp, column=0)
            temp = temp + 2
            
        temp = 1
        for i in range(len(self.variables)):
            entry = tkinter.Entry(self.root, state=DISABLED)
            entry.grid(row=temp, column=0)
            temp = temp + 2
            self.entries.append(entry)

        clsbtn = tkinter.Button(self.root,
                                text='Close',
                                command=self.root.destroy)
        clsbtn.grid(row=24, column=0)

        addbtn = tkinter.Button(self.root,
                                text='Add',
                                     command=self.add_contact)
        addbtn.grid(row=24, column=1)

        delbtn = tkinter.Button(self.root,
                                text='Delete',
                                command=self.del_contact)
        delbtn.grid(row=24, column=2)

        editbtn = tkinter.Button(self.root,
                                 text='Edit',
                                 command = self.edit_contact)
        editbtn.grid(row=24, column=3)

        self.root.mainloop()

    def display_contact(self, event):
        if self.contacts.size() != 0:
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                data = event.widget.get(index)
                for i in range(len(self.dictionary[data])):
                    self.entries[i].config(state='normal')
                    self.entries[i].delete(0, END)
                    self.entries[i].insert(0,
                                           self.dictionary[data][self.variables[i]])
                    self.entries[i].config(state='disable')
            else:
                for i in range(len(self.entries)):
                    self.entries[i].config(state='normal')
                    self.entries[i].delete(0, END)
                    self.entries[i].config(state='disable')

    def del_contact(self):
        selection = self.contacts.curselection()
        if selection:
            index = selection[0]
            data = self.contacts.get(index)
            self.contacts.delete(index)
            del self.dictionary[data]
            address_main.save(self.dictionary)
        else:
            messagebox.showinfo('Error',
                                'No Contact Selected')

    def add_contact(self):
        self.add_window()
       
    def update_dict(self, item):
        self.dictionary.update(item)
        address_main.save(self.dictionary)

    def update_list(self, name):
        self.contacts.insert(END, name)


    def add_window(self):
        entries = []
        root = tkinter.Toplevel(self.root)
        root.title('Add Contact')
        root.grid()
        for i in range(len(self.variables)):
            lbl = tkinter.Label(root, text=self.variables[i])
            lbl.grid(row=i, column=0)
            entry = tkinter.Entry(root)
            entry.grid(row=i, column=1)
            entries.append(entry)

        clsbtn = tkinter.Button(root,
                                text='Close',
                                command=root.destroy)
        clsbtn.grid(row=12, column=0)

        addbtn = tkinter.Button(root,
                                text='Add',
                                command = lambda: self.add_button(root,
                                                                  entries))
        addbtn.grid(row=12, column=1)


    def add_button(self, root, entries):
        if entries[0].get() == '':
            messagebox.showinfo('Error',
                                'Missing Required Information: Name')
            root.lift()
        elif entries[0].get() in self.dictionary.keys():
            messagebox.showinfo('Error',
                                'Name Already Registered')
            root.lift()
        else:
            temp_dict = {}
            for i in range(len(entries)):
                temp_dict.update({self.variables[i] : entries[i].get()})
            root.destroy()
            self.update_list(temp_dict['Name'])
            self.update_dict({temp_dict['Name'] : temp_dict})
            self.sort_contacts()

    def edit_contact(self):
        selection = self.contacts.curselection()
        if selection:
            index = selection[0]
            data = self.contacts.get(index)
            self.edit_window(data)
        else:
            messagebox.showinfo('Error',
                                'No Contact Selected')

    def edit_window(self, data):
        root = tkinter.Toplevel(self.root)
        root.title('Add Contact')
        root.grid()
        entries = []
        for i in range(len(self.variables)):
            lbl = tkinter.Label(root, text=self.variables[i])
            lbl.grid(row=i, column=0)
            entry = tkinter.Entry(root)
            entry.insert(0, self.dictionary[data][self.variables[i]])
            entry.grid(row=i, column=1)
            entries.append(entry)
            

        clsbtn = tkinter.Button(root,
                                text='Close',
                                command=root.destroy)
        clsbtn.grid(row=12, column=0)

        cnfbtn = tkinter.Button(root,
                                text='Confirm',
                                command = lambda:
                                self.confirm_edit(root, entries, data))
        cnfbtn.grid(row=12, column=1)

    def confirm_edit(self, root, entries, old_name):
        del self.dictionary[old_name]
        for i in range(self.contacts.size()):
            if self.contacts.get(i) == old_name:
                self.contacts.delete(i)
        self.add_button(root, entries)

    def sort_contacts(self):
        contact_list = []
        for i in range(self.contacts.size()):
            contact_list.append(self.contacts.get(0))
            self.contacts.delete(0)
        contact_list.sort()
        for i in range(len(contact_list)):
           self.contacts.insert(END, contact_list[i])
        



    


        
    
            
        
        
