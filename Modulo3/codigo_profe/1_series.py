import pandas as pd
# pip install pandas
# !pip install pandas

# print(pd.__version__)

# 1. ¿Qué es Pandas?
# Pandas es una biblioteca de Python para
# la manipulación y análisis de datos estructurados. 

#  Está construida sobre NumPy y proporciona estructuras
# como Series y DataFrame

# 2. ¿Qué es una Serie?
# Una Serie es una estructura unidimensional
# que puede contener datos de cualquier
# tipo (enteros, cadenas, flotantes, etc.),
# asociados a un índice (etiquetas).

#s = pd.Series([10, 20, 30, 40, 'as'])
#print(s)

# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 3. Índices personalizados
# Puedes cambiar las etiquetas del índice
# para que sean más significativas.
#d = pd.Series([25, 30, 22, 28])
#print(d)
#edades = pd.Series([25, 30, 22, 28], index=["Ana", "Luis", "Sofía", "Carlos"])
#print(edades)

# Ana       25
# Luis      30
# Sofía     22
# Carlos    28
# dtype: int64



# 4. Acceso a elementos
# Acceder por etiqueta
#print(edades["Luis"])  # 30

# Acceder por posición
#print(edades[2])       # WARNING 22
#print(edades.iloc[2])  # Correcto 22



# 5. Operaciones básicas
# Sumar 5 años a todas las edades
#print(edades + 5)

# Comparación booleana
# print(edades > 25)

# Filtrado
#print(edades[edades > 25])



# 6. Ejercicio

# 1. Crear una Serie con los precios de 4 frutas
precios = pd.Series([450, 300, 600, 520], index=["manzana", "banana", "kiwi", "pera"])

# 2. Mostrar la Serie completa
print("Precios de las frutas:")
print(precios)

# 3. Mostrar el precio del "kiwi"
print("\nPrecio del kiwi:")
print(precios["kiwi"])
print(f"El precio del {precios.index[2]} es: ${precios['kiwi']}")


# 4. Aumentar un 10% todos los precios
precios_actualizados = precios * 1.10
print("\nPrecios actualizados con 10% de aumento:")
print(precios_actualizados)

# 5. Mostrar solo las frutas cuyo precio sea mayor a $500
frutas_caras = precios_actualizados[precios_actualizados > 500]
# print("\nFrutas con precio mayor a $500:")
#print(frutas_caras)




