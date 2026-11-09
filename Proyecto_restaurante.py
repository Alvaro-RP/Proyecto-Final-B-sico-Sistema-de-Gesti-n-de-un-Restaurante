# Importaciones
import os
from lectura_escritura_json import cargar_restaurante
from gestion_restaurante import (
    cargar_peticiones,
    tomar_pedido,
    cobrar_mesa
)


# Funciones definidas
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

                for numero, nombre in enumerate(archivos, 1):
                    print(numero, nombre)

                seleccion = int(input("Elige un archivo: "))

                if 1 <= seleccion <= len(archivos):
                    ruta = "restaurante/" + archivos[seleccion - 1]
                    restaurante = cargar_restaurante(ruta)
                    ruta_restaurante = ruta
                    print("Restaurante cargado:", restaurante["nombre"])
                else:
                    print("Selección no válida.")

            except (OSError, ValueError, TypeError, KeyError):
                print("No se pudo cargar el restaurante.")

        elif opcion == "2":
            if restaurante is None:
                print("Primero debes cargar un restaurante.")
            else:
                ruta = input("Ruta del JSON de grupos: ")

                try:
                    cargar_peticiones(restaurante, ruta)
                except (OSError, ValueError, TypeError, KeyError):
                    print("No se pudieron cargar los grupos.")

        elif opcion == "3":
            if restaurante is None:
                print("Primero debes cargar un restaurante.")
            else:
                pendientes = []

                for mesa in restaurante["mesas"]:
                    if not mesa["atendida"]:
                        pendientes.append(mesa)
                        print(
                            "Mesa:", mesa["num_mesa"],
                            "Clientes:", mesa["clientes"]
                        )

                if len(pendientes) == 0:
                    print("No hay mesas pendientes de pedido.")
                else:
                    try:
                        numero = int(input("Número de mesa: "))
                        mesa_elegida = None

                        for mesa in pendientes:
                            if mesa["num_mesa"] == numero:
                                mesa_elegida = mesa

                        if mesa_elegida is None:
                            print("Mesa no válida.")
                        else:
                            tomar_pedido(
                                mesa_elegida,
                                restaurante["menu"]
                            )

                    except ValueError:
                        print("Introduce un número de mesa válido.")

        elif opcion == "4":
            if restaurante is None:
                print("Primero debes cargar un restaurante.")
            else:
                servidas = []

                for mesa in restaurante["mesas"]:
                    if mesa["atendida"]:
                        servidas.append(mesa)
                        print(
                            "Mesa:", mesa["num_mesa"],
                            "Clientes:", mesa["clientes"]
                        )

                if len(servidas) == 0:
                    print("No hay mesas con pedido para cobrar.")
                else:
                    try:
                        numero = int(input("Número de mesa a cobrar: "))
                        mesa_elegida = None

                        for mesa in servidas:
                            if mesa["num_mesa"] == numero:
                                mesa_elegida = mesa

                        if mesa_elegida is None:
                            print("Mesa no válida.")
                        else:
                            cobrar_mesa(restaurante, numero)

                    except ValueError:
                        print("Introduce un número de mesa válido.")

        elif opcion == "7":
            print("Programa cerrado.")

        elif opcion in ("5", "6"):
            if restaurante is None:
                print("Primero debes cargar un restaurante.")
            else:
                print("Opción pendiente de conectar.")

        else:
            print("Opción no válida.")



# PuntO de entrada
if __name__ == '__main__':
    main()
   