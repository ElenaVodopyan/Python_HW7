import view

def write_conacts(contacts_list):
    data = open('phone_numbers.txt', mode='w', encoding='utf-8')
    for contact in contacts_list:
        data.writelines(contact + '\n')
    data.close()

def read_contacts():
    data = open('phone_numbers.txt', mode='r', encoding='utf-8')
    cotacts_list = data.readlines()
    view.print_contacts_list(cotacts_list)
    data.close() 