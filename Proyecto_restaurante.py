## Hacer un random para cuantos clientes / meas van en un día (al final del proyecto si da timepo)

# Importaciones
from lectura_escritura_json import cargar_restaurante, cargar_grupos

# Funciones definidas
def añadir_mesa(restaurante, clientes):
    if type(clientes) is not int or clientes <= 0:
        print("[ERROR] El número de clientes debe ser un entero positivo.")
        return

    if restaurante["ocupacion"] + clientes > restaurante["aforo"]:
        print("[ERROR] No queda espacio para nuevos clientes.")
        return

    if len(restaurante["mesas"]) >= restaurante["max_mesas"]:
        print("[ERROR] Se ha alcanzado el límite de mesas.")
        return

    num_mesa = 1
    numeros_ocupados = [
        mesa["num_mesa"] for mesa in restaurante["mesas"]
    ]

    while num_mesa in numeros_ocupados:
        num_mesa += 1

    mesa = {
        "num_mesa": num_mesa,
        "clientes": clientes,
        "cuenta": 0,
        "atendida": False,
        "pedidos": []
    }

    restaurante["mesas"].append(mesa)
    restaurante["ocupacion"] += clientes

    print(f"Mesa {num_mesa} añadida para {clientes} clientes.")

def cargar_peticiones(restaurante, ruta):
    grupos = cargar_grupos(ruta)

    for grupo in grupos:
        añadir_mesa(restaurante, grupo["clientes"])


# Funcion

# Punto de entrada

if __name__ == '__main__':
    print