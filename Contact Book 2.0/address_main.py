import pickle
import address_book_gui


def open_contact_file():
    file =open('contacts.pkl', 'rb')
    output = pickle.load(file)
    file.close()
    return output

def save(dictionary):
    file = open('contacts.pkl', 'wb')
    pickle.dump(dictionary, file)
    file.close()

def clear():
    save({})    


if __name__ == '__main__':
    address_book = address_book_gui.Address_Book_GUI(open_contact_file())

