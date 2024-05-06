from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

root = Tk()
root.title("Pfoh Editor")
root.iconbitmap("Thumbnails-80_icon-icons.com_57262.ico") 



mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar=mensaje, justify='right')
monitor.pack(side='bottom')

def nuevo():
    mensaje.set('Nuevo fichero')
    texto.delete(1.0, END)

def abrir(): 
    global ruta 

    mensaje.set('Abrir fichero')

    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(
            ("Ficheros de texto", "*.txt"),  
        ), 
        title="Abrir un fichero."
    )

    if ruta != "":  
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')     
        texto.insert('insert', contenido)  
        fichero.close()                    
        root.title(ruta + " - Mi editor")

def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()


def guardar_como():
    global ruta
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode='w',
            defaultextension=".txt")
    ruta = fichero.name  # El atributo name es la ruta, si está abierto
    if fichero is not None:
        contenido = texto.get(1.0, 'end-1c')  # recuperamos el texto
        fichero = open(ruta, 'w+') # creamos el fichero o abrimos
        fichero.write(contenido)  # escribimos el texto
        fichero.close()
        mensaje.set('Fichero guardado correctamente')
    else:
        mensaje.set('Guardado cancelado')


ruta = ''

#Menu superior 
menubar = Menu(root)
root.config(menu=menubar)

#Menu archivo
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)






#menu editar
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=editmenu)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")







#menu ayuda
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

#Texto
texto = Text()
texto.pack()


root.mainloop()