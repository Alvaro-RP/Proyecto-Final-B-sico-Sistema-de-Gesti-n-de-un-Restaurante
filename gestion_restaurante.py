from lectura_escritura_json import leer_json, guardar_restaurante


def añadir_mesa(restaurante, clientes):
    if clientes <= 0:
        print("[ERROR] El número de clientes tiene que ser positivo.")
        return

    if restaurante["ocupacion"] + clientes > restaurante["capacidad"]:
        print("[ERROR] No queda espacio para nuevos clientes.")
        return

    if len(restaurante["mesas"]) >= restaurante["mesas_max"]:
        print("[ERROR] Se ha alcanzado el límite de mesas.")
        return

    numeros_ocupados = []
    for mesa in restaurante["mesas"]:
        numeros_ocupados.append(mesa["num_mesa"])

    num_mesa = 1
    while num_mesa in numeros_ocupados:
        num_mesa += 1

    mesa = {
        "num_mesa": num_mesa,
        "clientes": clientes,
        "atendida": False,
        "pedidos": []
    }
    restaurante["mesas"].append(mesa)
    restaurante["ocupacion"] += clientes
    print(f"Mesa {num_mesa} añadida para {clientes} clientes.")


def cargar_peticiones(restaurante, ruta):
    grupos = leer_json(ruta)
    for grupo in grupos:
        añadir_mesa(restaurante, grupo["clientes"])


def tomar_pedido(mesa, menu):
    pedidos = []

    for n_cliente in range(1, mesa["clientes"] + 1):
        print(f"Cliente {n_cliente} de la mesa {mesa['num_mesa']}")
        plato = ""

        while plato != "Eso es todo":
            plato = input("¿Qué plato desea? (escriba 'Eso es todo' para terminar): ")

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
    return precio_total


def dividir_cuenta(total, clientes):
    por_persona = round(total / clientes, 2)
    ultimo = round(total - por_persona * (clientes - 1), 2)

    for n_cliente in range(1, clientes):
        print(f"Cliente {n_cliente}: {por_persona:.2f} €")
    print(f"Cliente {clientes}: {ultimo:.2f} €")


def cobrar_mesa(restaurante, mesa):
    total = calcular_cuenta(mesa, restaurante["menu"])
    print(f"Total de la mesa {mesa['num_mesa']}: {total:.2f} €")

    respuesta = input("¿Desean dividir la cuenta entre los clientes? (s/n): ")
    if respuesta.lower() == "s":
        dividir_cuenta(total, mesa["clientes"])

    restaurante["ganancias"] += total
    restaurante["ocupacion"] -= mesa["clientes"]
    restaurante["mesas"].remove(mesa)

    print(f"Mesa {mesa['num_mesa']} cobrada. La mesa ha quedado libre.")


def ampliar_menu(restaurante, ruta):
    nombre = input("Nombre del plato: ")

    if nombre in restaurante["menu"]:
        print("El plato ya existe. Se actualizará su precio.")

    precio_valido = False
    while not precio_valido:
        try:
            precio = float(input("Precio del plato: "))
            if precio > 0:
                precio_valido = True
            else:
                print("El precio tiene que ser positivo.")
        except ValueError:
            print("Introduce un número válido.")

    restaurante["menu"][nombre] = precio
    guardar_restaurante(ruta, restaurante)
    print("El menú se ha actualizado y guardado.")


def consultar_estado(restaurante):
    print("\n--- ESTADO DEL RESTAURANTE ---")
    print("Nombre:", restaurante["nombre"])
    print("Capacidad:", restaurante["capacidad"])
    print("Máximo de mesas:", restaurante["mesas_max"])
    print("Ocupación actual:", restaurante["ocupacion"])

    print("\n--- MESAS ACTIVAS ---")
    if len(restaurante["mesas"]) == 0:
        print("No hay mesas ocupadas.")

    for mesa in restaurante["mesas"]:
        if mesa["atendida"]:
            estado = "con pedido"
        else:
            estado = "pendiente de pedido"
        print(f"Mesa {mesa['num_mesa']}: {mesa['clientes']} clientes, {estado}")
        print("   Pedidos:", mesa["pedidos"])
        print(f"   Cuenta: {calcular_cuenta(mesa, restaurante['menu']):.2f} €")

    print("\n--- MENÚ ---")
    for plato in restaurante["menu"]:
        print(f"{plato}: {restaurante['menu'][plato]:.2f} €")

    print(f"\nGanancias de la noche: {restaurante['ganancias']:.2f} €")
