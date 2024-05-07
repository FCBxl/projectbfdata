import pandas as pd

df = pd.read_csv("newbarometerdata.csv")
columns_to_drop = [1,5]
df_revised = df.drop(columns_to_drop)
print(df_revised)

