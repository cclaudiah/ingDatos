# Ing. de Datos - Modulo 2 - Clase 1
# Claudia Carrasco Herrera
#
# 1.  Investiga brevemente el lenguaje Python: 
#     ¿Qué lo hace especial? 
#     Es un lenguaje que su sintaxis es poco compleja, lo que ayuda para leer sin complicaciones el código. Para muchos es su primer lenguaje de programación. Python es un lenguaje de alto 
#     nivel, interpretado y multiplataforma
#     
#     ¿Para qué se usa principalmente?  
#     Es un lenguaje multipropósito utilizado por grandes empresas como Google, Netflix, Facebook y la NASA, diseñado con el claro propósito de ser accesible y fácil de aprender
#
#     ¿Cuáles son sus principales características?
#     - Es un lenguaje fácil de aprender
#     - Su código limpio y legible
#     - Posee muchas librerias
#     - Funciona en todos los sistemas (Windows, Mac, Linux, cloud)
#     - Tiene una comunidad enorme, lo cual ayuda para el feedback con problemas.
#
#     ¿Qué versión estás utilizando?
#     PS C:\Workspace\ingDatos> python --version
#     Python 3.11.5
#
# 2. La actividad será desarrollada en Visual Studio Code Version 1.100.3
#
# 3. Desarrollo del Script:
# 
# Crea un script con las siguientes funcionalidades:
# -   Declaración de al menos 4 variables (uno de cada tipo: entero, decimal, string, booleano).
# -   Uso de operadores aritméticos y lógicos.
# -   Solicita entrada del usuario para ingresar un nombre y una edad.
# -   Utiliza estructuras condicionales (if, elif, else) para imprimir diferentes mensajes:
#       -   Si es mayor de edad: “Acceso permitido”.
#       -   Si es menor de edad: “Acceso denegado”.
# -   Imprime mensajes con print() y documenta el código con comentarios.
# -   Aplica conversión de tipos si es necesario (int(), str(), etc).
#######################################################################################################

#Bienvenida al programa con print
print("Bienvenido al curso de Ing. de Datos")
print("Módulo 2 - Clase 1")

print("")
print("")

#Asignación de variable Entero, Boolean, Decimal, String
print("Variables")
tipo_entero = 16
is_boolean = True
tipo_decimal = 3.14159
tipo_string = "Ing. de Datos"

#Despliegue de las variables
print("Entero:", tipo_entero, "| Tipo:", type(tipo_entero))
print("Booleano:", is_boolean, "| Tipo:", type(is_boolean))
print("Decimal:", tipo_decimal, "| Tipo:", type(tipo_decimal))
print("Cadena de texto:", tipo_string, "| Tipo:", type(tipo_string))

print("")
print("")

#Ejemplo de operadores aritmeticos y lógicos

suma = tipo_entero + tipo_decimal

if (suma > 0):
    print("La suma de", tipo_entero, " y ",tipo_decimal, "es ", suma)
else:
    print("Esto nunca se imprimirá")

print("")
print("")

#Solicitud de datos al usuario, se maneja la conversión a int desde string
print("Validación Edad")
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Qué edad tienes? "))

#Si edad es menor a 18 acceso denegado, si no acceso permitido.
if edad < 18:
    print(f"{nombre} : Acceso denegado.")
else:
    print(f"{nombre} : Acceso permitido.")