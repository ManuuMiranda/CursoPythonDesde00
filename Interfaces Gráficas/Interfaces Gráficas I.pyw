# Graphic User Interface (GUI)

"""
                 Estructura de Ventana con Tkinter:

Raíz (tk) o ventana con un frame dentro que organiza o aglutina los elementos o widgets (botones, cuadros de texto...)
                                                                                             (incluso un frame)
"""

""" Empezamos: """


from tkinter import *

raiz = Tk()

raiz.title("Ventana de Prueba")

raiz.resizable(1, 0)  # Sirve para que no podamos ampliar o disminuir el tamaño de la ventana, le damos uno predet
                      # Admite 2 parámetros, width y height, booleanos (1 o 0)

raiz.iconbitmap("salto.ico")  # Para añadir un icono a la interfaz, debe ser .ico

raiz.geometry("650x400")  # Para darle un tamañi en específico a la interfaz

raiz.config(bg="black")  # bg = background, así le ponemos un color al fondo

raiz.mainloop()  # Necesario porque para que una ventana esté en ejecución debe de estar en una especie de bucle infinit
                 # Instrucción siempre al final

""" Para que se pueda abrir la ventana sin necesidad de usar la consola de python hay que cambiar el archivo a .pyw """