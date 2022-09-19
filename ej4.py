
from tkinter import *

def countUp():
    n = int(entry1.get())
    n = n + 1
    entryNum.set(n)

def countDown():
    n=int(entry1.get())
    n = n - 1
    entryNum.set(n)

def resetButton():
    n=0
    entryNum.set(n)

window= Tk()
window.config(bg="white")
window.geometry("400x80")
window.title("Contador")
Num=IntVar(window,0)

label1 = Label(window, text = "Contador", bg="Lightgrey")
label1.place(x = 40, y = 29)


entryNum = StringVar()
entryNum.set(0) 
entry1 = Entry(window, textvariable = entryNum,state="readonly")
entry1.place(x = 107, y = 30)

buttonUp = Button(window, text = "+1", command = countUp, bg="Lightgrey")
buttonUp.place(x = 240, y = 27)

buttonDown = Button(window, text = "-1", command = countDown, bg="Lightgrey")
buttonDown.place(x = 270, y = 27)

buttonReset = Button(window, text = "Reset", command = resetButton, bg="Lightgrey")
buttonReset.place(x = 300, y = 27)

window.mainloop()