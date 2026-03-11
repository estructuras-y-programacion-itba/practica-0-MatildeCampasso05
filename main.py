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

    
import random

def tirar_dados(cantidad):
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(1, 6))
    return lista

def cambiar_posicion(dados_actuales, posiciones_a_cambiar):
    # Por cada posición que el usuario eligió, tiramos un dado nuevo
    for pos in posiciones_a_cambiar:
        if 1 <= pos <= 5:
            dados_actuales[pos-1] = random.randint(1, 6)
    return dados_actuales

# --- FUNCIONES DE VALIDACIÓN (Lógica de juego) ---

def contar_apariciones(dados, numero):
    cont = 0
    for d in dados:
        if d == numero:
            cont += 1
    return cont

def es_escalera(dados):
    d = sorted(dados)
    # Las tres posibles escaleras: 1-2-3-4-5, 2-3-4-5-6 o 1-3-4-5-6
    return d == [1,2,3,4,5] or d == [2,3,4,5,6] or d == [1,3,4,5,6]

def es_full(dados):
    tiene_3 = False
    tiene_2 = False
    for i in range(1, 7):
        cant = contar_apariciones(dados, i)
        if cant == 3: tiene_3 = True
        if cant == 2: tiene_2 = True
    return tiene_3 and tiene_2

def es_poker(dados):
    for i in range(1, 7):
        if contar_apariciones(dados, i) >= 4:
            return True
    return False

def es_generala(dados):
    for i in range(1, 7):
        if contar_apariciones(dados, i) == 5:
            return True
    return False

# --- GESTIÓN DE PLANILLA Y ARCHIVO ---

def guardar_csv(nombres_cat, p1, p2):
    arch = open("jugadas.csv", "w")
    arch.write("jugada,j1,j2\n")
    for i in range(len(nombres_cat)):
        # Si el puntaje es -1, mostramos vacío en el CSV
        v1 = p1[i] if p1[i] != -1 else ""
        v2 = p2[i] if p2[i] != -1 else ""
        arch.write(str(nombres_cat[i]) + "," + str(v1) + "," + str(v2) + "\n")
    arch.close()

# --- FLUJO PRINCIPAL DEL TURNO ---

def jugar_turno(nro_jugador, nombres_cat, puntajes_propios):
    print(f"\n--- TURNO JUGADOR {nro_jugador} ---")
    dados = tirar_dados(5)
    tiro = 1
    
    while tiro < 3:
        print(f"Tiro {tiro}: {dados}")
        if tiro == 1 and es_generala(dados):
            print("¡GENERALA SERVIDA!")
            return "GENERALA_REAL", dados
            
        rpta = input("¿Desea volver a tirar? (s/n): ")
        if rpta.lower() == 's':
            print("Ingrese posiciones a cambiar (1 a 5) separadas por espacio:")
            # Convertimos la entrada "1 3 5" en una lista de ints [1, 3, 5]
            pos_input = input().split()
            poss = []
            for p in pos_input:
                poss.append(int(p))
            dados = cambiar_posicion(dados, poss)
            tiro += 1
        else:
            break
    
    print(f"Dados finales: {dados}")
    return tiro, dados

# --- PROGRAMA PRINCIPAL ---

categorias = ["1", "2", "3", "4", "5", "6", "E", "F", "P", "G"]
puntos_j1 = [-1] * 10 # -1 significa categoría no usada
puntos_j2 = [-1] * 10

final_abrupto = False

for ronda in range(10): # 10 categorías en total
    for j in [1, 2]:
        p_actual = puntos_j1 if j == 1 else puntos_j2
        tiro_finalizado, dados_finales = jugar_turno(j, categorias, p_actual)
        
        # Caso Generala Real
        if tiro_finalizado == "GENERALA_REAL":
            print(f"¡EL JUGADOR {j} GANÓ POR GENERALA REAL!")
            final_abrupto = True
            # Llenamos la generala con 80 (50 + 30 de bono)
            p_actual[9] = 80
            break
        
        # Selección de categoría
        print("Categorías disponibles:")
        for i in range(len(categorias)):
            if p_actual[i] == -1:
                print(f"{i}: {categorias[i]}", end=" | ")
        
        eleccion = int(input("\nElija el número de categoría para anotar: "))
        
        # Calcular puntaje según elección
        puntos = 0
        es_servida = (tiro_finalizado == 1)
        
        if eleccion < 6: # Números 1 al 6
            puntos = contar_apariciones(dados_finales, eleccion + 1) * (eleccion + 1)
        elif eleccion == 6 and es_escalera(dados_finales): # Escalera
            puntos = 25 if es_servida else 20
        elif eleccion == 7 and es_full(dados_finales): # Full
            puntos = 35 if es_servida else 30
        elif eleccion == 8 and es_poker(dados_finales): # Poker
            puntos = 45 if es_servida else 40
        elif eleccion == 9 and es_generala(dados_finales): # Generala
            puntos = 50
        
        p_actual[eleccion] = puntos
        guardar_csv(categorias, puntos_j1, puntos_j2)
        
    if final_abrupto: break

# Determinar Ganador
total1 = sum([x for x in puntos_j1 if x != -1])
total2 = sum([x for x in puntos_j2 if x != -1])
print(f"\nPuntaje Final -> J1: {total1} | J2: {total2}")
if total1 > total2: print("¡Ganador Jugador 1!")
elif total2 > total1: print("¡Ganador Jugador 2!")
else: print("¡Empate!")