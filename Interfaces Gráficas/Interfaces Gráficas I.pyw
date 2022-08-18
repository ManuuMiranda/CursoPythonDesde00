# Graphic User Interface (GUI)

"""
                 Estructura de Ventana con Tkinter:

Raíz (tk) o ventana con un frame dentro que organiza o aglutina los elementos o widgets (botones, cuadros de texto...)
                                                                                             (incluso un frame)
"""

"""                                   Empezamos:                                            """


from tkinter import *

raiz = Tk()

raiz.title("Ventana de Prueba")

raiz.resizable(1, 0)  # Sirve para que no podamos ampliar o disminuir el tamaño de la ventana, le damos uno predet
raiz.resizable(True, True)  # Admite 2 parámetros, width y height, booleanos o (1 o 0)

raiz.iconbitmap("salto.ico")  # Para añadir un icono a la interfaz, debe ser .ico

raiz.geometry("650x400")  # Para darle un tamañi en específico a la interfaz

raiz.config(bg="black")  # bg = background, así le ponemos un color al fondo

frame = Frame()

frame.pack()

frame.config(bg="red")

frame.config(width="650", height="350")

""" Packer Options: Para cambiar el comportamiento por defecto del frame al ampliar o disminuir la interfaz """

frame.pack(side="right")
frame.pack(side="right", anchor="n")  # Para usar 2 propiedades.
# frame.pack(fill="x")  # Para que se complete en el eje x
# frame.pack(fill="y", expand=True)  # Para que se complete el eje y
# frame.pack(fill="both", expand=True)  # Para que se complete en ambos ejes

""" También podemos cambiar las características del borde del frame o de la raíz """

frame.config(bd=25)
frame.config(relief="sunken")

""" También podemos cambiar como se ve el cursor cuando entramos en el frame o en la raíz """

frame.config(cursor="hand2")
frame.config(cursor="pirate")


raiz.mainloop()  # Necesario porque para que una ventana esté en ejecución debe de estar en una especie de bucle infinit
                 # Instrucción siempre al final

""" Para que se pueda abrir la ventana sin necesidad de usar la consola de python hay que cambiar el archivo a .pyw """


