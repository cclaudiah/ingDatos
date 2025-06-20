"""
Herencia y Excepciones en Python
"""
# 1️. Exploración inicial (como comentarios en el script):
# • Explica brevemente qué es la herencia y por qué es útil.
#       La herencia es uno de los pilares fundamentales de la Programación Orientada a Objetos (POO). 
#       Permite crear nuevas clases basadas en clases existentes, reutilizando su código y extendiendo sus funcionalidades.
#
# • Describe qué es una excepción y cómo ayuda a manejar errores en los programas.
#        Una excepción es un error que ocurre durante la ejecución de un programa. Si no se maneja, el programa se detiene abruptamente.
#
# • Incluye una lista de los dunder methods más comunes que conoces.
#       Los dunder methods son métodos especiales que empiezan y terminan con doble guion bajo __
#       -  __init__
#       -  __str__
#       -  __mro__
#
# 2️. Definición de clases y jerarquía:
# • Crea una clase Usuario con los atributos nombre, correo, activo=True.
# • Crea un método presentarse() que imprima el nombre del usuario.
# • Crea una subclase Administrador que herede de Usuario, añadiendo:
#   o Atributo adicional: permisos (lista de strings).
#   o Método sobrescrito presentarse() que también muestre sus permisos.
#   o Método agregar_permiso().
# • Crea una clase SuperUsuario que herede de Administrador y otra clase llamada Soporte, simulando herencia múltiple.
#   o Incluye un ejemplo que imprima __mro__.
#
# 3️. Uso de polimorfismo y sobrecarga:
# • Crea una función mostrar_usuario(usuario) que funcione con cualquier tipo de objeto (Usuario, Administrador, etc.).
# • Implementa una función con parámetros por defecto o *args para simular sobrecarga.
#
# 4️. Implementación de excepciones:
# • Crea una excepción personalizada PermisoInsuficienteError.
# • En el método agregar_permiso, lanza esta excepción si el usuario no tiene rol "administrador".
# • Implementa bloques try-except para capturar ValueError y tu excepción personalizada.
# • Usa finally para imprimir un mensaje final.

from usuario import Usuario
from administrador import Administrador
from super_usuario import SuperUsuario
from error_personalizado import PermisoInsuficienteError

print(f"Bienvenida al curso de Ing. de Datos.")
print("Módulo 2 - Clase 5")
print("")
# Se crea el objeto Usuario y utiliza metodo presentarse
usuario = Usuario("Claudia Carrasco", "claudia.carrascoh@gmail.com", False)

# Se crea el objeto Administrador y utiliza metodo presentarse
lista_permisos = ["consultar", "firmar", "eliminar", "modificar", "administrador"]
administrador = Administrador("Leo Muzzio", "leito@gmail.com", True, lista_permisos)

# Se crea el objeto SuperUsuario y __mro__
print("Clase SuperUsuario y __mro__")
print(SuperUsuario.__mro__)

# Uso de polimorfismo
def mostrar_usuario(usuario):
    usuario.presentarse()

print("\nMetodo: mostrar_usuario()")
mostrar_usuario(usuario)
mostrar_usuario(administrador)

# Uso de sobrecarga
def saludar(*args):
    if not args:
        print("No vienen datos.")
    elif isinstance(args[0], Administrador):
        print(f"Nombre: {administrador.nombre}, Correo: {administrador.correo}")
    elif isinstance(args[0], Usuario):
        print(f"Nombre: {usuario.nombre}")
    else:
        print("Dato ingresado no corresponde")

saludar()
saludar(usuario)
saludar(administrador)
saludar("prueba")

try:
    print("\nAgregar permiso")
    #prueba con un administrador con permiso
    administrador.agregar_permiso("lectura")
    mostrar_usuario(administrador)

    print("\nAgregar permiso sin el rol administrador")
    lista_permisos.remove("administrador")
    admin = Administrador("Erick Muzzio", "erick@gmail.com", False, lista_permisos)
    admin.agregar_permiso("lectura")
except PermisoInsuficienteError as e:
    print(f"Error {e}")
finally:
    print("\nFinally")