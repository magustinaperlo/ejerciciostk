from tkinter import *
import tkinter

def suma():
    valor = int(lineEdit ["text"])
    lineEdit ["text"] = f"{valor+1}"

window= Tk()
window.config(bg="White")
window.geometry("270x100")
window.title("ContCreciente")
window.resizable(False, False)


Label1=Label(window,width = 10,text=" Contador ", bg="lightgrey")
Label1.place(x=30,y=40)

lineEdit = Label(window,width = 10,text = "0" , bg = "lightgrey")
lineEdit.place( x = 120, y = 40)

Boton= Button(window, width = 2,text = "+", command= suma, bg= "lightgrey")
Boton.place(x=210,y=36)

window.mainloop()