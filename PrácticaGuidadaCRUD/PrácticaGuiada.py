from tkinter import *
from tkinter import messagebox  # Para importar las ventanas emergentes
import sqlite3

root = Tk()

root.title('Práctica Interfaces con BBDD')

root.iconbitmap("salto.ico")

root.geometry("650x500")  # Da un tamaño específico a la raíz

frame = Frame(root, width=600, height=450)
frame.pack()

conection = sqlite3.connect("Users")
cursor = conection.cursor()

ID = StringVar()
Name = StringVar()
Surname = StringVar()
Password = StringVar()
Address = StringVar()
Coments = StringVar()

"""----Blank Spaces to Write In (Entrys y Text para el Comentario)----------------------------------------------"""

IDBlankSpace = Entry(frame, textvariable=ID)
IDBlankSpace.grid(row=0, column=1)

NameBlankSpace = Entry(frame, textvariable=Name)
NameBlankSpace.grid(row=1, column=1)
NameBlankSpace.config(fg='green')

SurnameBlankSpace = Entry(frame, textvariable=Surname)
SurnameBlankSpace.grid(row=2, column=1)

PasswordBlankSpace = Entry(frame, textvariable=Password)
PasswordBlankSpace.grid(row=3, column=1)
PasswordBlankSpace.config(show='*')

AdressBlankSpace = Entry(frame, textvariable=Address)
AdressBlankSpace.grid(row=4, column=1)

ComentsText = Text(frame, width=16, height=5)
ComentsText.grid(row=5, column=1)

"""------------Labels------------------------------------------------------------------------------------------"""

IDLabel = Label(frame, text="ID:")
IDLabel.grid(row=0, column=0, padx=10, pady=10, sticky='e')
# Sticky para que se quede pegado en un lado u otro en vez del centro

NameLabel = Label(frame, text="Name:")
NameLabel.grid(row=1, column=0, padx=10, pady=10, sticky='e')

SurnameLabel = Label(frame, text="Surname:")
SurnameLabel.grid(row=2, column=0, padx=10, pady=10, sticky='e')

PasswordLabel = Label(frame, text="Password:")
PasswordLabel.grid(row=3, column=0, padx=10, pady=10, sticky='e')

AddressLabel = Label(frame, text="Adress:")
AddressLabel.grid(row=4, column=0, padx=10, pady=10, sticky='e')

ComentsLabel = Label(frame, text="Coments:")
ComentsLabel.grid(row=5, column=0, padx=10, pady=10, sticky='e')

"""----Scroll Bar for the Comment Section----------------------------------------------------------------------"""

VertScrollBar = Scrollbar(frame, command=ComentsText.yview)
VertScrollBar.grid(row=5, column=2, sticky="nsew")  # Con este sticky se adapta al tamaño del cuadrito de texto

ComentsText.config(yscrollcommand=VertScrollBar.set)
# Para que el posicionador indique en to momento en que punto estas


"""----Funciones para los Botones del Menú--------------------------------------------------------------------"""


def about():
    messagebox.showinfo('Práctica Guiada', 'Interface conected to a BBDD in 2022')


# Las funciones deben ir antes de crear to el menú para que se las pueda llamar correctamente --> flujo de ejecución


def licensex():
    messagebox.showwarning('License', 'Producto bajo licencia en Pycharm Student y Tkinter')


def exitx():
    exiting = messagebox.askquestion('Exit', 'Are you sure you want to exit the app?')

    if exiting == 'yes':
        root.destroy()


def deleteanswers():
    borro = messagebox.askquestion('Delete Answers', ' Are you sure you want to delete your answers?')
    if borro == 'yes':
        ID.set("")
        Name.set("")
        Surname.set("")
        Password.set("")
        Address.set("")
        ComentsText.delete(1.0, END)  # Para borrar los comentarios (de tipo Text() y elegimos de donde a donde borrar)


def conectarbase():
    global conection
    global cursor

    try:
        cursor.execute("""
        CREATE TABLE USERS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME VARCHAR (50),
        SURNAME VARCHAR (50),
        PASSWORD VARCHAR (50),
        ADRESS VARCHAR (50),
        COMENTS VARCHAR (100))
        """)

        messagebox.showinfo('BBDD', 'Database created succesfully')

    except:
        messagebox.showwarning('Warning!', 'The database already exists')


"""-------------------------------------OJOOOOOOOOOOO----------------------------------------------------------------"""

data = Name.get(), Surname.get(), Password.get(), Address.get(), ComentsText.get("1.0", END)


def crearbase():
    global conection
    global cursor
    global data
    data = Name.get(), Surname.get(), Password.get(), Address.get(), ComentsText.get("1.0", END)

    try:
        cursor.execute("INSERT INTO USERS VALUES (NULL,?,?,?,?,?)", data)
        #cursor.execute(" INSERT INTO USERS VALUES (NULL, '" + Name.get() +
        #               "','" + Surname.get() +
        #               "','" + Password.get() +
        #               "','" + Address.get() +
        #               "','" + ComentsText.get("1.0", END) + "')")

        conection.commit()
        messagebox.showinfo('BBDD', 'Register done correctly')
    except:
        messagebox.showwarning('Warning!', 'You may have written too many words, try again!')


def leerbase():
    global conection
    global cursor

    try:
        cursor.execute("SELECT * FROM USERS WHERE ID = ?", ID.get())
        userx = cursor.fetchall()
        print(userx)
        for i in userx:
            ID.set(i[0])
            Name.set(i[1])
            Surname.set(i[2])
            Password.set(i[3])
            Address.set(i[4])
            ComentsText.insert(1.0, i[5])

        conection.commit()
        messagebox.showinfo('BBDD', 'The Input is being Showed Successfully')

    except:
        messagebox.showwarning('Warning!', 'You have to write an ID number')


def actualizarbase():
    global conection
    global cursor
    global data

    try:
        cursor.execute("UPDATE USERS SET USER_NAME ='" + Name.get() +
                       "', SURNAME ='" + Surname.get() +
                       "', PASSWORD ='" + Password.get() +
                       "', ADRESS ='" + Address.get() +
                       "', COMENTS ='" + ComentsText.get("1.0", END) +
                       "' WHERE ID=" + ID.get())

        conection.commit()
        messagebox.showinfo('BBDD', 'The register has been updated successfully')

    except:
        messagebox.showwarning('Warning!', 'Write an ID number')


def borrarbase():
    global conection
    global cursor
    try:
        cursor.execute("DELETE FROM USERS WHERE ID = ?", ID.get())
        conection.commit()
        messagebox.showinfo('BBDD', 'Record Deleted Successfully')

    except:
        messagebox.showwarning('Warning!', 'You have to write an ID number')


"""----Menús y Ventanas-----------------------------------------------------------------------------------------"""

menu_bar = Menu(root)  # Se hace en la raíz porque queda mejor, se puede en el frame también
root.config(menu=menu_bar, width=300, height=300)

bbdd_menu = Menu(menu_bar, tearoff=0)  # tearoff para quitar el separador que se pone al estar vacío
menu_bar.add_cascade(label='BBDD', menu=bbdd_menu)  # Necesario para que salga en la barra
bbdd_menu.add_command(label='Connect', command=conectarbase)
bbdd_menu.add_separator()
bbdd_menu.add_command(label='Exit', command=exitx)

delete_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Delete', menu=delete_menu)
delete_menu.add_command(label='Delete Answers', command=deleteanswers)

crud_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='CRUD', menu=crud_menu)
crud_menu.add_command(label='Create', command=crearbase)
crud_menu.add_command(label='Read', command=leerbase)
crud_menu.add_command(label='Update', command=actualizarbase)
crud_menu.add_command(label='Delete', command=borrarbase)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='License', command=licensex)
help_menu.add_command(label='About...', command=about)

"""----Botones-----------------------------------------------------------------------------------------------"""

frame2 = Frame(root, width=100, height=100)
frame2.pack()

createbutton = Button(frame2, text="Create", command=crearbase)
createbutton.grid(row=0, column=0, padx=10, pady=15)

readbutton = Button(frame2, text="Read", command=leerbase)
readbutton.grid(row=0, column=1, padx=10, pady=15)

updatebutton = Button(frame2, text="Update", command=actualizarbase)
updatebutton.grid(row=0, column=2, padx=10, pady=15)

deletebutton = Button(frame2, text="Delete", command=borrarbase)
deletebutton.grid(row=0, column=3, padx=10, pady=15)

root.mainloop()
