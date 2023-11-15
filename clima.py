import requests
from pprint import pprint

city = input("Enter your city:  ")
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=1b81cdba152c5dc5d951066295360d1e".format(city)

res = requests.get(url)

# Imprimir la respuesta completa
pprint(res.json())

try:
    temp = res.json()["main"]["temp"]
    vel_viento = res.json()["wind"]["speed"]
    latitud = res.json()["coord"]["lat"]
    longitud = res.json()["coord"]["lon"]
    descripcion = res.json()["weather"][0]["description"]

    print("Temperatura: ", temp)
    print("Velocidad del viento: {} m/s".format(vel_viento))
    print("Latitud: {}".format(latitud))
    print("Longitud: {}".format(longitud))
    print("Descripción: {}".format(descripcion))

except KeyError as e:
    print("Error: Clave no encontrada - {}".format(e))
