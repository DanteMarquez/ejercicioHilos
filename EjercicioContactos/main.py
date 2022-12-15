import sqlite3
from contactos_view import ContactosView, ContactoNuevo
from contactos_controller import ContactosController
from contactos_repositorio import ContactsRepository

def main():
    with sqlite3.connect('contactos.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contacts' ''')
        if c.fetchone()[0]==1: 
            print('Tabla ya existe')
            repo = ContactsRepository(conn)
            view = ContactosView()
            controller = ContactosController(repo, view)
            view.set_controller(controller)
            controller.start()
        else:
            c.execute('''CREATE TABLE contacts(
                last_name TEXT,
                first_name TEXT,
                email TEXT,
                phone TEXT
            )''')
            print('Tabla creada')

if __name__ == '__main__':
    main()