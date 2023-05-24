#Importación de Librerias
from tkinter import*
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib.pyplot import text
from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt

#Crear ventana y etiquetas
win=Tk()
win.geometry("740x740")
win.title("Trabajo Final Cálculo Integral")
win.config(bg="aliceblue")
tit=Label(win,text="GRAFICADORA DE INTEGRALES DEFINIDAS")
tit.pack()
tit.place(x=200,y=10)
tit.config(bg="aliceblue")
tit.configure(font=("Consolas", 14))

#Función Graficar y Hallar Área
def graficar():
    fig=Figure(figsize=(5,15),dpi=120)
    plot1=fig.add_subplot(111)
    fun={"sin":"np.sin","cos":"np.cos","tan":"np.tan","sqrt":"np.sqrt","exp":"np.exp","log":"np.log","pi":"np.pi"}
    def fx(funcion,x):
        for i in fun:
            if i in funcion:
                funcion=funcion.replace(i,fun[i])
        return eval(funcion)
    a=int(lim_inferior.get())
    b=int(lim_superior.get())
    c=int(tramos.get())
    muestras=c+1
    #Hallar área
    h=(b-a)/c
    suma=0
    xi=a
    for i in range(0,c,1):
        areatrapecio=h*(fx(funcion.get(),xi)+fx(funcion.get(),xi+h))/2
        suma+=areatrapecio
        xi+=h

    muestraslineas=muestras*10
    xi=np.linspace(a,b,muestras)
    fi=fx(funcion.get(),xi)
    xk=np.linspace(a,b,muestraslineas)
    fk=fx(funcion.get(),xk)
    plot1.fill_between(xi,0,fi,color="lime")

    for i in range(0,muestras,1):
        plot1.axvline(xi[i], color="w")

    plot1.plot([0, b], [0, 0], color='black')
    plot1.grid()
    plot1.plot(xi,fi,"ro")
    plot1.plot(xk,fk)
    plot1.set_title(f"El área es: {suma}")
    canvas1=FigureCanvasTkAgg(fig,master=canvas)
    canvas1.draw() 
    canvas1.get_tk_widget().pack(padx=100,pady=50)

    toolbar=NavigationToolbar2TkAgg(canvas1,win)
    toolbar.update()
    canvas1.get_tk_widget().pack(side=TOP,fill=BOTH)

    #Funcion para Limpiar
    def limpiar():
        canvas1.draw()
        canvas1.get_tk_widget().pack_forget()
        lim_inferior.delete(0, END)
        lim_superior.delete(0, END)
        tramos.delete(0, END)  
        funcion.delete(0, END)

    #Boton para limpiar
    btn2=Button(win, text="  LIMPIAR  ",bg="cyan3", command=limpiar)
    btn2.configure(font=("Consolas", 12))
    btn2.pack()
    btn2.place(x=400,y=110)

#Etiqueta Función
fun=Label(win,text="Función")
fun.pack()
fun.place(x=10,y=40)
fun.config(bg="aliceblue")
funcion=Entry(win)
funcion.pack()
funcion.place(x=10,y=60)

#Etiqueta Limite Inferior
lim_inf=Label(win,text="Limite Inferior")
lim_inf.pack()
lim_inf.place(x=200, y=40)
lim_inf.config(bg="aliceblue")
lim_inferior=Entry(win)
lim_inferior.pack()
lim_inferior.place(x=200,y=60)

#Etiqueta Limite Superior
lim_sup=Label(win,text="Limite Superior")
lim_sup.pack()
lim_sup.place(x=400,y=40)
lim_sup.config(bg="aliceblue")
lim_superior=Entry(win)
lim_superior.pack()
lim_superior.place(x=400,y=60)

#Etiqueta Tramos
trm=Label(win, text="Tramos")
trm.pack()
trm.place(x=600,y=40)
trm.config(bg="aliceblue")
tramos=Entry(win)
tramos.pack()
tramos.place(x=600, y=60)

#Boton para ejecutar
btn=Button(win, text=" GRAFICAR ",bg="cyan3", command=graficar)
btn.configure(font=("Consolas", 12))
btn.pack()
btn.place(x=250,y=110)


#Espacio para la grafica
canvas=Canvas(win,width=700,height=600,highlightbackground="cyan3")
canvas.pack(pady=160)
win.mainloop()