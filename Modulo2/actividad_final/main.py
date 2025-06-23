"""
Sistema de Gestión de libros, usuarios y préstamos
"""
# Objetivo:
# Desarrollar una aplicación en Python aplicando funciones, estructuras de datos, POO y manejo de errores para gestionar 
# libros, usuarios y préstamos de forma automatizada.
# 
# Contexto:
# La empresa DataSolutions Academy, dedicada a la formación continua de profesionales en áreas tecnológicas, ha lanzado una nueva 
# plataforma educativa enfocada en el aprendizaje autónomo. Una de sus unidades, llamada “Biblioteca Digital para Ingenieros de Datos”, 
# necesita una aplicación interna que permita gestionar libros, usuarios y préstamos de manera automatizada y escalable.
# Hasta ahora, todo el proceso se realizaba manualmente, lo que ha provocado errores frecuentes, pérdida de información y lentitud en la 
# atención a estudiantes. Por ello, se ha decidido desarrollar una aplicación en Python que permita:
#   • Registrar y consultar libros según diferentes criterios (autor, género, disponibilidad).
#   • Registrar usuarios y diferenciar su rol (por ejemplo: estudiante, instructor).
#   • Gestionar préstamos de libros con validación de disponibilidad.
#   • Controlar errores como préstamos duplicados o usuarios no registrados.
# La aplicación debe ser simple, clara y robusta, aplicando los conocimientos adquiridos en este módulo.
#
# Instrucciones:
# Desarrolla un programa en Python que cumpla con los siguientes requerimientos:
# 1. Estructura General
#   o El proyecto debe estar organizado en módulos.
#   o Todo el código debe estar comentado y documentado (usando docstrings y comentarios tipo PEP8).
# 2. Funciones
#   o Uso de funciones definidas por el usuario para dividir la lógica del programa.
#   o Empleo de funciones con argumentos, retorno de valores, argumentos por defecto y argumentos variables.
# 3. Estructuras de Datos
#   o Uso de listas y diccionarios para almacenar información de libros y usuarios.
#   o Uso de tuplas o sets donde sea apropiado.
# 4. Programación Orientada a Objetos
#   o Definición de clases para representar libros, usuarios y préstamos.
#   o Uso de atributos, métodos y constructores.
#   o Implementación de herencia para diferenciar tipos de usuarios.
#   o Aplicación de polimorfismo en métodos comunes.
# 5. Manejo de Excepciones
#   o Uso de estructuras try-except para capturar y gestionar errores comunes como:
#       ▪ Libro no encontrado
#       ▪ Usuario no registrado
#   ▪ Préstamo duplicado
# 6. Operaciones del sistema (Ejecutables desde menú):
#   o Registrar nuevo libro
#   o Registrar nuevo usuario
#   o Consultar libros por autor, género o disponibilidad
#   o Realizar un préstamo
#   o Listar libros prestados

""" Clase principal con el menu"""

from funciones import registrar_libro, registrar_usuario, consultar_libro, realizar_prestamo, listar_prestados;

opc = 1

while opc != 0:
    print("\nBiblioteca Digital para Ingenieros de Datos.\n")
    print("1. Registrar nuevo libro")
    print("2. Registrar nuevo usuario")
    print("3. Consultar libros")
    print("4. Realizar un préstamo")
    print("5. Listar préstamos activos")
    print("0. Salir\n")

    opc = int(input("Selecciona opción: "))

    if (opc == 1) :
        registrar_libro()
    elif (opc ==2) :
        registrar_usuario()
    elif (opc == 3) :
        consultar_libro()
    elif (opc ==4) :
        realizar_prestamo()
    elif (opc ==5) :
        listar_prestados()
    else :
        opc =opc