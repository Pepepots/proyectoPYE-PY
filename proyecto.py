import pandas as pd
from tkinter import *
from datos import bebida

raiz = Tk()

def ventanaPrediccion():
    newWindow = Toplevel(raiz) 
    
    newWindow.title("New Window") 
  
    newWindow.geometry("200x200") 

    txt = f'Tu bebida debe ser {bebida(edad.get(), temperatura.get())}'


    Label(newWindow, text =txt).pack()

raiz.title('Proyecto final')

# Seccion de inputs para el programa

inputFrame = Frame(raiz, width=500, height=400)
inputFrame.pack()

edad = IntVar(value=0)
temperatura = IntVar(value=0)

labelEdad = Label(inputFrame, text='Introduce tu edad: ').grid(row=1, column=1, sticky='e', padx=10, pady=15)
cuadroEdad = Entry(inputFrame, textvariable=edad).grid(row=1,column=2, padx=10, pady=15)

labelTemperatura = Label(inputFrame, text='Introduce la temperatura: ').grid(row=2, column=1, sticky='e', padx=10, pady=15)
cuadroTemperatura = Entry(inputFrame, textvariable=temperatura).grid(row=2,column=2, padx=10, pady=15)

# Frame par el boton

botonFrame = Frame(raiz, width=500, height=100)
botonFrame.pack()

botonEviar = Button(botonFrame, text='Enviar', width=3, command=ventanaPrediccion).place(relx=.4,rely=.4, relwidth=.2)

raiz.mainloop()