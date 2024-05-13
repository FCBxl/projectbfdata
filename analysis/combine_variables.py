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

def count_categories(row):
  counts = {}
  for col in df.columns[1:]:  # Skip the first column (country)
    value = row[col]  # Get the value from the current column
    if value == 1:  # Check if the value indicates a selection (assuming 1 represents selection)
      category_name = col.split('_')[1]  # Extract the category name from the column name
      if category_name in counts:
        counts[category_name] += 1  # Increment count for existing category
      else:
        counts[category_name] = 1  # Add new category with count 1
  return counts

