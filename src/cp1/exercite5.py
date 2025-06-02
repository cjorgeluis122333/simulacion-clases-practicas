#!/usr/bin/env python3
"""
Programa: Generador Congruencial Mixto con período 256

Objetivo:
    Encontrar un conjunto de valores para a y c en el generador congruencial mixto
    que asegure un período máximo de 256, en una computadora con palabra de 8 bits (2^8 = 256).
    Además, se generan los primeros 257 números para evidenciar que el ciclo completo (256 números)
    se repite, ya que el número inicial se vuelve a generar en la posición 256.

Modelo del generador:
    xₙ₊₁ = (a * xₙ + c) mod m
donde:
    m = 256

Condiciones para período máximo (Teorema de Hull–Dobell):
    1. c y m deben ser coprimos. (Para m = 256, c debe ser impar)
    2. a - 1 debe ser divisible por el factor primo de m. (m = 256 tiene 2 como único factor)
    3. Si m es múltiplo de 4, entonces a - 1 debe ser divisible por 4. (Se requiere que a ≡ 1 mod 4)

Ejemplo de parámetros elegidos:
    a = 5, c = 1, x₀ = 0
Estos parámetros cumplen:
    - c = 1 es impar y, por lo tanto, coprimo con 256.
    - a - 1 = 4, que es divisible por 4.

Con estos parámetros, el generador tendrá período 256.
"""


def generar_lcg(a, c, m, x0, n):
    """
    Genera n números usando el generador congruencial mixto.

    Parámetros:
        a  : multiplicador.
        c  : incremento.
        m  : módulo.
        x0 : semilla inicial.
        n  : cantidad de números a generar.

    Retorna:
        Una lista con los n números generados.
    """
    numeros = [x0]  # Se agrega la semilla inicial a la lista.
    x = x0
    for _ in range(n - 1):
        # Calcula el siguiente número del generador.
        x = (a * x + c) % m
        numeros.append(x)
    return numeros


def main():
    # Definición de los parámetros del generador:
    m = 256  # Módulo: 2^8 = 256.
    a = 5  # a debe cumplir a ≡ 1 mod 4, por ejemplo, 5.
    c = 1  # c debe ser impar (coprimo con 256).
    x0 = 0  # Semilla inicial (puede ser cualquier valor en [0, 255]).

    # Se desea generar los primeros 257 números (esto cubre un ciclo completo de 256 números
    # y el siguiente número, que debe ser igual al inicial, evidenciando el período).
    n = 257

    # Generamos la secuencia con el generador congruencial mixto.
    secuencia = generar_lcg(a, c, m, x0, n)

    # Imprime los parámetros y la secuencia generada.
    print("Generador Congruencial Mixto con m =", m)
    print("Parámetros elegidos:")
    print("    a =", a, " (debe ser ≡ 1 mod 4)")
    print("    c =", c, " (debe ser impar)")
    print("    x₀ =", x0)
    print("\nGenerando los primeros", n, "números:")
    for i, num in enumerate(secuencia):
        print(f"x[{i}] = {num}")

    # Verificación del período:
    # El primer número (x[0]) debe repetirse en la posición x[256] si el período es 256.
    if secuencia[0] == secuencia[256]:
        print("\nVerificación: El primer número se repite en la posición 256, lo que confirma un período de 256.")
    else:
        print("\nVerificación: La secuencia NO tiene un período de 256.")


if __name__ == "__main__":
    main()
