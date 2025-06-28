# Limpieza de datos

# Identificar valores faltantes (NaN) en un DataFrame.
# Eliminar o reemplazar datos nulos.
# Cambiar tipos de datos en columnas.
# Renombrar columnas y/o índices para mejorar la legibilidad.

# 1. Detección de valores nulos
# .isnull() y .notnull()

import pandas as pd

df = pd.read_csv("titanic.csv")

# Ver cuántos valores faltan por columna
# print(df.isnull().sum())

# Ver si hay algún valor nulo en la columna 'Age'
# print(df["Age"].isnull().head())


# 2. Eliminación e imputación de datos nulos
# Eliminar filas que tengan valores nulos en cualquier columna
df_sin_nulos = df.dropna()
# print(df_sin_nulos.isnull().sum())

# Eliminar solo si falta el valor en la columna 'Embarked'
df.dropna(subset=["Embarked"], inplace=True)
# print(df.isnull().sum())


# Reemplazar valores nulos con fillna
# Reemplazar nulos en la edad con la media

# Reemplazar nulos en la columna 'Embarked' con el valor más frecuente
# Toma el primer valor de la Serie de moda. Esto es necesario porque .mode() puede devolver más de un resultado.


modo_embarked = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(modo_embarked)
df["Age"] = df["Age"].fillna(df["Age"].mean())

# print(df.isnull().sum())


# Renombrar columnas

# Cambiar nombres de columnas
df.rename(columns={
    "Name": "Nombre",
    "Sex": "Sexo",
    "Age": "Edad"
}, inplace=True)

# print(df[["Nombre", "Sexo", "Edad"]].head())


