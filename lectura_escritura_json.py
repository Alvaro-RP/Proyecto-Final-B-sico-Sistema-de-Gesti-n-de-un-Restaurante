import json


def cargar_restaurante(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        restaurante = json.load(archivo)

    restaurante["mesas"] = []
    restaurante["ocupacion"] = 0
    restaurante["ganancias"] = 0

    return restaurante

def cargar_grupos(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        grupos = json.load(archivo)

    if not isinstance(grupos, list):
        raise ValueError("El archivo debe contener una lista de grupos.")

    for grupo in grupos:
        if not isinstance(grupo, dict):
            raise ValueError("Cada grupo debe ser un diccionario.")

        clientes = grupo.get("clientes")

        if type(clientes) is not int or clientes <= 0:
            raise ValueError(
                "Cada grupo debe tener un número entero positivo de clientes."
            )

    return grupos