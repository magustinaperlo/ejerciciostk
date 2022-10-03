from tkinter import *


def funcionSuma():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    #estamos sumando la misma variable dos veces
    # r = x1 + x1
    r=x1+x2
    resultado.set(r)

def funcionResta():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    #estamos restando la misma variable dos veces
    #r = x1 - x1
    r= x1-x2
    resultado.set(r)

def funcionProducto():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
     #estamos multiplicando la misma variable dos veces
   # r = x1 * x1
    r = x1*x2
    resultado.set(r)

def funcionDivision():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    if x2 ==  0:
        r="Error, no se puede dividir por 0."
        resultado.set(r)
    else:
        r = x1/x2
        resultado.set(r)

def funcionPorcentaje():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    #error en el calculo de porcentaje, estás sacando el módulo que es otra operación matemática
    #r = x1%x2 
    r = (x1*x2)/100
    resultado.set(r)

def funcionClear():
    e1.set("")
    e2.set("")
    resultado.set("")
