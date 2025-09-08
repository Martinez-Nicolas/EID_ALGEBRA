"""
Archivo principal del proyecto.
Aquí se integra la lógica (core) con la interfaz (ui).
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui.interface import iniciar_interfaz

def main():
    print("=== Analizador de Funciones ===")
    iniciar_interfaz()

if __name__ == "__main__":
    main()
