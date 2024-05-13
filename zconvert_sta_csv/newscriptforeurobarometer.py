import pandas as pd
import matplotlib
import numpy


df = pd.read_stata("Eurobarometerdata.dta")

print (df.head)

df.to_csv('newbarometerdata.csv', index=False)