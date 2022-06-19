
def funcion1(archivo,lista):
    with open(archivo,"w") as temporal:
        for i in lista:
            temporal.write("%s\n" % i)
    file = open(archivo, 'r')
    # print(file.read())
    
def funcion2(archivo,lista):
    import math
    lista2=[]
    for i in lista:
        lista2.append(math.sqrt(i))
    with open(archivo,"w") as temporal:
        for i in lista2:
            temporal.write("%s\n" % i)
    file = open(archivo, 'r')
