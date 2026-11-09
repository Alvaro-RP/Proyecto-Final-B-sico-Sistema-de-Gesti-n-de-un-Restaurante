# Importaciones

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
    opcion = ""

    while opcion != "7":
        opcion = mostrar_menu()

        if opcion == "7":
            print("Programa cerrado.")
        elif opcion in ("1", "2", "3", "4", "5", "6"):
            print("Opción pendiente de conectar.") # MODIFICAR
        else:
            print("Opción no válida.")



# PuntO de entrada
if __name__ == '__main__':
    main()
   