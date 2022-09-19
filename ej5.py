from tkinter import *


def funcionSuma():
    x1 = int(entry1.get())
    x2 = int(entry2.get())
    r = x1 + x1
    resultado.set(r)

def funcionResta():
    x1 = int(entry1.get())
    x2 = int(entry2.get())
    r = x1 - x1
    resultado.set(r)

def funcionProducto():
    x1 = int(entry1.get())
    x2 = int(entry2.get())
    r = x1 * x1
    resultado.set(r)

def funcionDivision():
    x1 = int(entry1.get())
    x2 = int(entry2.get())
    if x2 ==  0:
        r="Error, no se puede dividir por 0."
        resultado.set(r)
    else:
        r = x1/x2
        resultado.set(r)

def funcionPorcentaje():
    x1 = int(entry1.get())
    x2 = int(entry2.get())
    r = x1%x2
    resultado.set(r)

def funcionClear():
    e1.set("")
    e2.set("")
    resultado.set("")






window = Tk()
window.geometry("300x300")
window.title("Calculadora")
window.config(bg = "white")

e1= StringVar()
e2= StringVar()
resultado= StringVar()
e1.set("")
e2.set("")
resultado.set("")

label1 = Label(window,text= "Primer valor",bg ="lightgrey")
label1.place(x =30,y = 15)
entry1 = Entry(window,textvariable=e1)
entry1.place(x = 150, y = 15)


label2 = Label(window,text= "Segundo valor",bg ="lightgrey")
label2.place(x = 30, y = 50)
entry2 = Entry(window,textvariable=e2)
entry2.place(x = 150, y = 50)

label3 = Label(window,text= "Resultado",bg ="lightgrey")
label3.place(x = 30, y = 90)
entry3 = Entry(window,textvariable=resultado,state="readonly")
entry3.place(x = 150, y = 90)

botonSuma = Button(window, text = " + ", command = funcionSuma, bg="lightgrey",width=10)
botonSuma.place(x = 40, y = 130)

botonResta = Button(window, text = " - ", command = funcionResta, bg="lightgrey",width=10)
botonResta.place(x = 160, y = 130)

botonMultiplicacion = Button(window, text = " * ", command = funcionProducto, bg="lightgrey",width=10)
botonMultiplicacion.place(x = 40, y = 170)

botonDivision= Button(window, text = " / ", command = funcionDivision, bg="lightgrey",width=10)
botonDivision.place(x = 160, y = 170)

botonPorcentaje= Button(window, text = " % ", command = funcionPorcentaje, bg="lightgrey",width=10)
botonPorcentaje.place(x = 40, y = 210)

botonClear = Button(window, text = " AC ", command = funcionClear, bg="Red",width=10)
botonClear.place(x = 160, y = 210)




window.mainloop()