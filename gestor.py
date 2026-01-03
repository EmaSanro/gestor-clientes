from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Gestor de clientes')

conex = sqlite3.connect('crm.db')

cursor = conex.cursor()

cursor.execute("""
    CREATE TABLE if not exists cliente(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL,
        empresa TEXT NOT NULL
    );
""")

def render_clientes():
    clientes = cursor.execute("SELECT * FROM cliente").fetchall()

    tree.delete(*tree.get_children())

    for cliente in clientes:
        tree.insert('', END, cliente[0], values=(cliente[1], cliente[2], cliente[3]))

def insertar(cliente):
    cursor.execute("""
        INSERT INTO cliente(nombre, telefono, empresa) VALUES(?,?,?)
    """, (cliente['nombre'], cliente['telefono'], cliente['empresa']))
    conex.commit()
    render_clientes()

def obtener(cliente):
    clientes = cursor.execute("SELECT * FROM cliente WHERE nombre LIKE ?", (f"%{cliente}%",)).fetchall()
    tree.delete(*tree.get_children())
    print(clientes)

    for cliente in clientes:
        tree.insert('', END, cliente[0], values=(cliente[1], cliente[2], cliente[3]))

def buscar_cliente():
    def buscar():
        if not name.get():
            messagebox.showerror(title="Advertencia", message="Tienes que ingresar el nombre del cliente a buscar")
            return
        cliente = name.get().capitalize()
        obtener(cliente)
        window.destroy()
        
        
    window = Toplevel()
    window.title("Buscar Cliente")
    window.geometry("300x100")

    lname = Label(window, text="Nombre cliente")
    lname.pack()

    name = Entry(window, width=40)
    name.pack()

    search = Button(window, text="Buscar", command=buscar)
    search.pack()
    window.mainloop()

def agregar_cliente():
    def agregar():

        if not name.get():
            messagebox.showerror(title='Advertencia', message='El campo del nombre es obligatorio!')
            return
        elif not tel.get():
            messagebox.showerror(title='Advertencia', message='El campo del telefono es obligatorio!')
            return
        elif not emp.get():
            messagebox.showerror(title='Advertencia', message='El campo de la empresa es obligatorio!')
            return
            
        cliente = {
            'nombre' : name.get().title(),
            'telefono' : tel.get(),
            'empresa' : emp.get().title()
        }

        insertar(cliente)
        window.destroy()

    window = Toplevel()
    window.title('Agregar Cliente')
    window.geometry('300x200')

    lname = Label(window, text='Nombre')
    lname.pack()
    vcmd = root.register(solo_letras)
    name = Entry(window, width=40, validate="key", validatecommand=(vcmd, '%S'))
    name.bind('<Return>', lambda event: agregar())
    name.pack()
    
    ltel = Label(window, text='Telefono')
    ltel.pack()
    vcmd = root.register(solo_numeros)
    tel = Entry(window, width=40, validate="key", validatecommand=(vcmd, '%S'))
    tel.bind('<Return>', lambda event: agregar())
    tel.pack()
    
    lemp = Label(window, text='Empresa')
    lemp.pack()
    emp = Entry(window, width=40)
    emp.bind('<Return>', lambda event: agregar())
    emp.pack()

    submit = Button(window, text='Agregar', width=20, command=agregar)
    submit.pack(pady=10)


    name.focus()
    window.mainloop()

def eliminar_cliente():
    selections = tree.selection()
    confirm = messagebox.askokcancel(title='Eliminar Cliente', message='Estas seguro que deseas eliminar este/os cliente/s?')
    if confirm:
        for selection in selections:
            cursor.execute("DELETE FROM cliente WHERE id = ?", (selection, ))
        conex.commit()
        render_clientes()

def solo_numeros(caracter):
    return caracter.isdigit()

def solo_letras(caracter):
    return caracter.isalpha() or caracter == " "

btnAgregar = Button(root, text='Agregar cliente', command=agregar_cliente)
btnAgregar.grid(row=0,column=0, padx=10, pady=10)

btnEliminar = Button(root, text='Eliminar cliente', command=eliminar_cliente)
btnEliminar.grid(row=0, column=1, padx=10, pady=10)

btnBuscar = Button(root, text="Buscar cliente", command=buscar_cliente)
btnBuscar.grid(row=0, column=2, padx=10, pady=10)

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')

tree.column('#0', width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('#0')
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(row=1, column=0, columnspan=3)

render_clientes()

root.mainloop()