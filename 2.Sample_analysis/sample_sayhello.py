import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path 

file_path = Path(__file__).parent
df_sample = pd.read_csv(Path(file_path, "sample_eurobarometer.csv"))

print(df_sample.head(8))


crosstabs = pd.crosstab(df_sample["d12at"], df_sample["most_used_media"])
#%%
# Group data by the variable on the x-axis (e.g., country)

#grouped_data = df_sample.groupby('d12at')['most_used_media'].value_counts().unstack()

# Create the stacked bar chart
#grouped_data.plot(kind='bar', stacked=True, colormap='Set2')  # Adjust colormap as desired
#plt.xlabel('City')
#plt.ylabel('citizens')
#plt.title('Age Group Distribution by Country')
#plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
#plt.tight_layout()
#plt.show()
#%%

# Get value counts for the categorical variable
value_counts = df_sample['device_used'].value_counts()

# Create the histogram
plt.figure(figsize=(6, 6))  # Adjust figure size as desired
value_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Device Used')
plt.ylabel('Count')
plt.title('Histogram of Category Counts')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
# %%

plt.style.use('_mpl-gallery')

# plot:
fig, ax = plt.subplots()

ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 56), yticks=np.linspace(0, 56, 9))

plt.show()