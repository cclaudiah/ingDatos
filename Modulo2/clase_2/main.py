# Ing. de Datos - Modulo 2 - Clase 1
# Claudia Carrasco Herrera
# 
# 1. Exploración de Funciones y Módulos:
# • Investiga y comenta brevemente en tu scrUna función es un bloque de código que realiza una tarea específica
#   - ¿Qué es una función en Python?
#     Una función es un bloque de código que realiza una tarea específica.
#
#   - ¿Qué es un módulo y para qué sirve?
#     Un módulo es un extracto de código que contiene funciones, clases, variables, etc. Se utiliza principalmente en programas grandes, el cual se divide en módulos para poder #     reutilizar código y para que sea más comprensible.

#   - ¿Qué ventajas tiene modularizar el código?
#     + Reutilizar el código y que no exista duplicidad.
#     + Código ordenado.
#     + Código más legible y mantención menos costosa.
#     + Muchos programadores pueden estar trabajando en el mismo proyecto.
#     
#   - ¿Qué es un docstring y cómo se usa?
#     Es una cadena de texto que documenta un módulo, clase o función. Explica qué hace el código, sus parámetros de entrada y retorno. Mejora el mantenimiento y colaboración del código.
#
# 2. Crea dos archivos:
# • operaciones.py: Contendrá las funciones matemáticas.
# • main.py: Programa principal que usará las funciones del módulo
#

"""
main.py

Codigo principal, importa funciones desde operaciones.py.

"""

#Se importan las funciones
from operaciones import mostrar_info, multiplicar, restar, sumar, potencia, factorial

print("Bienvenido al curso de Ing. de Datos")
print("Módulo 2 - Clase 2")

print("")
print("")

num_1 = int(input("Ingresa un numero  : "))
num_2 = int(input("Ingresa otro numero: "))

print("Funciones: ")
print(f"Sumar : {sumar(num_1, num_2)}")
print(f"Restar: {restar(num_1, num_2)}")
print(f"Multiplicar: {multiplicar(num_1, num_2)}")
print(f"Potencia: {potencia(num_1, num_2)}")
print(f"Factorial: {num_1} -> {factorial(num_1)}, {num_2} ->{factorial(num_1)}")

print("")
print("")

print("Ingresa los siguientes datos:")
nombre = input("Nombre: ")
curso  = input("Curso : ")
edad   = int(input("Edad  : "))
print("")
print("")

print("Datos ingresados:")
mostrar_info(nombre=nombre, curso=curso, edad=edad)