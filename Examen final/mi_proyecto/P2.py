import random
from funciones import *

cant= input('Ingrese el tamaño de lista: ')
cant=int(cant)

lista= []
for i in range(0,cant):
    var1=random.randint(1,100)
    lista.append(var1)

llamado1 = funcion1("notas.txt",lista)
llamado2=funcion2("notas2.txt",lista)

