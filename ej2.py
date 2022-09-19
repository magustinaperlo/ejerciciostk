from tkinter import *
import tkinter

def resta():
    valor = int(lineEdit ["text"])
    lineEdit ["text"] = f"{valor-1}"

window= Tk()
window.config(bg="white")
window.geometry("270x100")
window.title("ContCreciente")
window.resizable(False, False)


Label1=Label(window,width = 10,text=" Contador ", bg="lightgrey")
Label1.place(x=30,y=40)

lineEdit = Label(window,width = 10,text = "88" , bg = "lightgrey")
lineEdit.place( x = 120, y = 40)

Boton= Button(window, width = 2,text = "-", command= resta, bg= "lightgrey")
Boton.place(x=210,y=36)

window.mainloop()