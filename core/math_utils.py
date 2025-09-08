"""
Operaciones matemáticas con funciones.
Integrante responsable: Elias Caranza
"""

import sympy as sp

def analizar_funcion(expr_str):
    """
    Recibe una función en formato string y retorna información:
    - Expresión simbólica
    - Dominio
    - Intersecciones con ejes
    """
    x = sp.symbols('x')

    try:
        expr = sp.sympify(expr_str)

        intersecciones_x = sp.solve(expr, x)
        interseccion_y = expr.subs(x, 0)

        dominio = sp.calculus.util.continuous_domain(expr, x, sp.S.Reals)

        return {
            "expr": expr,
            "dominio": dominio,
            "intersecciones_x": intersecciones_x,
            "interseccion_y": interseccion_y
        }

    except Exception as e:
        return {"error": str(e)}
