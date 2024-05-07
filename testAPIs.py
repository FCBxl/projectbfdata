import requests
import json

response = requests.get("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/DEMO_R_D3DENS?lang=EN")
data = json.loads(response.text)

print(response.text)
print(type(data))
