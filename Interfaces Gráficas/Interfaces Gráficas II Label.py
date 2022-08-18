from tkinter import *

root = Tk()

frame = Frame(root, width=500, height=400)

frame.pack()

label = Label(frame, text="TusMuertos")
label.place(x=50, y=150)

imagen = PhotoImage(file="Label y Entry Parametros Tipicos.png")
Label(frame, image=imagen).place(x=0, y=50)

""" También se puede hacer sin poner variables: """

Label(frame, text="TusMuertos", fg="blue", font=("Comic Sans MS", 18)).place(x=75, y=175)

root.mainloop()