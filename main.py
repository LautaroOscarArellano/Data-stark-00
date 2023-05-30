from data_stark import*
from funciones import*
import os

while True:
    os.system("cls")
    print("***Desafio Marvel***")
    print("A. Analizar detenidamente el set de datos")
    print("B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    print("C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    print("D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)")
    print("E Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)")
    print("F. Recorrer la lista y determinar la altura promedio de los superhéroes(PROMEDIO)")
    print("G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("H. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("I. Ordenar el código implementando una función para cada uno de los valores informados.")
    print("J. Construir un menú que permita elegir qué dato obtener")
    opcion=input("Ingrese opcion ").upper()

    if(opcion=="B"):
        mostrarNombre()

    elif(opcion=="C"):
        nombreAltura()

    elif(opcion=="D"):
       nombre_alto=heroeMayor(mayor,nombre_mayor)

    elif(opcion=="E"):
        nombre_bajo=heroe_chiquito(menor,nombre_menor)

    elif(opcion=="F"):
        altura_prromedio()
  
    elif (opcion=="G"):
        informe_maximo_minimo(nombre_alto,nombre_bajo)

    elif(opcion=="H"):
        heroe_menos_pesado(mas_pesado ,nombre_pesado ,nombre_menos_pesado , menos_pesado)
    os.system("pause")    





















