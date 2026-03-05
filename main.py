import random

def numeros ():
    num=random.randint (1, 6)
    return num

def tirada ():
    cont=0
    lista=[]
    while cont<5:
        numero=numeros()
        lista.append(numero)
        cont+=1  
    return lista

def definir_tirada (tirar):
    poss=[]
    valido=True
    while len(poss)<5 and valido==True:
        posicion_elegida=input("Que posicion desea modificar? (presione enter para terminar)")
        if posicion_elegida!="":
            poss.append(int(posicion_elegida))
        else:
            valido=False
    return poss

def cambiar_posicion(tirar, poss):
    num=numeros()
    for i in range(len(tirar)):
        for j in poss:
            if j==i+1:
                tirar[i]=num
    print(tirar)

def sinrep(lista):
    nueva=[]
    for j in lista:
        for i in nueva:
            if j!=i:
                nueva.append(j)
    return nueva

def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i]>lista[j]:
                lista[i], lista[j]==lista[j], lista[i]

def escalera(tirar):
    sr=sinrep(tirar)
    if len(sr)==5:
        esca=True
    else:
        esca=False

def full(tirar):
    sr=sinrep(tirar)
    contadores=[]
    for i in tirar:
        cont=0
        for j in sinrep:
            if i==j:
                cont+=1
    f=False
    ordenar(contadores)
    if contadores[-1]==3 and contadores[-2]==2:
        f=True
    return f

def poker (tirar):
    sr=sinrep(tirar)
    contadores=[]
    for i in tirar:
        cont=0
        for j in sinrep:
            if i==j:
                cont+=1
    p=False
    ordenar(contadores)
    if contadores[-1]==4:
        p=True
    return p

def generala (tirar):
    sr=sinrep(tirar)
    contadores=[]
    for i in tirar:
        cont=0
        for j in sinrep:
            if i==j:
                cont+=1
    g=False
    if contadores[-1]==5:
        g=True

tirar=tirada()
print(tirar)
tir=0
if generala(tirar)==False:
    while tir<3:
        jugar=input("desea seguir tirando?")
        if jugar[0]=="s" or jugar[0]=="S":
            tir+=1
            poss=definir_tirada(tirar)
            print(poss)
            cambiar_posicion(tirar, poss)
        else:
            tir=3

    
