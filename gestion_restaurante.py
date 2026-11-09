# Importaciones
from lectura_escritura_json import (
    cargar_restaurante,
    cargar_grupos,
    guardar_restaurante
)

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

def dividir_cuenta(mesa, menu):
    total = calcular_cuenta(mesa, menu)
    total_centimos = round(total * 100)

    pago_base = total_centimos // mesa["clientes"]
    centimos_restantes = total_centimos % mesa["clientes"]

    print(f"Cuenta total: {total:.2f} €")
    print("Número de clientes:", mesa["clientes"])

    for cliente in range(1, mesa["clientes"] + 1):
        pago = pago_base

        if cliente <= centimos_restantes:
            pago += 1

        print(f"Cliente {cliente}: {pago / 100:.2f} €")

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

def ampliar_menu(restaurante, ruta):
    nombre = input("Nombre del plato: ")

    if nombre in restaurante["menu"]:
        print("El plato ya existe. Se actualizará su precio.")

    precio_valido = False

    while not precio_valido:
        try:
            precio = float(input("Precio del plato: "))

            if 0 < precio < float("inf"):
                precio_valido = True
            else:
                print("Introduce un precio positivo")

        except ValueError:
            print("Introduce un número válido.")

    restaurante["menu"][nombre] = precio
    guardar_restaurante(ruta, restaurante)

    print("El menú se ha actualizado y guardado.")

def consultar_estado(restaurante):
    print("\n--- ESTADO DEL RESTAURANTE ---")
    print("Nombre:", restaurante["nombre"])
    print("Capacidad:", restaurante["aforo"])
    print("Máximo de mesas:", restaurante["max_mesas"])
    print("Ocupación actual:", restaurante["ocupacion"])

    print("\n--- MESAS ACTIVAS ---")

    if not restaurante["mesas"]:
        print("No hay mesas ocupadas.")

    for mesa in restaurante["mesas"]:
        print("\nMesa:", mesa["num_mesa"])
        print("Clientes:", mesa["clientes"])

        if mesa["atendida"]:
            print("Estado: con pedido")
        else:
            print("Estado: pendiente de pedido")

        print("Pedidos:", mesa["pedidos"])
        print("Cuenta:", mesa["cuenta"])

    print("\n--- MENÚ ---")

    for plato, precio in restaurante["menu"].items():
        print(f"{plato}: {precio:.2f} €")

    print(f"\nGanancias de la noche: {restaurante['ganancias']:.2f} €")