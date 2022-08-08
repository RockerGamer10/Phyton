from tkinter import DoubleVar


print("Ingrese su sueldo")
sueldo=int(input())

if (sueldo<1000):
    pay=float(sueldo*1.15)
    print("El sueldo es",pay)
else: print("El sueldo es",sueldo)