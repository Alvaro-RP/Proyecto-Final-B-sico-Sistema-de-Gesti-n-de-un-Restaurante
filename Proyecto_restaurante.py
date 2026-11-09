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

def tomar_pedido(mesa, menu):
    pedidos = []

    for nCliente in range(1, mesa["clientes"] + 1):
        print(f"Cliente {nCliente} de la mesa {mesa['num_mesa']}")
        plato = ""

        while plato != "Eso es todo":
            plato = input(
                "¿Qué plato desea? Escriba 'Eso es todo' para terminar: "
            )

            if plato in menu:
                pedidos.append(plato)
            elif plato != "Eso es todo":
                print("El plato no está en el menú.")

    mesa["pedidos"] = pedidos
    mesa["atendida"] = True

def calcular_cuenta(mesa, menu):
    precio_total = 0

    for plato in mesa["pedidos"]:
        precio_total += menu[plato]

    mesa["cuenta"] = precio_total

    return precio_total

def cobrar_mesa(restaurante, num_mesa):
    for mesa in restaurante["mesas"]:
        if mesa["num_mesa"] == num_mesa:
            if not mesa["atendida"]:
                print("Esta mesa todavía no tiene pedido.")
                return

            total = calcular_cuenta(mesa, restaurante["menu"])

            restaurante["ganancias"] += total
            restaurante["ocupacion"] -= mesa["clientes"]
            restaurante["mesas"].remove(mesa)

            print(f"Mesa {num_mesa} cobrada: {total:.2f} €")
            print("La mesa ha quedado libre.")
            return

    print("No existe una mesa con ese número.")

# Funcion

# Punto de entrada

# if __name__ == '__main__':
   