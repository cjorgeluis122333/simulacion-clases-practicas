#!/usr/bin/env python3
"""
Implementación del algoritmo de Marsaglia y MacLaren

Descripción:
-------------
El algoritmo de Marsaglia y MacLaren es una técnica para mejorar la calidad de los números aleatorios
generados mediante el uso de dos fuentes independientes. Se basa en una tabla (o vector) de tamaño k, que
se inicializa con k números aleatorios (obtenidos mediante una función generadora uniforme). Luego, para cada
número a generar, se utiliza otro número aleatorio para seleccionar un índice en dicha tabla. El valor en ese
índice se utiliza como salida y se reemplaza por un nuevo número aleatorio.

Este método ayuda a "mezclar" la secuencia y a reducir ciertas correlaciones presentes en los generadores
básicos.

Algoritmo:
-----------
1. Definir un parámetro k (en este caso k = 10) que determina el tamaño de la tabla.
2. Inicializar la tabla V con k números aleatorios obtenidos de la función generadora uniforme.
3. Para cada número a generar (se desea generar n números, en este caso n = 100):
   a) Generar un número y (usando un generador uniforme independiente).
   b) Calcular el índice j = floor(k * y) (esto es, la parte entera de k * y).
   c) El número de salida es el valor almacenado en la posición j de la tabla V.
   d) Reemplazar V[j] por un nuevo número aleatorio obtenido de la función generadora (la fuente “x”).
4. La secuencia de salida consiste en los n números generados, que se espera tengan mejores propiedades
   estadísticas que la secuencia simple del generador uniforme.

Nota:
------
Para efectos de esta implementación didáctica, se utiliza la misma función random.random() para obtener
los números de ambas fuentes (x_n y y_n), lo cual es adecuado para ilustrar el algoritmo, aunque en una
aplicación real se podrían usar generadores independientes.

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""

import random


def marsaglia_maclaren(k, n):
    """
    Implementa el algoritmo de Marsaglia y MacLaren para generar n números aleatorios.

    Parámetros:
        k (int): Tamaño de la tabla de mezcla.
        n (int): Número de números aleatorios a generar.

    Retorna:
        list: Lista con n números aleatorios generados mediante el algoritmo.
    """
    # Paso 1: Inicializar la tabla V con k números aleatorios (usando la función random.random())
    V = [random.random() for _ in range(k)]

    # Lista donde se almacenarán los números generados
    salida = []

    # Paso 2: Generar n números aleatorios
    for i in range(n):
        # Generar un número aleatorio y (fuente "y")
        y = random.random()

        # Calcular el índice j = floor(k * y)
        # La función int() en Python descarta la parte decimal, equivalente a floor() para números positivos.
        j = int(k * y)

        # Asegurarse de que j esté en el rango [0, k-1]
        if j >= k:
            j = k - 1

        # El número de salida se obtiene de la tabla en la posición j
        x = V[j]
        salida.append(x)

        # Reemplazar el valor en la posición j por un nuevo número aleatorio (fuente "x")
        V[j] = random.random()

    return salida


def main():
    # Parámetros del algoritmo
    k = 10  # Tamaño de la tabla de mezcla
    n = 100  # Cantidad de números a generar

    # Generar la secuencia mediante el algoritmo de Marsaglia y MacLaren
    numeros_generados = marsaglia_maclaren(k, n)

    # Mostrar los resultados
    print("Algoritmo de Marsaglia y MacLaren (k =", k, ")")
    print("Se han generado", n, "números aleatorios:\n")
    for indice, numero in enumerate(numeros_generados, start=1):
        print(f"{indice:3d}: {numero:.8f}")


if __name__ == "__main__":
    main()
