"""
Estructuras de Datos e Iteraciones en Python
"""

print("Bienvenido al curso de Ing. de Datos")
print("Módulo 2 - Clase 3")

print("BLOQUE 1: – Listas y Listas Anidadas")
print("")

# BLOQUE 1: – Listas y Listas Anidadas:
#Crea una lista con al menos 5 elementos de diferentes tipos.

numEntero = 16
numDecimal = 3.14
texto = "cadena"
isBoolean = True
nulo = None

lista = [numEntero, numDecimal, texto, isBoolean, nulo]

print("Valores de la lista:", lista)

# Agrega y elimina un elemento

# agregar
nuevo_elemento = "nuevo elemento"
lista.append(nuevo_elemento)
print("Se agrega a la lista: ", nuevo_elemento)
print("Lista con elemento agregado:", lista)

# eleminiar
lista.remove(numEntero) 
print("Se elimina a la lista: ", numEntero)
print("Lista con elemento eliminado: ", lista)

# Accede al primer y último elemento.
print("Primer objeto: ", lista[0])
print("Ultimo objeto: ", lista[-1])

# Crea una lista anidada (matriz de 3x3) e imprime su segunda fila.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Segunda fila equivale a indice 1
print("Segunda linea de la matriz: ", matriz[1])

# BLOQUE 2: – Diccionarios y Diccionarios Anidados:
#Crea un diccionario con datos de un estudiante (nombre, edad, carrera).
print("")
print("BLOQUE 2: – Diccionarios y Diccionarios Anidados")

estudiante = {
    "nombre": "Clau",
    "edad": 36,
    "carrera": "Ing de Datos"
}

# Agrega una clave notas con una lista de 3 notas.
estudiante['notas'] = lista = [7.0, 6.1, 6.5]
# Imprime la segunda nota y la carrera del estudiante.
print("Segunda nota:", estudiante["notas"][1])
print("Carrera:", estudiante["carrera"])

# BLOQUE 3 – Tuplas y Empaquetado/Desempaquetado:
print("")
print("BLOQUE 3 – Tuplas y Empaquetado/Desempaquetado:")
# Crea una tupla con datos de un libro (título, autor, año).
libro = ("Harry Potter y la Piedra Filosofal", "J. K. Rowling", "1997")

# Desempaqueta la tupla en tres variables.
titulo, autor, anno = libro

# Imprime una frase usando los datos desempaquetados.
print(f"El libro {titulo} fue escrito por {autor} en el año {anno}")

# BLOQUE 4 – Sets y Operaciones de Conjunto:
print("")
print("BLOQUE 4 – Sets y Operaciones de Conjunto")

# Crea dos conjuntos con elementos duplicados y elimina los duplicados.
numeros_impar     = {1, 1, 3, 5, 7, 9}
numeros_primarios = {1, 2, 2, 3, 5, 7}
print("numeros impar:", numeros_impar)
print("numeros primarios:", numeros_primarios)

# Realiza e imprime la intersección y la unión de ambos conjuntos.
print("Interseccion:", numeros_impar & numeros_primarios)
print("Union:", numeros_impar | numeros_primarios)

# BLOQUE 5 – Iteraciones:
print("")
print("BLOQUE 5 – Iteraciones")

# Itera una lista de nombres usando for e imprime un saludo para cada uno.
lista_familia = ["Claudia", "Leonardo", "Erick"]

for nombre in lista_familia:
    print(f"Hola {nombre}")

# Usa range para imprimir los números del 1 al 10.
for i in range(1,11):
    print(f"Numero: {i}")

# Itera un diccionario imprimiendo las claves y los valores.
# Se utiliza mismo diccionario del bloque 2
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# Usa un ciclo while para sumar los números del 1 al 5.
suma = 0
cont = 1
while cont <= 5:
    suma = suma + cont
    cont = cont + 1
print("Suma de 1 al 5:", suma)