from tkinter import *

def Añadir():
    lista.insert(END,entrada.get())
    entrada.set("")
    
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