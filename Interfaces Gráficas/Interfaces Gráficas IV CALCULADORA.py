from tkinter import *

raiz = Tk()

frame = Frame(raiz)

frame.pack()

operacion = ""

resultado = 0

resetearPantalla = False

"""------Pantalla------"""

numPantalla = StringVar()

entrypantalla = Entry(frame, textvariable=numPantalla)
entrypantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)  # Columnspan pa que se ajuste a botones, ocupará 4c
entrypantalla.config(background='black', fg='blue', justify='right')

"""------Funciones/Pulsaciones para el Teclado-----------"""


def numPulsado(num):
    global operacion
    global resetearPantalla

    if resetearPantalla:  # Si no se pone nada lo toma como True
        numPantalla.set(num)
        resetearPantalla = False
    else:
        numPantalla.set(numPantalla.get() + num)


"""-----------------Función Suma-------------------------"""


def suma(num):
    global operacion
    global resultado
    global resetearPantalla
    operacion = "suma"
    resultado += float(num)
    # IGUAL QUE PONER: resultado = resultado + float(num)
    numPantalla.set(resultado)
    resetearPantalla = True


"""----------------Función Resta------------------"""
num1 = 0
cont_resta = 0


def resta(num):
    global operacion
    global resultado
    global resetearPantalla
    global num1
    global cont_resta

    if cont_resta == 0:
        num1 = float(num)
        resultado = num1
    else:
        if cont_resta == 1:
            resultado = num1 - float(num)
        else:
            resultado = float(resultado) - float(num)

        numPantalla.set(resultado)
        resultado = numPantalla.get()

    cont_resta = cont_resta + 1
    operacion = "resta"
    resetearPantalla = True


"""--------------Función Multiplicación-------------------"""


cont_multi = 0


def multiplicacion(num):
    global operacion
    global resultado
    global resetearPantalla
    global num1
    global cont_multi

    if cont_multi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if cont_multi == 1:
            resultado = num1 * float(num)
        else:
            resultado = float(resultado) * float(num)

        numPantalla.set(resultado)
        resultado = numPantalla.get()

    cont_multi = cont_multi+1
    operacion = "multiplicacion"
    resetearPantalla = True


"""------------------Función División---------------------"""


cont_divi = 0


def division(num):
    global operacion
    global resultado
    global resetearPantalla
    global cont_divi
    global num1

    if cont_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if cont_divi == 1:
            resultado = num1/float(num)
        else:
            resultado = float(resultado)/float(num)

        numPantalla.set(resultado)
        resultado = numPantalla.get()

    cont_divi = cont_divi+1
    operacion = "division"
    resetearPantalla = True


"""------------Función para dar el Resultado--------------"""


def igual():
    global resultado
    global operacion
    global cont_divi
    global cont_multi
    global cont_resta

    if operacion == "suma":
        numPantalla.set(resultado + float(numPantalla.get()))
        # Debe salir lo que hay almacenado en resultado más lo que esté ahora en pantalla (último número que se suma)
        resultado = 0

    elif operacion == "resta":
        numPantalla.set(float(resultado) - float(numPantalla.get()))
        resultado = 0
        cont_resta = 0

    elif operacion == "multiplicacion":
        numPantalla.set(float(resultado) * float(numPantalla.get()))
        resultado = 0
        cont_multi = 0

    elif operacion == "division":
        numPantalla.set(float(resultado) / float(numPantalla.get()))
        resultado = 0
        cont_divi = 0


"""------Botones 1--------"""


boton7 = Button(frame, text='7', width=3, command=lambda: numPulsado('7'))
boton7.grid(row=2, column=1)

boton8 = Button(frame, text='8', width=3, command=lambda: numPulsado('8'))
boton8.grid(row=2, column=2)

boton9 = Button(frame, text='9', width=3, command=lambda: numPulsado('9'))
boton9.grid(row=2, column=3)

botondiv = Button(frame, text='/', width=3, command=lambda: division(numPantalla.get()))
botondiv.grid(row=2, column=4)


"""------Botones 2--------"""


boton4 = Button(frame, text='4', width=3, command=lambda: numPulsado('4'))
boton4.grid(row=3, column=1)

boton5 = Button(frame, text='5', width=3, command=lambda: numPulsado('5'))
boton5.grid(row=3, column=2)

boton6 = Button(frame, text='6', width=3, command=lambda: numPulsado('6'))
boton6.grid(row=3, column=3)

botonx = Button(frame, text='X', width=3, command=lambda: multiplicacion(numPantalla.get()))
botonx.grid(row=3, column=4)


"""------Botones 3--------"""


boton1 = Button(frame, text='1', width=3, command=lambda: numPulsado('1'))
boton1.grid(row=4, column=1)

boton2 = Button(frame, text='2', width=3, command=lambda: numPulsado('2'))
boton2.grid(row=4, column=2)

boton3 = Button(frame, text='3', width=3, command=lambda: numPulsado('3'))
boton3.grid(row=4, column=3)

botonrest = Button(frame, text='-', width=3, command=lambda: resta(numPantalla.get()))
botonrest.grid(row=4, column=4)

"""------Botones 4-------"""

botonpunto = Button(frame, text='.', width=3, command=lambda: numPulsado('.'))
botonpunto.grid(row=5, column=1)

boton0 = Button(frame, text='0', width=3, command=lambda: numPulsado('0'))
boton0.grid(row=5, column=2)

botonigual = Button(frame, text='=', width=3, command=lambda: igual())
botonigual.grid(row=5, column=3)

botonmas = Button(frame, text='+', width=3, command=lambda: suma(numPantalla.get()))
botonmas.grid(row=5, column=4)


raiz.mainloop()
