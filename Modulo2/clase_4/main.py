"""
Introducción a la Programación Orientada a Objeto
"""
# 1️. Exploración Inicial:
# o ¿Qué es la Programación Orientada a Objetos?
#       La Programación Orientada a Objetos (POO) es un paradigma que permite modelar el mundo real utilizando "objetos". 
#       Cada objeto combina datos (atributos) y funciones (métodos) en una estructura llamada clase.
#
# o ¿Cuáles son sus cuatro principios fundamentales?
#       1. Abstracción: Ocultar detalles internos
#       2. Encapsulamiento: Proteger datos del objeto
#       3. Herencia: Reutilizar código entre clases
#       4. Polimorfismo: Comportamientos distintos según contexto
#
# o ¿Qué ventajas aporta la POO frente a la programación estructurada?
#        - Ayuda a organizar mejor el código.
#        - Promueve la reutilización de código.
#        - Facilita el mantenimiento de aplicaciones complejas. 
#        - Se trabaja pensando en entidades que interactúan entre sí (clases).
#
# 2️. Definición de Clases:
# • Crea una clase Usuario con:
# o Atributos: nombre, correo, _contraseña (privado).
# o Métodos: saludar(), mostrar_info().
# o Constructor que inicialice todos los atributos.
# o Getters y setters para la contraseña usando decoradores.
#
# Nota: 
# Se debe crear un objeto a partir de la clase Usuario y utilizar sus métodos.
#
# Opcional:
# Crear una nueva clase que herede de "Usuario" e instanciar un objeto a partir de la nueva clase.

from usuario import Usuario
from cliente import Cliente

print("")
# Se crea el objeto Usuario y se utilizan sus metodos: saludar , mostrar_info , setter
usuario = Usuario("Claudia Carrasco", "claudia.carrascoh@gmail.com", "password")
print("Método saludar")
usuario.saludar()

print("Método mostrar_info")
usuario.mostrar_info()
print("")
print("Uso de setter")
nueva_pass = input("Ingresa nueva contraseña: ")
usuario.contrasena = nueva_pass
print("")
print("Nueva info")
usuario.mostrar_info()

#Se instancia nueva clase Cliente
print("")
print("Nueva Clase hija")
cliente = Cliente("Leo Muzzio", "leito@gmail.com", "pass", "cliente frecuente")
cliente.saludar()