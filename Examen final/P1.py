import random

def unico(var1,var2):
  esUnico=True
  for i in range(len(var2)):
    if var1==var2[i]:
      esUnico=False
      break
  return esUnico
var2=[]
j=0
while j<10:
  var1=random.randint(1,100)
  if unico(var1,var2):
    var2.append(var1)
    j+=1

var2.sort(reverse=True)
lista1=[]
lista1= lista1+var2
lista2=[]
var2.sort(reverse=False)
lista2=lista2+var2

print('La lista ordenada de mayor a menor es:', lista1)
print('La lista ordenada de menor a mayor es:', lista2)
print('El mayor valor es: ', max(var2))


