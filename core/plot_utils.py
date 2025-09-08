"""
Gráficas con Matplotlib.
Integrante responsable: Martin Sanhueza
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def graficar_funcion(expr, x_val=None, intersecciones=None):
    """
    Grafica la función y marca intersecciones + punto evaluado.
    """
    x = sp.symbols('x')
    f = sp.lambdify(x, expr, "numpy")

    X = np.linspace(-10, 10, 400)
    Y = f(X)

    plt.figure(figsize=(6,4))
    plt.plot(X, Y, label=f"f(x) = {expr}")

    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)

    if intersecciones:
        for xi in intersecciones.get("intersecciones_x", []):
            if xi.is_real:
                plt.plot(float(xi), 0, "ro", label="Intersección eje X")
        plt.plot(0, float(intersecciones.get("interseccion_y", 0)), "go", label="Intersección eje Y")

    if x_val is not None:
        y_val = f(x_val)
        plt.plot(x_val, y_val, "bo", label=f"Punto ({x_val},{y_val})")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfico de la función")
    plt.legend()
    plt.grid(True)
    plt.show()
