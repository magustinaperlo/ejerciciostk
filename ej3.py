
import math
from tkinter import *




def calculoFactorial():      
    c = int(num.get())+1
    resultadoFactorial.config(text= math.factorial(c))
    for i in range(c):
        num.set(c)
   
window=Tk()
window.geometry("500x100")
window.title("Factorial")
window.resizable(False, False)
window.config(bg="White")

Label1 = Label(window, text=" !n ", bg= "lightgrey")
Label1.place(x = 45, y = 29)

num = IntVar(value=0)
E1 = Entry(window,textvariable=num,state="readonly")
E1.place(x = 70, y = 30)

L2 = Label(window, text= "Factorial (n)", bg= "lightgrey")
L2.place(x = 200, y = 29)

resultadoFactorial = Label(window,text="1")
resultadoFactorial.place(x = 275, y = 30)

Boton = Button(window, text="Siguiente", command=calculoFactorial, bg= "lightgrey")
Boton.place(x = 410, y = 26)

window.mainloop()