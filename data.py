import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv("animal_data_dirty1.csv", sep=";")

# Diagnóstico
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Animal type"].value_counts())
print(df["Country"].value_counts())

# Eliminar duplicados
df = df.drop_duplicates()

# Corregir animales
df["Animal type"] = df["Animal type"].replace({
    "red squirrell": "red squirrel",
    "red squirel": "red squirrel",
    "lynx?": "lynx",
    "European bison™": "European bison",
    "European buster": "European bison",
    "European bisson": "European bison",
    "ledgehod": "hedgehog",
    "wedgehod": "hedgehog"
})

# Corregir países
df["Country"] = df["Country"].replace({
    "PL": "Poland",
    "HU": "Hungary",
    "Hungry": "Hungary",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "Czech": "Czech Republic",
    "Australia": "Desconocido",
    "CC": "Desconocido"
})

# Datos faltantes
df["Animal type"] = df["Animal type"].fillna("Desconocido")
df["Country"] = df["Country"].fillna("Desconocido")
df["Gender"] = df["Gender"].fillna("not determined")
df["Animal name"] = df["Animal name"].fillna("Sin nombre")

# Datos numéricos
df["Weight kg"] = df["Weight kg"].fillna(df["Weight kg"].median())
df["Body Length cm"] = df["Body Length cm"].fillna(df["Body Length cm"].median())

# Corregir valores negativos
df.loc[df["Weight kg"] <= 0, "Weight kg"] = df["Weight kg"].median()
df.loc[df["Body Length cm"] <= 0, "Body Length cm"] = df["Body Length cm"].median()

# Convertir fecha
df["Observation date"] = pd.to_datetime(
    df["Observation date"],
    format="mixed",
    dayfirst=True
)

# NumPy
df["Tipo de peso"] = np.where(
    df["Weight kg"] > 10,
    "Pesado",
    "Ligero"
)

print("Peso promedio:", np.mean(df["Weight kg"]))

# Groupby
print(df.groupby("Animal type").size())
print(df.groupby("Animal type")["Weight kg"].mean())
print(df.groupby("Country")["Body Length cm"].mean())
print(df.groupby("Country").size())

# Comprobar limpieza
print("Duplicados finales:", df.duplicated().sum())
print("Valores faltantes finales:")
print(df.isnull().sum())