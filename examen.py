from tkinter import *
import turtle
import os

t= turtle.Pen()

tk = Tk()
tk.geometry("300x300")
btn1 = Button(tk, text = "perimetros")
btn2 = Button(tk, text = "animacion")

btn1.pack()
btn2.pack()

perimetro = 0
area = 0

def perimetro():
    fig = int(input ("ingrese el numero de lados de la figura"))
    lado = int (input("ingrese el valor del lado: "))
    
    if lado == 3:
        print("perimetro triangulo es: ", 3*lado)
       
        
            
    elif lado == 4:
        print("perimetro cuadrado es : ", 4*lado)
        t.reset()
        for x in range (1,5):
            t.foreward(100)
            t.left(270)
        
    elif lado == 5:
        print("perimetro pentago es: ", 5*lado)
        t.reset()
        for x in range (1,6):
            t.forward(105)
            t.left(292)
        
    
def area():

    print("ingrese los siguientes datos")
    
    fig = int(input ("ingrese el numero de lados de la figura"))
    lado = int (input("ingrese el valor del lado"))
    base = int (input("ingrese el base"))
    altura = int (input("ingrese el altura"))
    apotema = int (input("ingrese el apotema"))

    if fig ==3:
        print("triangulo")
        print("area de un triangulo es: ", ((base * altura)/2))
        
    elif fig == 4:
        
        print("cuadrado")
        print("area de un cuadrado es: ", lado **2)
 
    elif fig == 5:
        print("pentagono")
        perimetro = 5*lado
        print("area de un pentagono es: ",((perimetro*apotema)/2))

def dibujar():
    
    


 
btn3 = Button(tk, padx = 10, bd = 5, text = "Perimeto", fg = "black", command = perimetro)
btn3.pack()
btn4 =Button(tk,padx = 10 , bd = 5 , text = "area", command = area)
btn4.pack()
