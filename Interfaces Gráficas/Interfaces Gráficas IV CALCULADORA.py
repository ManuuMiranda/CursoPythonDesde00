from tkinter import *

raiz = Tk()

frame = Frame(raiz)

frame.pack()

operacion = ""
resultado = 0

"""------Pantalla------"""

numPantalla = StringVar()

entrypantalla = Entry(frame, textvariable=numPantalla)
entrypantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)  # Columnspan pa que se ajuste a botones, ocupará 4c
entrypantalla.config(background='black', fg='blue', justify='right')

"""------Funciones/Pulsaciones para el Teclado-----------"""


def numPulsado(num):
    global operacion
    if operacion != "":
        numPantalla.set(num)
        operacion = ""
    else:
        numPantalla.set(numPantalla.get() + num)


"""-----------------Función Suma-------------------------"""


def suma(num):
    global operacion
    global resultado
    operacion = "suma"
    resultado += float(num)  # IGUAL QUE PONER: resultado = resultado + int(num)
    numPantalla.set(resultado)


"""------------Función para dar el Resultado--------------"""


def igual():
    global resultado
    numPantalla.set(float(numPantalla.get())+resultado)
    resultado = 0



"""------Botones 1--------"""

boton7 = Button(frame, text='7', width=3, command=lambda: numPulsado('7'))
boton7.grid(row=2, column=1)
boton8 = Button(frame, text='8', width=3, command=lambda: numPulsado('8'))
boton8.grid(row=2, column=2)
boton9 = Button(frame, text='9', width=3, command=lambda: numPulsado('9'))
boton9.grid(row=2, column=3)
botondiv = Button(frame, text='/', width=3)
botondiv.grid(row=2, column=4)

"""------Botones 2--------"""

boton4 = Button(frame, text='4', width=3, command=lambda: numPulsado('4'))
boton4.grid(row=3, column=1)
boton5 = Button(frame, text='5', width=3, command=lambda: numPulsado('5'))
boton5.grid(row=3, column=2)
boton6 = Button(frame, text='6', width=3, command=lambda: numPulsado('6'))
boton6.grid(row=3, column=3)
botonx = Button(frame, text='X', width=3)
botonx.grid(row=3, column=4)

"""------Botones 3--------"""

boton1 = Button(frame, text='1', width=3, command=lambda: numPulsado('1'))
boton1.grid(row=4, column=1)
boton2 = Button(frame, text='2', width=3, command=lambda: numPulsado('2'))
boton2.grid(row=4, column=2)
boton3 = Button(frame, text='3', width=3, command=lambda: numPulsado('3'))
boton3.grid(row=4, column=3)
botonrest = Button(frame, text='-', width=3)
botonrest.grid(row=4, column=4)

"""------Botones 4-------"""

botoncoma = Button(frame, text=',', width=3, command=lambda: numPulsado(','))
botoncoma.grid(row=5, column=1)
boton0 = Button(frame, text='0', width=3, command=lambda: numPulsado('0'))
boton0.grid(row=5, column=2)
botonigual = Button(frame, text='=', width=3, command=lambda: igual())
botonigual.grid(row=5, column=3)
botonmas = Button(frame, text='+', width=3, command=lambda: suma(numPantalla.get()))
botonmas.grid(row=5, column=4)

raiz.mainloop()
