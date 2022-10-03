from tkinter import *
from random import *

window= Tk()
window.geometry("320x200")
window.config(bg="white")
window.title("Generador de números")
window.resizable(False, False)


def generadorNumero():
    x1 = int(spinBox1.get())
    x2 = int(spinBox2.get())
    if x1 > x2:
        r = "El primer valor debe ser superior al segundo valor"
        numeroGen.set(r)
    else:
        r = randint(x1,x2)
        numeroGen.set(r)

label1 = Label(window,text="Número 1")
label1.place(x= 30,y = 20)
label2 = Label(window,text="Número 2")
label2.place(x= 30,y = 50)
label3 = Label(window,text="Número Generado")
label3.place(x= 30,y = 80)

#se añaden los estados de readonly en ambos spin para que el usuario manipule mediante el uso del widget exclusivamente los números
spinBox1 = Spinbox(window,to = 1000, state="readonly")
spinBox1.place(x= 170,y = 20)

spinBox2 = Spinbox(window,to = 1000, state="readonly")
spinBox2.place(x= 170,y = 50)

numeroGen = StringVar()
numeroGen.set("")
entry1 = Entry(window,textvariable=numeroGen)
entry1.place(x= 170,y = 80)

botonGenerar = Button(window,text="Generar",command=generadorNumero)
botonGenerar.place(x = 200, y= 110)



window.mainloop()
