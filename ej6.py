from tkinter import *
from tkinter import messagebox

# def Añadir():
#     lista.insert(END,entrada.get())
#     entrada.set("")

#debemos validar los ingresos vacios

def Añadir():
    a = entrada.get() #Se obtiene valor en Entry
   #validamos el ingreso para no almacenar datos erróneos
    if (a.isspace() or len(a) <= 1):
        messagebox.showinfo(message="El nombre de la película no debe comenzar con un espacio", title="Error")
        entrada.set("")
    else:
        lista.insert(END, a) #Se inserta en Listbox
        entrada.set("") #Se limpia el campo
    
window=Tk()
window.geometry("600x400")
window.title("Peliculas")
window.config(bg="white")
entrada=StringVar()

label1 = Label(window, text = "Nombre de la pelicula.", bg="lightgrey")
label1.place(x = 70, y = 50)

entry1 = Entry(window, textvariable = entrada, bg="lightgrey")
entry1.place(x = 70, y = 90)

botonAdd = Button(window, text = "Agregar", command = Añadir, bg="lightgrey")
botonAdd.place(x = 70, y = 130)

label2 = Label(window, text = "Peliculas", bg="lightgrey")
label2.place(x = 360, y = 50)

lista= Listbox(window)
lista.place(x = 320, y = 70)

window.mainloop()
