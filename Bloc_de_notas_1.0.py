from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

def acopiar ():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())
def apegar():
    editor.insert(INSERT, editor.clipboard_get())
def acortar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())
    editor.delete("sel.first", "sle.last")
def adeshacer():
    editor.edit_undo()
def arehacer():
    editor.edit_redo()
def anuevo():
    editor.delete(1.0,END)
def aabrir():
    documento = askopenfile(filetypes=[("Archivo de texto","*.txt")])
    if documento != None:
        editor.insert(1.0, documento.read())
def aguardar():
    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])
    print(documento.weite(editor.get(1.0, END)))
def aacerca():
    messagebox.showinfo("Acerca de Bloc de notas", "Bloc de notas es un lector de archivos de texto plano,"
    "creado por Eduardo Gil Reyes como un proyecto de Python, "
    "realizar una aplicación de este tipo ayuda al estudiante a practicar"
    "el uso de interfaces gr+aficas, la manipulación de archivos de texto"
    "y algunas funciones extra."
    "\n\n"
    "A pesar de ser sencillo tenemos 2 funcionalidades que no tiene el"
    "bloc de notas de Windows, la primera es la opción de rehacer,"
    "la segunda caracteristica es que se puede deshacer o rehacer tantas veces"
    "como se desee a diferencia del cloc de notas de Windows que solo permite"
    "dehacer 2 veces y la segunda cuenta como un rehacer.")

if __name__ == "__main__":

    ventana = Tk()

    menubar = Menu(ventana)
    archivo = Menu(menubar, tearoff=0)
    archivo.add_command(label="Nuevo    ", command=anuevo)
    archivo.add_command(label="Abrir    ", command=aabrir)
    archivo.add_command(label="Guardar  ",command=aguardar)
    archivo.add_command(label="Salir    ", command=ventana.quit)
    menubar.add_cascade(label="Archivo", menu=archivo)

    editar = Menu(menubar, tearoff=0)
    editar.add_command(label="Deshacer  ", command=adeshacer)
    editar.add_command(label="Rehacer  ", command=arehacer)
    editar.add_separator()
    editar.add_command(label="Copiar  ", command=acopiar)
    editar.add_command(label="Pegar  ", command=apegar)
    editar.add_command(label="Cortar  ", command=acortar)
    menubar.add_cascade(label="Edición", menu=editar)

    ayuda = Menu(menubar, tearoff=0)
    ayuda.add_command(label="Acerca del Bloc de notas ", command=aacerca)
    menubar.add_cascade(label="Ayuda", menu=ayuda)

    editor = Text(ventana, undo="true")
    editor.pack(side=TOP, fill=BOTH, expand=1)

    ventana.title("Blog de notas de Eduardo")
    ventana.geometry("695x424")
    ventana.config(menu=menubar)
    ventana.mainloop()