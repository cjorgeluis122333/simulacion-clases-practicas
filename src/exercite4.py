#!/usr/bin/env python3
"""
Programa para el análisis del generador congruencial mixto con m = 10.

El generador tiene la forma:
    xₙ₊₁ = (a * xₙ + c) mod m
con m = 10.

Se deben resolver los siguientes apartados:
a) Encontrar valores de a, c y x₀ que produzcan todos los números impares (ciclo de 5) y ningún par.
b) Encontrar valores de a, c y x₀ que produzcan todos los números pares (ciclo de 5) y ningún impar.
c) Determinar si existen valores no triviales de a y c (diferentes de 1) que produzcan un período completo de 10.
"""


def generar_secuencia(a, c, x0, m=10):
    """
    Genera la secuencia del generador congruencial mixto hasta detectar la repetición del ciclo.

    Parámetros:
        a: multiplicador.
        c: incremento.
        x0: semilla inicial.
        m: módulo (por defecto 10).

    Retorna:
        secuencia: lista de los números generados antes de que se repita el ciclo.
    """
    secuencia = []
    x = x0
    while True:
        # Si x ya está en la secuencia, se detecta el ciclo y se finaliza
        if x in secuencia:
            break
        secuencia.append(x)
        x = (a * x + c) % m
    return secuencia


def es_todo_impar(secuencia):
    """
    Verifica si todos los elementos de la secuencia son impares.

    Parámetro:
        secuencia: lista de números.

    Retorna:
        True si todos son impares, False en caso contrario.
    """
    return all(x % 2 == 1 for x in secuencia)


def es_todo_par(secuencia):
    """
    Verifica si todos los elementos de la secuencia son pares.

    Parámetro:
        secuencia: lista de números.

    Retorna:
        True si todos son pares, False en caso contrario.
    """
    return all(x % 2 == 0 for x in secuencia)


def main():
    m = 10
    print("Generador Congruencial Mixto con m =", m)
    print("===========================================")

    # Parte (a): Buscar valores que produzcan solo números impares (ciclo de 5).
    # Solución propuesta: a = 1, c = 2, x0 = 1.
    a_a = 1
    c_a = 2
    x0_a = 1
    secuencia_a = generar_secuencia(a_a, c_a, x0_a, m)
    print("\nParte (a): Secuencia de números impares")
    print("Parámetros: a =", a_a, ", c =", c_a, ", x0 =", x0_a)
    print("Secuencia generada:", secuencia_a)
    print("Longitud del ciclo:", len(secuencia_a))
    if es_todo_impar(secuencia_a) and len(secuencia_a) == 5:
        print("Resultado: La secuencia contiene solo números impares con ciclo de 5 elementos.")
    else:
        print("Resultado: La secuencia NO cumple la condición requerida.")

    # Parte (b): Buscar valores que produzcan solo números pares (ciclo de 5).
    # Solución propuesta: a = 1, c = 2, x0 = 0.
    a_b = 1
    c_b = 2
    x0_b = 0
    secuencia_b = generar_secuencia(a_b, c_b, x0_b, m)
    print("\nParte (b): Secuencia de números pares")
    print("Parámetros: a =", a_b, ", c =", c_b, ", x0 =", x0_b)
    print("Secuencia generada:", secuencia_b)
    print("Longitud del ciclo:", len(secuencia_b))
    if es_todo_par(secuencia_b) and len(secuencia_b) == 5:
        print("Resultado: La secuencia contiene solo números pares con ciclo de 5 elementos.")
    else:
        print("Resultado: La secuencia NO cumple la condición requerida.")

    # Parte (c): Determinar si existen valores no triviales de a y c (ambos ≠ 1) que produzcan período 10.
    # De acuerdo con el teorema de Hull-Dobell, para m = 10 se requiere:
    #   - c debe ser coprimo con 10 (c ∈ {1, 3, 7, 9}).
    #   - a - 1 debe ser divisible por 10, es decir, a ≡ 1 mod 10.
    # Evitando a = 1, una solución es: a = 11, c = 3 y x0 = 0.
    a_c = 11
    c_c = 3
    x0_c = 0
    secuencia_c = generar_secuencia(a_c, c_c, x0_c, m)
    print("\nParte (c): Período completo de 10")
    print("Parámetros: a =", a_c, ", c =", c_c, ", x0 =", x0_c)
    print("Secuencia generada:", secuencia_c)
    print("Longitud del ciclo:", len(secuencia_c))
    if len(secuencia_c) == 10:
        print("Resultado: Con a =", a_c, "y c =", c_c, "se obtiene un período de 10.")
    else:
        print("Resultado: Los parámetros dados NO producen un período de 10.")


if __name__ == "__main__":
    main()
