import model
import view
from tkinter import *
from tkinter import ttk

elements = {}

def add_contact():
    view.set_new_contact()

def add_to_listbox(contact):
    elements['contacts list'].insert(END, contact)
    send_contacts_list_to_model()

def delete_contact():
    elements['contacts list'].delete(elements['contacts list'].curselection()[0])
    send_contacts_list_to_model()

def send_contacts_list_to_model():
    contacts_list = elements['contacts list'].get(0, END)
    model.write_conacts(contacts_list)

def get_elements():
    return elements

def start():
    root = Tk()
    frm = ttk.Frame(root, padding = 20)
    frm.grid()

    Label(frm, text='Телефонный справочник').grid(row=0, column=0)

    Label(frm, text='Введите имя').grid(row=1, column=0)
    name_entry = Entry(frm)
    name_entry.grid(row=1, column=1)
    elements['name'] = name_entry

    Label(frm, text='Введите фамилию').grid(row=2, column=0)
    lastname_entry = Entry(frm)
    lastname_entry.grid(row=2, column=1)
    elements['lastname'] = lastname_entry

    Label(frm, text='Введите номер телефона').grid(row=3, column=0)
    phonenumber_entry = Entry(frm)
    phonenumber_entry.grid(row=3, column=1)
    elements['phonenumber'] = phonenumber_entry

    add_contact_btn = Button(frm, text='Добавить контакт', command=add_contact).grid(row=4, column=1)
    delete_contact_btn = Button(frm, text='Удалить контакт', command=delete_contact).grid(row=6, column=1)

    all_contacts = Listbox(frm, width=30, height=8)
    all_contacts.grid(row=6, column=0)
    elements['contacts list'] = all_contacts
    model.read_contacts()

    root.mainloop()