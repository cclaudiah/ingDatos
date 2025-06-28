import pandas as pd
# 1. ¿Qué es un DataFrame?
# Un DataFrame es una estructura
# bidimensional (tabla) de Pandas,
# similar a una hoja de Excel o una tabla SQL.

# 2. Crear un DataFrame
# Desde un diccionario:
data = {
    "Nombre": ["Ana", "Luis", "Marta", "Carlos"],
    "Edad": [25, 30, 22, 28],
    "Ciudad": ["Santiago", "Valparaíso", "Temuco", "Concepción"]
}

df = pd.DataFrame(data)
print(df.set_index("Nombre"))
# print(df)

# Desde una lista de listas:
datos = [
    ["Ana", 25, "Santiago"],
    ["Luis", 30, "Valparaíso"],
    ["Marta", 22, "Temuco"]
]
print(df.loc[df['Nombre'] == 'Juan'])

df2 = pd.DataFrame(datos, columns=["Nombre", "Edad", "Ciudad"])
# print(df2)

# print(df.head())      # Primeras 5 filas
# print(df.tail(2))     # Últimas 2 filas
# print(df.shape)       # (filas, columnas)
# print(df.columns)     # Nombres de las columnas
# print(df.dtypes)      # Tipos de datos por columna



# data = {
#     "Nombre": ["Ana", "Luis", "Marta", "Carlos"],
#     "Edad": [25, 30, 22, 28],
#     "Ciudad": ["Santiago", "Valparaíso", "Temuco", "Concepción"]
# }
# df = pd.DataFrame(data)

# 4. Acceso a columnas y filas
# print(df["Edad"])
# print(df[["Edad", "Nombre"]])


# Acceder a una fila por índice:
# print(df.loc[1])    # Por etiqueta del índice (valor 1), Funciona incluso si el índice no es numérico
# print(df.iloc[1])   # Por posición


# 5. Selección y filtrado de datos

# Filtrar por condición
mayores_25 = df[df["Edad"] > 25]
# print(mayores_25)

# Seleccionar múltiples columnas
print(df[["Nombre", "Ciudad"]])