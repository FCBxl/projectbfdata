import requests
import pandas as pd

# Replace with the actual URL of the xlsx file
url = "https://webgate.ec.europa.eu/ebsm/api/public/odp/download?key=0059645504327BE08E891398610B8ADC"

response = requests.get(url)

df = pd.read_excel("eurobarometerdata.xlsx")

