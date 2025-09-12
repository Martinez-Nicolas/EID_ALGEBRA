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
    ctk.set_appearance_mode("dark")   # "light" o "system" también
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Analizador de Funciones")
    app.geometry("500x400")

    # Etiqueta principal
    lbl_titulo = ctk.CTkLabel(app, text="Analizador de Funciones", font=("Arial", 20))
    lbl_titulo.pack(pady=10)

    # Entrada de función
    lbl_funcion = ctk.CTkLabel(app, text="Función f(x):")
    lbl_funcion.pack()
    entry_funcion = ctk.CTkEntry(app, width=300, placeholder_text="Ejemplo: x**2 + 2*x + 1")
    entry_funcion.pack(pady=5)

    # Entrada de valor x
    lbl_x = ctk.CTkLabel(app, text="Valor de x (opcional):")
    lbl_x.pack()
    entry_x = ctk.CTkEntry(app, width=150, placeholder_text="Ejemplo: 2")
    entry_x.pack(pady=5)

    # Label para resultados
    lbl_resultados = ctk.CTkLabel(app, text="", justify="left")
    lbl_resultados.pack(pady=10)

    # Acción de análisis
    def ejecutar():
        expr = entry_funcion.get()
        x_val_str = entry_x.get()

        # Usar analizar_expresion en vez de analizar_funcion
        try:
            funcion, x = analizar_expresion(expr)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        # Aquí deberías llamar a las funciones para obtener dominio, intersecciones, etc.
        from core.math_utils import analizar_dominio_recorrido, encontrar_intersecciones

        dominio, recorrido = analizar_dominio_recorrido(funcion, x)
        intersecciones_x, interseccion_y = encontrar_intersecciones(funcion, x)

        texto = f"Dominio: {dominio}\n"
        texto += f"Intersecciones con X: {intersecciones_x}\n"
        texto += f"Intersección con Y: {interseccion_y}\n"
        lbl_resultados.configure(text=texto)

        x_val = None
        if x_val_str:
            try:
                x_val = float(x_val_str)
            except:
                messagebox.showerror("Error", "x debe ser un número válido")
                return

        # Usar plot_function en vez de graficar_funcion
        try:
            import matplotlib.pyplot as plt
            fig, ax = plot_function(funcion, eval_point=x_val)
            plt.show()
        except Exception as e:
            messagebox.showerror("Error al graficar", str(e))

    # Botón analizar
    btn_analizar = ctk.CTkButton(app, text="Analizar función", command=ejecutar)
    btn_analizar.pack(pady=15)

    # Loop principal
    app.mainloop()
