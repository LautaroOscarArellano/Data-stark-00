from data_stark import *

mayor=lista_personajes[0]
nombre_mayor=lista_personajes[0]
menor=lista_personajes[0]
nombre_menor=lista_personajes[0]
nombre_alto=None
nombre_bajo=None
mas_pesado=lista_personajes[0]
nombre_pesado=None
nombre_menos_pesado=None
menos_pesado=lista_personajes[0]


#pasaje numerico
for elemento in lista_personajes:
    elemento["altura"]=float(elemento["altura"])
    elemento["peso"]=float(elemento["peso"])




def mostrarNombre():
    print("Imprimir nombre de cada heroe\n")
    for clave in lista_personajes:
        print(f"{clave['nombre']}")

def nombreAltura():
    print("Nombre super heroe        altura ")
    for clave in lista_personajes:
        print(f"{clave['nombre']:20s}  {clave['altura']:10.2f}")


def heroeMayor(mayor,nombre_mayor):
    for elemento in lista_personajes:
        if(mayor["altura"]<elemento["altura"]):
            mayor=elemento
            nombre_mayor=elemento["nombre"]
    print(f"El super heroe mas alto es {nombre_mayor}")
    return(nombre_mayor)

def altura_prromedio():
    sumatoria=0
    vueltas=0
    for elemento in lista_personajes:
        sumatoria+=elemento["altura"]
        vueltas+=1
    promedio=sumatoria//vueltas
    print(f"Altura promedio de los super heroes es {promedio}")


def heroe_chiquito(menor , nombre_menor):
    for elemento in lista_personajes:
        if(menor["altura"]>elemento["altura"]):
            menor=elemento
            nombre_menor=elemento["nombre"]
    print(f"El super heroe mas bajo es {nombre_menor.get('nombre')}")#esto esta asi xk justo el pato es el primero, en caso de no ser el primero el mas chico tira error {nombre_menor.get('nombre')}
    return(nombre_menor)

def informe_maximo_minimo(a,b):
    print(f"El maximo es {a} , el minimo es {b['nombre']}")

def heroe_menos_pesado(mas_pesado,nombre_pesado,nombre_menos_pesado,menos_pesado):
    for elemento in lista_personajes:
        if(mas_pesado["peso"] < elemento["peso"]):
            mas_pesado=elemento
            nombre_pesado=elemento["nombre"]
        elif(menos_pesado["peso"]>elemento["peso"]):
            menos_pesado=elemento
            nombre_menos_pesado=elemento["nombre"]
    print(f"El super heroe mas pesado es {nombre_pesado} , nombre menos pesado {nombre_menos_pesado}")
