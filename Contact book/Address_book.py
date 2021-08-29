from tkinter import *
import tkinter
import pickle
import os

class Address_book():
    def __init__(self):
        self.initialize()
    #create the main address book window
    def initialize(self):
        
        #First, initialize a tkinter window
        self.root = tkinter.Tk()
        self.root.title('Address Book')
        self.root.grid()
        
        #Next, set up a list box to hold all of the contact names
        self.contacts = tkinter.Listbox(self.root, height=40, width=30)
        self.contacts.grid(rowspan=12, column=0)
        self.contacts.bind('<<ListboxSelect>>', self.display_contact)

        #Set up labels and label frames for all the variables
        #in the address book
        self.name_var = StringVar()
        name1 = tkinter.LabelFrame(self.root, text='Name')
        name1.grid(row=0, column=1)
        name2 = tkinter.Label(name1, textvariable=self.name_var)
        name2.pack()

        self.address1_var = StringVar()
        address1_1 = tkinter.LabelFrame(self.root, text='Address 1')
        address1_1.grid(row=1, column=1)
        address1_2 = tkinter.Label(address1_1, textvariable=self.address1_var)
        address1_2.pack()

        self.address2_var = StringVar()
        address2_1 = tkinter.LabelFrame(self.root, text='Address 2')
        address2_1.grid(row=2, column=1)
        address2_2 = tkinter.Label(address2_1, textvariable=self.address2_var)
        address2_2.pack()

        self.city_var = StringVar()
        city1 = tkinter.LabelFrame(self.root, text='City')
        city1.grid(row=3, column=1)
        city2 = tkinter.Label(city1, textvariable=self.city_var)
        city2.pack()

        self.state_var = StringVar()
        state1 = tkinter.LabelFrame(self.root, text='State')
        state1.grid(row=4, column=1)
        state2 = tkinter.Label(state1, textvariable=self.state_var)
        state2.pack()
        
        self.country_var = StringVar()
        country1 = tkinter.LabelFrame(self.root, text='Country')
        country1.grid(row=5, column=1)
        country2 = tkinter.Label(country1, textvariable=self.country_var)
        country2.pack()

        self.zip_var = StringVar()
        zip1 = tkinter.LabelFrame(self.root, text='Zip Code')
        zip1.grid(row=6, column=1)
        zip2 = tkinter.Label(zip1, textvariable=self.zip_var)
        zip2.pack()

        self.home_var = StringVar()
        home1 = tkinter.LabelFrame(self.root, text='Home Phone')
        home1.grid(row=7, column=1)
        home2 = tkinter.Label(home1, textvariable=self.home_var)
        home2.pack()

        self.cell_var = StringVar()
        cell1 = tkinter.LabelFrame(self.root, text='Cell Phone')
        cell1.grid(row=8, column=1)
        cell2 = tkinter.Label(cell1, textvariable=self.cell_var)
        cell2.pack()

        self.email_var = StringVar()
        email1 = tkinter.LabelFrame(self.root, text='Email')
        email1.grid(row=9, column=1)
        email2 = tkinter.Label(cell1, textvariable=self.email_var)
        email2.pack()

        self.bday_var = StringVar()
        bday1 = tkinter.LabelFrame(self.root, text='Birthday')
        bday1.grid(row=10, column=1)
        bday2 = tkinter.Label(bday1, textvariable=self.bday_var)
        bday2.pack()

        self.notes_var = StringVar()
        notes1 = tkinter.LabelFrame(self.root, text='Notes')
        notes1.grid(row=11, column=1)
        notes2 = tkinter.Label(notes1, textvariable=self.notes_var)
        notes2.pack()
        
        #Create the close button and the add button
        closebtn = tkinter.Button(self.root,
                                  text='Close',
                                  command = self.root.destroy)
        closebtn.grid(row=12, column=0)
        
        addbtn = tkinter.Button(self.root,
                                text='Add',
                                command=self.add_contact)
        addbtn.grid(row=12, column=1)

        #Open a pickle file to read the dictionary containing
        #the address book information
        #The saved dictionary is a nested dictionary
        file = open('contacts.pkl', 'rb')
        output = pickle.load(file)
        self.contact_dict = output
        file.close()

        #add the saved data to the listbox
        for i in self.contact_dict:
            self.contacts.insert(END, self.contact_dict[i]['Name'])

        

        self.root.mainloop()

    #funtion to add a contact to the main window's list box
    def add_contact(self):
        
        #initialize the window
        self.add_root = tkinter.Tk()
        self.add_root.grid()

        #Add all the labels and entry boxes for the address book variables
        namelbl = Label(self.add_root, text='Name:')
        namelbl.grid(row=0, column=0)
        self.name = Entry(self.add_root)
        self.name.grid(row=0, column=1)

        address1lbl = Label(self.add_root, text='Address1:')
        address1lbl.grid(row=1, column=0)
        self.address1 = Entry(self.add_root)
        self.address1.grid(row=1, column=1)

        address2lbl = Label(self.add_root, text='Address2:')
        address2lbl.grid(row=2, column=0)
        self.address2 = Entry(self.add_root)
        self.address2.grid(row=2, column=1)

        citylbl = Label(self.add_root, text='City:')
        citylbl.grid(row=3, column=0)
        self.city = Entry(self.add_root)
        self.city.grid(row=3, column=1)

        statelbl = Label(self.add_root, text='State:')
        statelbl.grid(row=4, column=0)
        self.state = Entry(self.add_root)
        self.state.grid(row=4, column=1)

        countrylbl = Label(self.add_root, text='Country:')
        countrylbl.grid(row=5, column=0)
        self.country = Entry(self.add_root)
        self.country.grid(row=5, column=1)

        ziplbl = Label(self.add_root, text='Zip Code:')
        ziplbl.grid(row=6, column=0)
        self.zip = Entry(self.add_root)
        self.zip.grid(row=6, column=1)

        homelbl = Label(self.add_root, text='Home Phone:')
        homelbl.grid(row=7, column=0)
        self.home = Entry(self.add_root)
        self.home.grid(row=7, column=1)

        celllbl = Label(self.add_root, text='Cell Phone:')
        celllbl.grid(row=8, column=0)
        self.cell = Entry(self.add_root)
        self.cell.grid(row=8, column=1)

        emaillbl = Label(self.add_root, text='Email:')
        emaillbl.grid(row=9, column=0)
        self.email = Entry(self.add_root)
        self.email.grid(row=9, column=1)

        bdaylbl = Label(self.add_root, text='Birthday:')
        bdaylbl.grid(row=10, column=0)
        self.bday = Entry(self.add_root)
        self.bday.grid(row=10, column=1)

        noteslbl = Label(self.add_root, text='Notes:')
        noteslbl.grid(row=11, column=0)
        self.notes = Entry(self.add_root)
        self.notes.grid(row=11, column=1)

        #add the close button and the add button
        closebtn = tkinter.Button(self.add_root,
                                  text='Close',
                                  command = self.add_root.destroy)
        closebtn.grid(row=12, column=0)

        addbtn = tkinter.Button(self.add_root,
                                text='Add',
                                command=self.update_list)
        addbtn.grid(row=12, column=1)

        self.add_root.mainloop()

    #this function creates a temporary dictionary to store the inputted
    #data fro the add window. Then it updates the saved list with the new
    #contact. Finally, it writes the new information to the saved pickle file
    def update_list(self):
        temp_contact = {'Name':self.name.get(),
                        'Address1':self.address1.get(),
                        'Address2':self.address2.get(),
                        'City':self.city.get(),
                        'State':self.state.get(),
                        'Country':self.country.get(),
                        'Zip Code':self.zip.get(),
                        'Home Phone':self.home.get(),
                        'Cell Phone':self.cell.get(),
                        'Email':self.email.get(),
                        'Birthday':self.bday.get(),
                        'Notes':self.notes.get()}
        self.contact_dict.update({self.name.get():temp_contact})
        self.contacts.insert(END, self.contact_dict[self.name.get()]['Name'] )
        self.add_root.destroy()
        contact_file = open('contacts.pkl', 'wb')
        pickle.dump(self.contact_dict, contact_file)
        contact_file.close()

    #When an item in the listbox is selected, this funtion will display all
    #of the information to the right of the listbox on the main window.
    def display_contact(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.name_var.set(self.contact_dict[data]['Name'])
            self.address1_var.set(self.contact_dict[data]['Address1'])
            self.address2_var.set(self.contact_dict[data]['Address2'])
            self.city_var.set(self.contact_dict[data]['City'])
            self.state_var.set(self.contact_dict[data]['State'])
            self.country_var.set(self.contact_dict[data]['Country'])
            self.zip_var.set(self.contact_dict[data]['Zip Code'])
            self.home_var.set(self.contact_dict[data]['Home Phone'])
            self.cell_var.set(self.contact_dict[data]['Cell Phone'])
            self.email_var.set(self.contact_dict[data]['Email'])
            self.bday_var.set(self.contact_dict[data]['Birthday'])
            self.notes_var.set(self.contact_dict[data]['Notes'])

        else:
            self.name_var.set('')
        
        


if __name__ == '__main__':
    book = Address_book()
