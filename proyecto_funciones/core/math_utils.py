from sympy import symbols, sympify, SympifyError, solve, S, Reals, oo, solveset
from sympy.parsing.latex import parse_latex

def analizar_expresion(expresion: str):

    x = symbols('x')
    
    if not expresion:
        raise ValueError("La expresión no puede estar vacía.")
    
    expresion_limpia = expresion.lower().replace('^', '**').replace('pi', 'sympy.pi').replace('e', 'sympy.E')
    
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
        paso_a_paso_str = f"Sustituyendo x por {valor_x} en la función: f({valor_x}) = {funcion.subs(x, valor_x_simbolico)}"
        
        resultado = funcion.subs(x, valor_x_simbolico)
        
        if resultado.is_real:
            valor_resultado = float(resultado)
            paso_a_paso_str += f"\nCalculando: f({valor_x}) = {valor_resultado}"
            return valor_resultado, paso_a_paso_str
        else:
            raise ValueError("La evaluación resultó en un número complejo.")
            
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error al evaluar la función en x={valor_x}: {e}.")
    
def encontrar_intersecciones(funcion, x):

    intersecciones_x = []
    interseccion_y = None
    
    try:
        interseccion_y = funcion.subs(x, 0)
        
        soluciones_x = solveset(funcion, x, domain=Reals)
        
        if soluciones_x.is_finite_set:
            intersecciones_x = [float(sol) for sol in soluciones_x]
        
    except Exception as e:
        raise ValueError(f"Error al calcular las intersecciones: {e}")
        
    return intersecciones_x, interseccion_y


def analizar_dominio_recorrido(funcion, x):

    dominio_str = "Todos los números reales (-∞, +∞)"
    recorrido_str = "Cálculo avanzado no disponible para esta función."
    
    if funcion.is_polynomial(x) or funcion.is_exponential(x):
        return dominio_str, recorrido_str
        
    if 'sqrt' in str(funcion):
        argumento_raiz = None
        for arg in funcion.args:
            if arg.func == 'sqrt':
                argumento_raiz = arg.args[0]
                break
        
        if argumento_raiz:
            dominio_set = solveset(argumento_raiz >= 0, x, domain=Reals)
            dominio_str = str(dominio_set).replace('(', '[').replace(')', ']') 
    
    if funcion.is_racional_function(x):
        try:
            numerador, denominador = funcion.as_numero_denom()
            
            raices_denominador = solveset(denominador, x, domain=Reals)
            
            if raices_denominador.is_finite_set:
                puntos_a_excluir = ', '.join(map(str, sorted(list(raices_denominador))))
                dominio_str = f"Todos los números reales excepto: {{{puntos_a_excluir}}}"
            
        except Exception as e:
            pass 
            
    return dominio_str, recorrido_str