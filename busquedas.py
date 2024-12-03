import random
import time
import sys

def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return True
    return None

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None

def main():
    # Generar una lista aleatoria de 1000 elementos
    lista = sorted([random.randint(0, 10000) for _ in range(1000)])
    objetivo = random.randint(0, 10000)

    # Medir el tiempo de la búsqueda secuencial
    inicio = time.time()
    resultado_secuencial = busqueda_secuencial(lista, objetivo)
    fin = time.time()
    print(f'Búsqueda secuencial: {"Encontrado" if resultado_secuencial else "No encontrado"} en {fin - inicio:.6f} segundos')

    # Medir el tiempo de la búsqueda binaria
    inicio = time.time()
    resultado_binaria = busqueda_binaria(lista, objetivo)
    fin = time.time()
    print(f'Búsqueda binaria: {"Encontrado" if resultado_binaria else "No encontrado"} en {fin - inicio:.6f} segundos')

if __name__ == "__main__":
    main()
