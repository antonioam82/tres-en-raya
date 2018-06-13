#TRES EN RAYA
#DE MOMENTO SOLO ESTÁ DISPONIBLE LA OPCIÓN PARA 2 JUGADORES
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import random####

def bloquear():
    for i in range(0,9):
        listaBotones[i].config(state="disable")

def hola():
    return True

def cambiar(num):
    global turno,nombreJugador1,nombreJugador2,elecJugador1,SnombreJugador1,SnombreJugador2,lista#,numJ###
    if t[num]=="N" and turno==0:
        listaBotones[num].config(text=elecJugador1)
        listaBotones[num].config(bg="white")
        if numJ=="1":
            del(lista[lista.index(str(num))])
            #print(lista)
        t[num]=elecJugador1
        turno=1
        turnoJugador.set("Turno: " + SnombreJugador2)
    elif t[num]=="N" and turno==1:
        if numJ=="1":####
            num=random.choice(lista)####
            #print(num)
            num=int(num)
        listaBotones[num].config(text=elecJugador2)
        listaBotones[num].config(bg="lightblue")
        
        t[num]=elecJugador2
        listaBotones[num].config(state="disable")
        del(lista[lista.index(str(num))])
        turno=0
        turnoJugador.set("Turno: " + SnombreJugador1)
            
        #print(lista)
        
    listaBotones[num].config(state="disable")
    ganador()

def ganador():
    if (t[0]==elecJugador1 and t[1]==elecJugador1 and t[2]==elecJugador1)or(t[3]==elecJugador1 and t[4]==elecJugador1 and t[5]==elecJugador1)or(t[6]==elecJugador1 and t[7]==elecJugador1 and t[8]==elecJugador1):
        bloquear()
        messagebox.showinfo("GANADOR",SnombreJugador1+" Gano el juego")
    if (t[0]==elecJugador1 and t[4]==elecJugador1 and t[8]==elecJugador1)or(t[2]==elecJugador1 and t[4]==elecJugador1 and t[6]==elecJugador1):
        bloquear()
        messagebox.showinfo("GANADOR",SnombreJugador1+" Gano el juego")
    if (t[0]==elecJugador1 and t[3]==elecJugador1 and t[6]==elecJugador1)or(t[1]==elecJugador1 and t[4]==elecJugador1 and t[7]==elecJugador1)or(t[2]==elecJugador1 and t[5]==elecJugador1 and t[8]==elecJugador1):
        bloquear()
        messagebox.showinfo("GANADOR",SnombreJugador1+" Gano el juego")
    if (t[0]==elecJugador2 and t[1]==elecJugador2 and t[2]==elecJugador2)or(t[3]==elecJugador2 and t[4]==elecJugador2 and t[5]==elecJugador2)or(t[6]==elecJugador2 and t[7]==elecJugador2 and t[8]==elecJugador2):
        bloquear()
        messagebox.showinfo("GANADOR",SnombreJugador2+" Gano el juego")
    if (t[0]==elecJugador2 and t[4]==elecJugador2 and t[8]==elecJugador2)or(t[2]==elecJugador2 and t[4]==elecJugador2 and t[6]==elecJugador2):
        bloquear()
        messagebox.showinfo("GANADOR",SnombreJugador2+" Gano el juego")
    if (t[0]==elecJugador2 and t[3]==elecJugador2 and t[6]==elecJugador2)or(t[1]==elecJugador2 and t[4]==elecJugador2 and t[7]==elecJugador2)or(t[2]==elecJugador2 and t[5]==elecJugador2 and t[8]==elecJugador2):
        bloquear()
        messagebox.showinfo("GANADOR",SnombreJugador2+" Gano el juego")

def iniciarJ():
    global lista
    lista=["0","1","2","3","4","5","6","7","8"]
    for i in range(0,9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="lightgrey")
        listaBotones[i].config(text="")
        t[i]="N"
    #aqui askstring
    global nombreJugador1,nombreJugador2,elecJugador1,elecJugador2,SnombreJugador1,SnombreJugador2,numJ
    try:
        while numJ==("") or (numJ!=str(1) and numJ!=str(2)):
            numJ=simpledialog.askstring("NUMERO JUGADORES","Indicar número de jugadores: ")
        while nombreJugador1==("") or not (",") in nombreJugador1:
            nombreJugador1=simpledialog.askstring("Jugador","Nombre jugador 1 y ficha (X o O) separadas por coma: ")
            elecJugador1=(("").join(nombreJugador1)).split(",")[1]#
            SnombreJugador1=(("").join(nombreJugador1)).split(",")[0]#
        if numJ=="2":
            while nombreJugador2==("") or not (",") in nombreJugador2:
                nombreJugador2=simpledialog.askstring("Jugador","Nombre jugador 2 y ficha (X o O) separadas por coma: ")#VER POSIBILIDADES DE "simpledialog".
                elecJugador2=(("").join(nombreJugador2)).split(",")[1]#
                SnombreJugador2=(("").join(nombreJugador2)).split(",")[0]#
        turnoJugador.set("Turno: " + SnombreJugador1)
        if numJ=="1":
            SnombreJugador2=("La Compu")
            if elecJugador1==("X"):
                elecJugador2=("O")
            else:
                elecJugador2=("X")
    except:
        bloquear()
ventana=Tk()
ventana.title("Tres en Raya")
ventana.geometry("400x500")
turno=0
numJ=("")
elecJugador1=("")
elecJugador2=("")
nombreJugador1=("")
nombreJugador2=("")
SnombreJugador1=("")##
SnombreJugador2=("")##
listaBotones=[]
lista=["0","1","2","3","4","5","6","7","8"]
t=[]
turnoJugador=StringVar()
for i in range(0,9):
    t.append("N")
boton0=Button(ventana,width=9,height=3,command=lambda: cambiar(0))
listaBotones.append(boton0)
boton0.place(x=50,y=50)
boton1=Button(ventana,width=9,height=3,command=lambda: cambiar(1))
listaBotones.append(boton1)
boton1.place(x=150,y=50)
boton2=Button(ventana,width=9,height=3,command=lambda: cambiar(2))
listaBotones.append(boton2)
boton2.place(x=250,y=50)
boton3=Button(ventana,width=9,height=3,command=lambda: cambiar(3))
listaBotones.append(boton3)
boton3.place(x=50,y=150)
boton4=Button(ventana,width=9,height=3,command=lambda: cambiar(4))
listaBotones.append(boton4)
boton4.place(x=150,y=150)
boton5=Button(ventana,width=9,height=3,command=lambda: cambiar(5))
listaBotones.append(boton5)
boton5.place(x=250,y=150)
boton6=Button(ventana,width=9,height=3,command=lambda: cambiar(6))
listaBotones.append(boton6)
boton6.place(x=50,y=250)
boton7=Button(ventana,width=9,height=3,command=lambda: cambiar(7))
listaBotones.append(boton7)
boton7.place(x=150,y=250)
boton8=Button(ventana,width=9,height=3,command=lambda: cambiar(8))
listaBotones.append(boton8)
boton8.place(x=250,y=250)
turnoE=Label(ventana,textvariable=turnoJugador).place(x=120,y=20)
iniciar=Button(ventana,bg="dark blue",fg="white",text="Iniciar Juego",width=15,height=3,command=iniciarJ).place(x=130,y=350)
bloquear()
ventana.mainloop()
