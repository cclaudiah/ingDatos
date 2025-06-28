# Carga y guardado de archivos
# Leer archivos CSV y Excel (pd.read_csv, pd.read_excel)# 
# Guardar datos a CSV y Excel (.to_csv, .to_excel)

# 1. Cargar un archivo CSV

import pandas as pd

# Cargar el archivo Titanic
df = pd.read_csv("titanic.csv")

# Mostrar las primeras 5 filas
print(df.head())


# 2. Exploración inicial del DataFrame

# print(df.info())       # Información general del DataFrame
# print(df.shape)        # Tamaño: (filas, columnas)
# print(df.columns)      # Lista de columnas
# print(df.describe())   # Estadísticas para columnas numéricas


# 3. Limpieza básica posterior a la carga

# Ver cuántos valores faltantes hay por columna
# print(df.isnull().sum())

# Rellenar valores faltantes en la edad con la media
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())

# Eliminar filas donde falta el puerto de embarque
# df.dropna(subset=["Embarked"], inplace=True)


# Guardar un nuevo archivo CSV
df.to_csv("titanic_limpio.csv", index=False)

# También podrías guardarlo como Excel
df.to_excel("titanic_limpio.xlsx", index=False)





