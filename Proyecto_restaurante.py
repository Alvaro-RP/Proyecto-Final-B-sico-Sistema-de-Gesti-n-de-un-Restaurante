import os
from lectura_escritura_json import leer_json
from gestion_restaurante import (
    cargar_peticiones,
    tomar_pedido,
    cobrar_mesa,
    ampliar_menu,
    consultar_estado,
    dividir_cuenta
)


def mostrar_menu():
    print("\n--- GESTIÓN DEL RESTAURANTE ---")
    print("1. Cargar restaurante")
    print("2. Cargar nuevas peticiones de grupos")
    print("3. Tomar un pedido")
    print("4. Cobrar y liberar una mesa")
    print("5. Ampliar el menú")
    print("6. Consultar estado")
    print("7. Salir")
    opcion = input("Elige una opción: ")
    return opcion


def elegir_mesa(restaurante, atendida):
    # Enseña solo las mesas con ese estado y devuelve la que elija el usuario
    disponibles = []
    for mesa in restaurante["mesas"]:
        if mesa["atendida"] == atendida:
            disponibles.append(mesa)
            print("Mesa", mesa["num_mesa"], "-", mesa["clientes"], "clientes")

    if len(disponibles) == 0:
        print("No hay mesas disponibles para esta opción.")
        return None

    numero = input("Número de mesa: ")
    for mesa in disponibles:
        if str(mesa["num_mesa"]) == numero:
            return mesa

    print("Mesa no válida.")
    return None


def main():
    restaurante = None
    ruta_restaurante = None
    opcion = ""

    while opcion != "7":
        opcion = mostrar_menu()

        if opcion == "1":
            try:
                archivos = []
                for nombre in os.listdir("restaurante"):
                    if nombre.endswith(".json"):
                        archivos.append(nombre)

                for i in range(len(archivos)):
                    print(i + 1, archivos[i])

                seleccion = int(input("Elige un archivo: "))

                if 1 <= seleccion <= len(archivos):
                    ruta_restaurante = "restaurante/" + archivos[seleccion - 1]
                    restaurante = leer_json(ruta_restaurante)
                    restaurante["mesas"] = []
                    restaurante["ocupacion"] = 0
                    restaurante["ganancias"] = 0
                    print("Restaurante cargado:", restaurante["nombre"])
                else:
                    print("Selección no válida.")
            except (OSError, ValueError, KeyError):
                print("No se pudo cargar el restaurante.")

        elif opcion == "7":
            print("Programa cerrado.")

        elif opcion not in ["2", "3", "4", "5", "6"]:
            print("Opción no válida.")

        # A partir de aquí todas las opciones necesitan un restaurante cargado
        elif restaurante is None:
            print("Primero debes cargar un restaurante.")

        elif opcion == "2":
            ruta = input("Ruta del JSON de grupos: ")
            try:
                cargar_peticiones(restaurante, ruta)
            except (OSError, ValueError, KeyError, TypeError):
                print("No se pudieron cargar los grupos.")

        elif opcion == "3":
            mesa = elegir_mesa(restaurante, False)
            if mesa is not None:
                tomar_pedido(mesa, restaurante["menu"])

        elif opcion == "4":
            mesa = elegir_mesa(restaurante, True)
            if mesa is not None:
                cobrar_mesa(restaurante, mesa)

        elif opcion == "5":
            try:
                ampliar_menu(restaurante, ruta_restaurante)
            except OSError:
                print("No se pudo guardar el menú.")

        elif opcion == "6":
            consultar_estado(restaurante)


if __name__ == "__main__":
    main()
