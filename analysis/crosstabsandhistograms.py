import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path 

file_path = Path(__file__).parent
df = pd.read_excel(Path(file_path, "newbarometerdata_clean.xlsx"))

categorical_column = df["most_used_device"]

value_bar = df[categorical_column].value_counts()

plt.bar(value_bar.index, value_bar.values)
plt.xlabel(categorical_column)
plt.ylabel('Count')
plt.title('Distribution of {}'.format(categorical_column))
plt.xticks(rotation=45)  # Rotate x-axis labels for readability if many categories
plt.show()


attitude_news_values = df["q8_news_follow_frequency"].value_counts

plt.bar(value_bar.index, value_bar.values)
plt.xlabel(attitude_news_values)
plt.ylabel('Count')
plt.title('Distribution of {}'.format(attitude_news_values))
plt.xticks(rotation=45)  # Rotate x-axis labels for readability if many categories
plt.show()