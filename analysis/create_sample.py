#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path 

file_path = Path(__file__).parent
df = pd.read_excel(Path(file_path, "newbarometerdata_clean.xlsx"))
# %%

ages = df["age"].value_counts()

# %%

df["age"] = pd.to_numeric(df['age'], errors='coerce')
# %%
print(ages)

# %%

df_sample = df.head(500)
df_sample.to_csv("sample_eurobarometer.csv", index=False)

# %%
