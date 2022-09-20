from tkinter import *
from tkinter import messagebox  # Para importar las ventanas emergentes

root = Tk()


def info_adicional():
    messagebox.showinfo("Procesador de Manuel", "Procesador de textos version 2022")


def aviso_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")


def salir_aplicacion():
    #valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?") OPCIÓN 1
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")  # OPCIÓN 2

    #if valor == "yes":  OPCIÓN 1
        #root.destroy()

    if valor:  # OPCIÓN 2
        root.destroy()


def cerrar_documento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar, documento bloqueado")
    # True = Si pulsa 'Reintentar' y False = si pulsa 'Cancelar'

    #if valor == False:
        #root.destroy()

    if not valor:
        root.destroy()


barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

archivo_menu = Menu(barra_menu, tearoff=0)  # tearoff para quitar el separador que se pone al estar vacío
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar como")
archivo_menu.add_separator()  # Para añadir un separador
archivo_menu.add_command(label="Cerrar", command=cerrar_documento)
archivo_menu.add_command(label="Salir", command=salir_aplicacion)

archivo_edicion = Menu(barra_menu, tearoff=0)
archivo_edicion.add_command(label="Copiar")
archivo_edicion.add_command(label="Cortar")
archivo_edicion.add_command(label="Pegar")

archivo_herramientas = Menu(barra_menu)

archivo_ayuda = Menu(barra_menu, tearoff=0)
archivo_ayuda.add_command(label="Licencia", command=aviso_licencia)
archivo_ayuda.add_command(label="Acerca de", command=info_adicional)



barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edición", menu=archivo_edicion)
barra_menu.add_cascade(label="Herramientas", menu=archivo_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=archivo_ayuda)

root.mainloop()