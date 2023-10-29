import requests
import json

url = "https://maptiles.p.rapidapi.com/es/map/v1/3/4/2.png"

headers = {
	"X-RapidAPI-Key": "98937ae092msh8bd9c048d80fa91p11f2d9jsn40f4e7aadc11",
	"X-RapidAPI-Host": "maptiles.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print(response.json())