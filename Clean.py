import pandas as pd

df = pd.read_csv('netflix_titles.csv')

print("Head:")
print(df.head(10), "\n")

print("Lista:")
list = df.values.tolist()
for i in range(10):
    print(list[i])
    print()

print("Porcentaje de Valores Nulos por Columna:")
percent_missing = df.isnull().sum() * 100 / len(df)
missing_value_df = pd.DataFrame({'column_name': df.columns,
                                 'percent_missing': percent_missing})
print(missing_value_df, "\n")

print("Tipos:")
print(df.dtypes, "\n")

# Eliminar espacios en blanco al inicio de cada dato
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

print("Separar Fecha en 3 columnas:")
df['date_added'] = pd.to_datetime(df['date_added'])
df['day_added'] = df['date_added'].dt.day
df['month_added'] = df['date_added'].dt.month
df['year_added'] = df['date_added'].dt.year
print(df[['day_added', 'month_added', 'year_added']].head(10), "\n")

print("Llenar Valores Nulos:")
df2 = df.fillna("None")
df2.to_csv("df2.csv")
print(df2, "\n")
