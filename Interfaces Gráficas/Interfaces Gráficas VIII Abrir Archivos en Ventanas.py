from tkinter import *
from tkinter import filedialog

root = Tk()


def abre_fichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:\\",
                                         filetypes=(("Ficheros de Excel", "*.xlsx"),
                                                    ("Ficheros de Texto", "*.txt"),
                                                    ("Todos los Ficheros", "*.*")))
    # initialdir para elegir por qué directorio se empieza a mirar (C: en vez de Documentos que es por defecto)

    print(fichero)  # imprime la ruta del archivo que queremos abrir


Button(root, text="Abrir fichero", command=abre_fichero).pack()





root.mainloop()