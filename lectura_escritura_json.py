import json


def leer_json(ruta):
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos


def guardar_restaurante(ruta, restaurante):

    datos = {
        "nombre": restaurante["nombre"],
        "capacidad": restaurante["capacidad"],
        "mesas_max": restaurante["mesas_max"],
        "menu": restaurante["menu"]
    }
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
