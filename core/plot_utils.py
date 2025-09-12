import matplotlib.pyplot as plt
import sympy as sp

def plot_function(
    func_or_expr,
    x_range=(-10, 10),
    num_points=400,
    eval_point=None,
    highlight_intersections=True,
    title="Gráfico de la función",
    xlabel="x",
    ylabel="f(x)",
    legend=True,
    figsize=(8,5),
    grid=True,
    color_func="#0055A4",
    color_xint="red",
    color_yint="green",
    color_eval="blue"
):
    x = sp.symbols('x')
    if isinstance(func_or_expr, sp.Basic):
        func = sp.lambdify(x, func_or_expr, "math")
        expr = func_or_expr
    elif callable(func_or_expr):
        func = func_or_expr
        expr = None
    else:
        raise ValueError("El argumento func_or_expr debe ser función o expresión SymPy.")

    x_min, x_max = x_range
    step = (x_max - x_min) / (num_points - 1)
    X = [x_min + i * step for i in range(num_points)]
    Y = []
    for xi in X:
        try:
            yi = func(xi)
            Y.append(float(yi))
        except Exception:
            Y.append(float('nan'))

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(X, Y, label=f"$f(x)$" if expr is None else f"$f(x) = {sp.latex(expr)}$", color=color_func, linewidth=2)

    ax.axhline(0, color="gray", linewidth=1, linestyle='--', zorder=0)
    ax.axvline(0, color="gray", linewidth=1, linestyle='--', zorder=0)

    labels_added = set()
    if highlight_intersections and expr is not None:
        # Intersección eje X (f(x)=0)
        x_ints = sp.solve(expr, x)
        for xi in x_ints:
            try:
                xi_val = float(xi)
                if x_min <= xi_val <= x_max:
                    lbl = "Intersección eje X" if "Intersección eje X" not in labels_added else None
                    ax.plot(xi_val, 0, "o", color=color_xint, label=lbl, markersize=8, zorder=3)
                    # Etiqueta con coordenadas
                    ax.text(xi_val, 0, f"({xi_val:.2f}, 0.00)", color=color_xint, fontsize=10, ha="left", va="bottom")
                    labels_added.add("Intersección eje X")
            except Exception:
                continue
        # Intersección eje Y (x=0)
        try:
            y_int = float(expr.subs(x,0))
            if x_min <= 0 <= x_max:
                lbl = "Intersección eje Y" if "Intersección eje Y" not in labels_added else None
                ax.plot(0, y_int, "o", color=color_yint, label=lbl, markersize=8, zorder=3)
                # Etiqueta con coordenadas
                ax.text(0, y_int, f"(0.00, {y_int:.2f})", color=color_yint, fontsize=10, ha="left", va="bottom")
                labels_added.add("Intersección eje Y")
        except Exception:
            pass

    # Punto evaluado (azul)
    if eval_point is not None and x_min <= eval_point <= x_max:
        try:
            y_eval = float(func(eval_point))
            lbl = f"Punto ({eval_point:.2f}, {y_eval:.2f})" if "Punto evaluado" not in labels_added else None
            ax.plot(eval_point, y_eval, "o", color=color_eval, label=lbl, markersize=8, zorder=3)
            # Etiqueta con coordenadas
            ax.text(eval_point, y_eval, f"({eval_point:.2f}, {y_eval:.2f})", color=color_eval, fontsize=10, ha="left", va="bottom")
            labels_added.add("Punto evaluado")
        except Exception:
            pass

    ax.set_xlabel(xlabel, fontsize=13)
    ax.set_ylabel(ylabel, fontsize=13)
    ax.set_title(title, fontsize=15, fontweight='bold')

    if legend:
        ax.legend(fontsize=11, loc='best', frameon=True)
    if grid:
        ax.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    return fig, ax

