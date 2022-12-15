from contactos_view import ContactosView, ContactoNuevo

class ContactosController(object):
    def __init__(self, repo, view):
        self.view = view
        self.selection = None
        self.repo = repo
        self.contacts = list(repo.get_contacts())

    def create_contact(self):
        print('Nuevo contacto')
        nuevo_contacto = ContactoNuevo(self.view).show()
        if nuevo_contacto:
            contact = self.repo.add_contact(nuevo_contacto)
            self.contacts.append(contact)
            self.view.add_contact(contact)

    def start(self):
        for c in self.contacts:
            self.view.add_contact(c)
        self.view.mainloop()

    def select_contact(self, index):
        print('Seleccionar contacto')
        self.selection = index
        contact = self.contacts[index]
        self.view.load_details(contact)

    def update_contact(self):
        if not self.selection:
            return
        rowid = self.contacts[self.selection].rowid
        updated_contact = self.view.get_data()
        updated_contact.rowid = rowid
        contact = self.repo.update_contact(updated_contact)
        self.contacts[self.selection] = contact
        self.view.update_contact(contact, self.selection)
        print('Actualizar contacto')

    def delete_contact(self):
        if not self.selection:
            return
        contact = self.contacts[self.selection]
        self.repo.delete_contact(contact)
        self.view.remove_contact(self.selection)
        print('Eliminar contacto')