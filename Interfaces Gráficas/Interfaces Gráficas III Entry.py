from tkinter import *

raiz = Tk()

frame = Frame(raiz, width=1200, height=600)
frame.pack()

nombre = StringVar()

cuadritodinombre = Entry(frame, textvariable=nombre)
# cuadritoditexto.place(x=100, y=100) Mejor con .grid()
cuadritodinombre.grid(row=0, column=1, padx=20, pady=20)
cuadritodinombre.config(fg='red', justify='center')  # Se nota al escribir

cuadritodiapellido = Entry(frame)
cuadritodiapellido.grid(row=1, column=1, padx=20, pady=20)
cuadritodinombre.config(fg='blue', justify='right')

cuadritodidireccion = Entry(frame)
cuadritodidireccion.grid(row=2, column=1, padx=20, pady=20)
cuadritodinombre.config(fg='yellow', justify='left')

"""----------------OJO----------"""

cuadritodipassword = Entry(frame)
cuadritodipassword.grid(row=3, column=1, padx=20, pady=20)
cuadritodipassword.config(show="*")

"""-------------------------------"""

labelNombre = Label(frame, text="Nombre: ")
# labelNombre.place(x=90, y=100)  # Aunque pongas la misma x que en el ENTRY te lo va a colocar uno al lao del otro
# labelNombre.place(x=100, y=100)  # Pero cuidado porque se puede suporponer, no es la mejor forma
labelNombre.grid(row=0, column=0, sticky='w', padx=10, pady=10)  # Nótese la diferencia con el padx

labelApellido = Label(frame, text="Apellido: ")
labelApellido.grid(row=1, column=0, sticky='e', padx=10, pady=10)

labelDireccion = Label(frame, text="Dirección: ")
labelDireccion.grid(row=2, column=0, sticky='e', padx=10, pady=10)

labelPassword = Label(frame, text="Password: ")
labelPassword.grid(row=3, column=0, padx=10, pady=10)

""" Parámetro sticky para que se queden los label en algún lado en vez de centrado (n,e,w,s) o (ne,nw,se,sw) """
""" Parámetro pady o padx para ajustar espacio de un contenedor o elemento a otro"""


""" Textos Largos y Buttons:"""

textoComents = Text(frame, width=16, height=5)
textoComents.grid(row=4, column=1, padx=20, pady=20)

labelComents = Label(frame, text="Coments: ")
labelComents.grid(row=4, column=0, sticky='e', padx=10, pady=10)

scrollVert = Scrollbar(frame, command=textoComents.yview)  # Barrita para subir y bajar en el cuadrito de texto
scrollVert.grid(row=4, column=2, sticky="nsew")  # Con este sticky se adapta al tamaño del cuadrito de texto

textoComents.config(yscrollcommand=scrollVert.set)  # Para que el posicionador indique en to momento en que punto estas


def funcionbotoncito():
    nombre.set("Manueh")  # 'nombre' hay que definirlo arriba por el flujo de ejecución
    # Al darle a enviar pone automaticamente el nombre 'Manueh'


botoncitoenvio = Button(raiz, text="Enviar", command=funcionbotoncito)
botoncitoenvio.pack()
# Si fuese en el frame y no en la raiz habría que usar .grid y meterlo en una row y col


raiz.mainloop()

"""--------------- FIN ---------------"""