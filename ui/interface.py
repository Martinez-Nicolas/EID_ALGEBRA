"""
Interfaz gráfica (CustomTkinter).
Integrante responsable: Diego Leiva
"""

import customtkinter as ctk
from tkinter import messagebox
from core.math_utils import analizar_expresion
from core.plot_utils import plot_function

def iniciar_interfaz():
    """
    Crea la ventana principal del programa con CustomTkinter.
    """
    # Apariencia general
    ctk.set_appearance_mode("dark")   # "light" o "system" también
    ctk.set_default_color_theme("blue")
    try:
        ctk.set_widget_scaling(1.05)  # leve escalado para mejor legibilidad
    except Exception:
        pass

    app = ctk.CTk()
    app.title("Analizador de Funciones")
    app.geometry("640x520")
    app.minsize(560, 480)

    # ---------- Contenedor principal ----------
    container = ctk.CTkFrame(app, corner_radius=16, fg_color=("gray90", "gray15"))
    container.pack(fill="both", expand=True, padx=16, pady=16)

    # ---------- Título ----------
    lbl_titulo = ctk.CTkLabel(
        container, text="Analizador de Funciones",
        font=("Arial", 22, "bold")
    )
    lbl_titulo.pack(pady=(12, 6))

    # ---------- Descripción breve ----------
    hint = ctk.CTkLabel(
        container,
        text="Ingresa una expresión en x (ej:  x**2 + 2*x + 1 )\n"
             "Opcionalmente indica un valor numérico para evaluar.",
        justify="center",
        text_color=("gray40", "gray70"),
        font=("Arial", 12)
    )
    hint.pack(pady=(0, 10))

    # ---------- Card de entradas ----------
    card_inputs = ctk.CTkFrame(container, corner_radius=14)
    card_inputs.pack(fill="x", padx=12, pady=8)

    # Fila función
    fila1 = ctk.CTkFrame(card_inputs, fg_color="transparent")
    fila1.pack(fill="x", padx=12, pady=(12, 6))
    lbl_funcion = ctk.CTkLabel(fila1, text="Función f(x):", width=110)
    lbl_funcion.pack(side="left")
    entry_funcion = ctk.CTkEntry(
        fila1, width=420, placeholder_text="Ejemplo: x**2 + 2*x + 1"
    )
    entry_funcion.pack(side="left", padx=(8, 0))

    # Fila x
    fila2 = ctk.CTkFrame(card_inputs, fg_color="transparent")
    fila2.pack(fill="x", padx=12, pady=(0, 12))
    lbl_x = ctk.CTkLabel(fila2, text="Valor de x (opcional):", width=160)
    lbl_x.pack(side="left")
    entry_x = ctk.CTkEntry(
        fila2, width=180, placeholder_text="Ejemplo: 2"
    )
    entry_x.pack(side="left", padx=(8, 0))

    # ---------- Botonera ----------
    actions = ctk.CTkFrame(container, fg_color="transparent")
    actions.pack(pady=6)
    # Acción de análisis
    def ejecutar():
        expr = entry_funcion.get().strip()
        x_val_str = entry_x.get().strip()

        if not expr:
            messagebox.showwarning("Falta información", "Debes ingresar una expresión para f(x).")
            entry_funcion.focus_set()
            return

        # Usar analizar_expresion en vez de analizar_funcion
        try:
            funcion, x = analizar_expresion(expr)
        except Exception as e:
            messagebox.showerror("Error al analizar", f"No se pudo analizar la expresión.\n\nDetalle: {e}")
            return

        # Cálculos (dominio, recorrido e intersecciones)
        try:
            from core.math_utils import analizar_dominio_recorrido, encontrar_intersecciones
            dominio, recorrido = analizar_dominio_recorrido(funcion, x)
            intersecciones_x, interseccion_y = encontrar_intersecciones(funcion, x)
        except Exception as e:
            messagebox.showerror("Cálculo fallido", f"Ocurrió un error durante los cálculos.\n\nDetalle: {e}")
            return

        texto = f"• Dominio: {dominio}\n"
        texto += f"• Recorrido: {recorrido}\n"
        texto += f"• Intersecciones con X: {intersecciones_x}\n"
        texto += f"• Intersección con Y: {interseccion_y}\n"
        lbl_resultados.configure(text=texto)

        x_val = None
        if x_val_str:
            try:
                x_val = float(x_val_str)
            except:
                messagebox.showerror("Dato inválido", "x debe ser un número válido (ej: 2, 3.14, -1).")
                return

        # Usar plot_function en vez de graficar_funcion
        try:
            import matplotlib.pyplot as plt
            fig, ax = plot_function(funcion, eval_point=x_val)
            fig.canvas.manager.set_window_title("Gráfico de f(x)")
            plt.show()
        except Exception as e:
            messagebox.showerror("Error al graficar", str(e))

    btn_analizar = ctk.CTkButton(actions, text="Analizar función", command=ejecutar)
    btn_analizar.pack(side="left", padx=6)

    # Botón limpiar (nuevo, no cambia variables existentes)
    def _limpiar():
        entry_funcion.delete(0, "end")
        entry_x.delete(0, "end")
        lbl_resultados.configure(text="")
        entry_funcion.focus_set()

    btn_limpiar = ctk.CTkButton(actions, text="Limpiar", fg_color=("gray80", "gray25"), command=_limpiar)
    btn_limpiar.pack(side="left", padx=6)

    # ---------- Resultados ----------
    card_results = ctk.CTkFrame(container, corner_radius=14)
    card_results.pack(fill="both", expand=True, padx=12, pady=(8, 0))

    header_res = ctk.CTkLabel(card_results, text="Resultados", font=("Arial", 16, "bold"))
    header_res.pack(anchor="w", padx=12, pady=(12, 6))

    lbl_resultados = ctk.CTkLabel(
        card_results,
        text="",
        justify="left",
        anchor="w"
    )
    lbl_resultados.pack(fill="x", padx=12, pady=(0, 12))

    # ---------- Pie de página ----------
    footer = ctk.CTkLabel(
        container,
        text="Tip: presiona Enter para Analizar • Ctrl+L para Limpiar",
        text_color=("gray50", "gray65"),
        font=("Arial", 11)
    )
    footer.pack(pady=(6, 0))

    # ---------- Accesos rápidos ----------
    app.bind("<Return>", lambda e: ejecutar())
    app.bind("<Control-l>", lambda e: _limpiar())

    # Foco inicial
    entry_funcion.focus_set()

    # Loop principal
    app.mainloop()
