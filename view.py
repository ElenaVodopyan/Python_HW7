import controller

def set_new_contact():
    elements = controller.get_elements()
    name = elements['name'].get()
    lastname = elements['lastname'].get()
    phonenumber = elements['phonenumber'].get()
    contact = f'{name} {lastname}: {phonenumber}'
    controller.add_to_listbox(contact)

def print_contacts_list(contacts_list):
    for contact in contacts_list:
        controller.add_to_listbox(contact[:-1])