#!/usr/bin/env python3
"""
Pruebas de Aleatoriedad: Prueba de Series y Prueba de Distancia Cuadrática

Este programa implementa dos pruebas estadísticas para evaluar si una secuencia de números
en el intervalo [0,1] se comporta como una secuencia de números aleatorios.

1. Prueba de Series:
   - Se forman pares consecutivos de números y se ubican en una matriz de frecuencias.
   - Se divide el intervalo [0,1] en "d" subintervalos en cada dimensión (por ejemplo, d=2 genera 4 celdas).
   - Se calcula el estadístico chi-cuadrado comparando las frecuencias observadas con las esperadas.

2. Prueba de Distancia Cuadrática:
   - Se forman pares consecutivos y se calcula la diferencia absoluta de cada par.
   - Se agrupan estas diferencias en "num_clases" intervalos.
   - Se utiliza la función de distribución teórica de la diferencia absoluta entre dos U(0,1):
         F(d) = 2d – d²   para 0 ≤ d ≤ 1.
   - Se calcula un estadístico chi-cuadrado comparando las frecuencias observadas y esperadas.

Autor: [Tu Nombre]
Fecha: [Fecha]
"""

import numpy as np
from scipy.stats import chi2


def prueba_series(datos, d=2):
    """
    Realiza la prueba de series.

    Se forman pares de números consecutivos y se ubican en una partición de d x d celdas del cuadrado unidad.
    Parámetros:
        datos: lista o arreglo de números en [0,1]. Se espera que la cantidad de datos sea par.
        d: número de subdivisiones en cada eje (por defecto 2).
    Retorna:
        chi2_stat: estadístico chi-cuadrado calculado.
        p_value: valor p asociado.
        tabla: matriz de frecuencias observadas (d x d).
    """
    n = len(datos)
    # Si el número de datos es impar, se descarta el último
    if n % 2 != 0:
        n = n - 1
        datos = datos[:n]
    num_pares = n // 2

    # Inicializamos la tabla de frecuencias (matriz de d x d)
    tabla = np.zeros((d, d), dtype=int)
    # Definimos los límites de las celdas (por ejemplo, para d=2, límites: [0, 0.5, 1])
    limites = np.linspace(0, 1, d + 1)

    # Se forman los pares: (datos[0], datos[1]), (datos[2], datos[3]), ... y se asignan a la celda correspondiente
    for i in range(num_pares):
        x = datos[2 * i]
        y = datos[2 * i + 1]
        # Se determina la celda usando np.searchsorted
        ix = np.searchsorted(limites, x, side='right') - 1
        iy = np.searchsorted(limites, y, side='right') - 1
        # Si el valor es exactamente 1, se asigna a la última celda
        if ix == d:
            ix = d - 1
        if iy == d:
            iy = d - 1
        tabla[ix, iy] += 1

    # Frecuencia esperada en cada celda: num_pares / (d^2)
    fe = num_pares / (d ** 2)
    # Cálculo del estadístico chi-cuadrado
    chi2_stat = np.sum((tabla - fe) ** 2 / fe)
    # Grados de libertad: (d - 1)^2
    gl = (d - 1) ** 2
    # Valor p (cola superior de la distribución chi-cuadrado)
    p_value = chi2.sf(chi2_stat, gl)

    return chi2_stat, p_value, tabla


def prueba_distancia_cuadratica(datos, num_clases=4):
    """
    Realiza la prueba de distancia cuadrática.

    Se forman pares consecutivos (por ejemplo, (x₁, x₂), (x₃, x₄), ...) y se calcula la diferencia
    absoluta de cada par. Se agrupan las diferencias en intervalos y se comparan con la distribución
    teórica de la diferencia absoluta entre dos variables U(0,1), cuya función de distribución es:
         F(d) = 2d – d²,  0 ≤ d ≤ 1.

    Parámetros:
        datos: lista o arreglo de números en [0,1]. Se espera que la cantidad de datos sea par.
        num_clases: número de clases (intervalos) en las cuales agrupar las diferencias (por defecto 4).
    Retorna:
        chi2_stat: estadístico chi-cuadrado calculado.
        p_value: valor p asociado.
        obs_frecuencias: arreglo con las frecuencias observadas en cada intervalo.
        exp_frecuencias: arreglo con las frecuencias esperadas en cada intervalo.
    """
    n = len(datos)
    if n % 2 != 0:
        n = n - 1
        datos = datos[:n]
    num_pares = n // 2

    # Se calculan las diferencias absolutas para cada par
    diferencias = []
    for i in range(num_pares):
        d_i = abs(datos[2 * i + 1] - datos[2 * i])
        diferencias.append(d_i)
    diferencias = np.array(diferencias)

    # Definición de los límites de los intervalos (por ejemplo, para num_clases=4, se usa [0, 0.25, 0.5, 0.75, 1])
    limites = np.linspace(0, 1, num_clases + 1)

    # Se cuentan las frecuencias observadas en cada intervalo
    obs_frecuencias, _ = np.histogram(diferencias, bins=limites)

    # Se calculan las frecuencias esperadas utilizando la función de distribución F(d) = 2d - d^2.
    # La probabilidad de que una diferencia se encuentre en el intervalo [a, b] es: F(b)-F(a)
    exp_frecuencias = []
    for i in range(num_clases):
        a = limites[i]
        b = limites[i + 1]
        prob = (2 * b - b ** 2) - (2 * a - a ** 2)
        exp_frecuencias.append(prob * num_pares)
    exp_frecuencias = np.array(exp_frecuencias)

    # Se calcula el estadístico chi-cuadrado
    chi2_stat = np.sum((obs_frecuencias - exp_frecuencias) ** 2 / exp_frecuencias)
    # Grados de libertad: número de clases - 1 (no se estiman parámetros)
    gl = num_clases - 1
    p_value = chi2.sf(chi2_stat, gl)

    return chi2_stat, p_value, obs_frecuencias, exp_frecuencias


def main():
    # Datos de entrada (se usan los 40 datos indicados)
    datos = [0.1569, 0.4617, 0.3166, 0.0235, 0.0552, 0.3047, 0.2842, 0.0769,
             0.5913, 0.9635, 0.8332, 0.4222, 0.8252, 0.0955, 0.912, 0.1744,
             0.0415, 0.1722, 0.9652, 0.1611, 0.5953, 0.4382, 0.2019, 0.0763,
             0.5821, 0.884, 0.1456, 0.1199, 0.4376, 0.1493, 0.229, 0.2441,
             0.9584, 0.853, 0.7609, 0.8968, 0.425, 0.0625, 0.3906, 0.2568]

    print("=== Prueba de Series ===")
    chi2_series, p_series, tabla = prueba_series(datos, d=2)
    print("Tabla de frecuencias observadas (matriz 2x2):")
    print(tabla)
    print(f"Estadístico Chi-cuadrado: {chi2_series:.4f}")
    print(f"Valor p: {p_series:.4f}")
    if p_series < 0.05:
        print("Resultado: Se rechaza la hipótesis de aleatoriedad (nivel de significancia 0.05).")
    else:
        print("Resultado: No se rechaza la hipótesis de aleatoriedad (nivel de significancia 0.05).")

    print("\n=== Prueba de Distancia Cuadrática ===")
    chi2_dist, p_dist, obs_freq, exp_freq = prueba_distancia_cuadratica(datos, num_clases=4)
    print("Frecuencias observadas por clase:")
    print(obs_freq)
    print("Frecuencias esperadas por clase:")
    print(exp_freq)
    print(f"Estadístico Chi-cuadrado: {chi2_dist:.4f}")
    print(f"Valor p: {p_dist:.4f}")
    if p_dist < 0.05:
        print("Resultado: Se rechaza la hipótesis de aleatoriedad (nivel de significancia 0.05).")
    else:
        print("Resultado: No se rechaza la hipótesis de aleatoriedad (nivel de significancia 0.05).")


if __name__ == "__main__":
    main()
