from tkinter import *
from tkinter import messagebox  # Para importar las ventanas emergentes

root = Tk()

root.title('Práctica Interfaces con BBDD')

root.iconbitmap("salto.ico")

root.geometry("650x500")  # Da un tamaño específico a la raíz

frame = Frame(root, width=600, height=450)
frame.pack()

ID = StringVar()
Name = StringVar()
Surname = StringVar()
Password = StringVar()
Address = StringVar()
Coments = StringVar()


"""----Blank Spaces to Write In (Entrys y Text para el Comentario)----"""


IDBlankSpace = Entry(frame, textvariable=ID)
IDBlankSpace.grid(row=0, column=1)

NameBlankSpace = Entry(frame, textvariable=Name)
NameBlankSpace.grid(row=1, column=1)

SurnameBlankSpace = Entry(frame, textvariable=Surname)
SurnameBlankSpace.grid(row=2, column=1)

PasswordBlankSpace = Entry(frame, textvariable=Password)
PasswordBlankSpace.grid(row=3, column=1)
PasswordBlankSpace.config(show='*')

AdressBlankSpace = Entry(frame, textvariable=Address)
AdressBlankSpace.grid(row=4, column=1)

ComentsText = Text(frame, width=16, height=5)
ComentsText.grid(row=5, column=1)


"""------------Labels-------------"""


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


"""----Scroll Bar for the Comment Section----"""


VertScrollBar = Scrollbar(frame, command=ComentsText.yview)
VertScrollBar.grid(row=5, column=2, sticky="nsew")  # Con este sticky se adapta al tamaño del cuadrito de texto

ComentsText.config(yscrollcommand=VertScrollBar.set)
# Para que el posicionador indique en to momento en que punto estas


"""----Menús y Ventanas----"""


menu_bar = Menu(root)  # Se hace en la raíz porque queda mejor, se puede en el frame también
root.config(menu=menu_bar, width=300, height=300)

bbdd_menu = Menu(menu_bar, tearoff=0)  # tearoff para quitar el separador que se pone al estar vacío
menu_bar.add_cascade(label='BBDD', menu=bbdd_menu)  # Necesario para que salga en la barra
bbdd_menu.add_command(label='Conectar')
bbdd_menu.add_separator()
bbdd_menu.add_command(label='Salir')

delete_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Delete', menu=delete_menu)
delete_menu.add_command(label='Borrar Campos')

crud_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='CRUD', menu=crud_menu)
crud_menu.add_command(label='Create')
crud_menu.add_command(label='Read')
crud_menu.add_command(label='Update')
crud_menu.add_command(label='Delete')

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Licencia')
help_menu.add_command(label='Acerca de')


root.mainloop()