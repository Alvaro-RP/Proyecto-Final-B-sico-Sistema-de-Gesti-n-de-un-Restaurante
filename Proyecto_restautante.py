## Hacer un random para cuantos clientes / meas van en un día (al final del proyecto si da timepo)

# Importaciones
import json

with open("datos_restaurante.json", "r") as archivo:
    datos_restaurante = json.load(archivo)

# Funciones definidas
def mesas(num_mesa, clientes, cuenta, pedidos):
    mesas = {
        'num_mesa':num_mesa,
        'clientes': clientes,
        'cuenta': cuenta,
        'atendida': False,
        'pedidos': pedidos
    }

    mesas_list = []
    mesas_list.append(mesas)
    variable = "borrar"


# Funcion

# Punto de entrada

if __name__ == '__main__':
    print