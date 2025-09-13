from sympy import symbols, sympify, SympifyError, solve, S, Reals, oo, solveset

def analizar_expresion(expresion: str):
    x = symbols('x')
    if not expresion:
        raise ValueError("La expresión no puede estar vacía.")
    expresion_limpia = expresion.lower().replace('^', '**').replace('pi', 'pi').replace('e', 'E')
    try:
        funcion = sympify(expresion_limpia)
        if x not in funcion.free_symbols and funcion.free_symbols:
            raise ValueError("La expresión contiene variables no soportadas.")
        return funcion, x
    except (SympifyError, SyntaxError) as e:
        raise ValueError(f"Error al parsear la función: {e}. Asegúrate de que la sintaxis es correcta.")

def evaluar_punto(funcion, valor_x):
    x = symbols('x')
    valor_x_simbolico = S(valor_x)
    try:
        paso_a_paso_str = f"Sustituyendo x por {valor_x} en la función:\n"
        paso_a_paso_str += f"f(x) = {funcion}\n"
        resultado = funcion.subs(x, valor_x_simbolico)
        paso_a_paso_str += f"f({valor_x}) = {resultado}\n"
        return paso_a_paso_str, resultado
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error al evaluar la función en x={valor_x}: {e}.")

def encontrar_intersecciones(funcion, x):
    intersecciones_x = []
    interseccion_y = None
    justificacion = ""
    try:
        # Intersección con eje X (f(x)=0)
        soluciones = solve(funcion, x)
        intersecciones_x = [float(sol.evalf()) for sol in soluciones if hasattr(sol, 'is_real') and sol.is_real]
        justificacion += f"Se resuelve f(x)=0 para encontrar intersecciones con X: {soluciones}\n"
        # Intersección con eje Y (x=0)
        interseccion_y = funcion.subs(x, 0)
        justificacion += f"Se evalúa f(0) para intersección con Y: {interseccion_y}\n"
    except Exception as e:
        justificacion += f"Error al calcular intersecciones: {e}\n"
    return intersecciones_x, interseccion_y, justificacion

def analizar_dominio_recorrido(funcion, x):
    dominio_str = "Todos los números reales (-∞, +∞)"
    justificacion = "La función es polinómica, por lo tanto su dominio son todos los reales."
    if funcion.is_rational_function(x):
        numerador, denominador = funcion.as_numer_denom()
        raices_denominador = solveset(denominador, x, domain=Reals)
        if raices_denominador.is_finite_set:
            puntos_a_excluir = ', '.join(map(str, sorted(list(raices_denominador))))
            dominio_str = f"Todos los números reales excepto: {{{puntos_a_excluir}}}"
            justificacion = f"El denominador se anula en x = {puntos_a_excluir}, por lo tanto esos puntos se excluyen del dominio."
    # Recorrido (simplificado)
    recorrido_str = "Cálculo avanzado no disponible para esta función."
    return dominio_str, recorrido_str, justificacion