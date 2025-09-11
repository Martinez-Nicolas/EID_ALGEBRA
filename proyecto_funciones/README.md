# EID_ALGEBRA
EID - Algebra para la Computacion

# 📊 Proyecto: Analizador de Funciones

Este proyecto corresponde a la **Parte B** del trabajo de investigación de la asignatura *Álgebra para la Computación (MAT1185)*.  
El objetivo es crear una aplicación en Python con interfaz gráfica que permita analizar funciones matemáticas.

---

## 🚀 Funcionalidades
- Ingresar una función matemática (ejemplo: `x**2 + 2*x + 1`).
- Calcular dominio, recorrido e intersecciones con los ejes.
- Evaluar un punto dado en la función mostrando el paso a paso.
- Graficar la función con Matplotlib, resaltando intersecciones y el punto evaluado.
- Interfaz gráfica moderna con **CustomTkinter**.

---

## 👥 Integrantes y Roles

Elias Caranza → Backend matemático (core/math_utils.py)

Martin Sanhueza → Gráficas (core/plot_utils.py)

Diego Leiva → Interfaz gráfica (ui/interface.py)

Nicolas Martinez → GitHub, integración, documentación, pruebas

---

## 📂 Estructura del Proyecto
proyecto_funciones/
│── main.py
│── requirements.txt
│── README.md
│
├── core/
│ ├── math_utils.py # Operaciones matemáticas (Elias Caranza)
│ └── plot_utils.py # Gráficas (Martin Sanhueza)
│
├── ui/
│ └── interface.py # Ventana principal (Diego Leiva)
│
└── tests/
└── test_math_utils.py

---

## ⚙️ Instalación
1. Clona este repositorio mediante gitkraken:
   https://github.com/Martinez-Nicolas/EID_ALGEBRA.git

---

## Instalacion de dependencias
    pip install -r requirements.txt

---

## USO
python main.py

---