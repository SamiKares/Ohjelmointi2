import requests
import json

pyyntö = "https://api.chucknorris.io/jokes/random"
response = requests.get(pyyntö).json()
print(f"Päivän random fakta: {response['value']}")