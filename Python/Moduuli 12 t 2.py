import requests
import json
kaupunki = input("Anna kaupunki")
tiedustelu =f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&lang=fi&appid=43f03023725685797c211f067be0bfe8&units=metric"
vastaus = requests.get(tiedustelu).json()
#print(json.dumps(vastaus, indent=2))
print(f'Sää kaupungissa: {vastaus["name"]}, tällä hetkellä: {vastaus["weather"][0]["description"]} ja lämpötila: {vastaus["main"]["temp"]} celsiusta')