from tkinter import *
    
window = Tk()
window.title("calculadora 2")
window.geometry("350x350")
window.config(bg = "white")
window.resizable(False, False)

def funcionSuma():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    #sumas la misma variable 2 veces
    #r = x1 + x1
    r =x1+x2
    resultado.set(r)

def funcionResta():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    #operas con la misma variable
    #r = x1 - x1
    r=x1-x2
    resultado.set(r)

def funcionProducto():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    #operas con la misma variable
    #r = x1 * x1
    r =x1*x2
    resultado.set(r)

def funcionDivision():
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    if x2 ==  0:
        r="No se puede dividir por 0."
        resultado.set(r)
    else:
        r = x1/x2
        resultado.set(r)



def opcionRb():
    varFunction = int(opcion.get())
    if varFunction == 1:
        funcionSuma()
    elif varFunction == 2:
        funcionResta()
    elif varFunction == 3:
        funcionProducto()
    elif varFunction == 4:
        funcionDivision()
    





label1 = Label(window,text= "Primer valor",bg ="lightgrey")
label1.place(x =30,y = 15)
entry1 = Entry(window)
entry1.place(x = 150, y = 15)


label2 = Label(window,text= "Segundo valor",bg ="lightgrey")
label2.place(x = 30, y = 50)
entry2 = Entry(window)
entry2.place(x = 150, y = 50)

resultado=StringVar()
resultado.set("")
label3 = Label(window,text= "Resultado",bg ="lightgrey")
label3.place(x = 30, y = 90)
entry3 = Entry(window,state="readonly",textvariable=resultado)
entry3.place(x = 150, y = 90)

label4 = Label(window,text= "Operaciones",bg ="lightgrey")
label4.place(x = 30, y = 130)


opcion= IntVar()
radioButton1 = Radiobutton(window,text="Suma",value = 1,variable=opcion)
radioButton1.place(x = 30, y = 160)

radioButton2 = Radiobutton(window,text="Resta",value = 2,variable=opcion) 
radioButton2.place(x = 30, y = 190)

radioButton3 = Radiobutton(window,text="Multiplicación",value = 3,variable=opcion)
radioButton3.place(x = 30, y = 220)

radioButton4 = Radiobutton(window,text="División",value = 4,variable=opcion)
radioButton4.place(x = 30, y = 250)

botonCalcular = Button(window,text="Calcular",command = opcionRb)
botonCalcular.place(x = 175, y = 130)



window.mainloop()
