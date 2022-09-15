from tkinter import *

# Son como los Radiobuttons (redondos) pero se puede escoger más de una opción a la vez

root = Tk()

root.title("Ejemplito")

playa = IntVar()
montana = IntVar()
ciudad = IntVar()


def opciones_destinos():
    opcion_escogida = ""

    if playa.get() == 1:
        opcion_escogida += " playa"
    if montana.get() == 1:
        opcion_escogida += " montaña"
    if ciudad.get() == 1:
        opcion_escogida += " ciudad"

    textofinal.config(text=opcion_escogida)


foto = PhotoImage(file="Certificado Data Science en R.png")  # Pongo esa foto por poner algo, es muy grande
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Destinos:", width=80).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opciones_destinos).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opciones_destinos).pack()
Checkbutton(frame, text="Ciudad", variable=ciudad, onvalue=1, offvalue=0, command=opciones_destinos).pack()

textofinal = Label(frame)
textofinal.pack()


root.mainloop()