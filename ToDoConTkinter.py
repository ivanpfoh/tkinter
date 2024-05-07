from tkinter import *
import tkinter as tk

root = Tk()
root.config(bd=15)


def tareaguardada():
    tarea_guardada = tarea.get()
    if tarea_guardada:
        lista_tareas.insert(tk.END, tarea_guardada)
        tarea.delete(0, tk.END)

def borrar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)

label = Label(root, text="Tarea 1: ")
label.grid(row=0, column=0)

tarea = Entry(root)
tarea.grid(row=0, column=1)



botonguardar = Button(root, text="Guardar", command=tareaguardada)
botonguardar.grid(row=0, column=2)


lista_tareas = tk.Listbox(root)
lista_tareas.grid(row=1, column=1)

botonguardar = Button(root, text="Borrar", command=borrar_tarea)
botonguardar.grid(row=2, column=2)




root.mainloop()