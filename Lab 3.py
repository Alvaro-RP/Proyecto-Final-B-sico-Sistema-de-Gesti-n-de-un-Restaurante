### EJERCICIO 1

plato_1 = "carne"
plato_2 = "pasta"
plato_3 = "sopa"

precio_1 = int(input("Precio plato 1:", ))
precio_2 = int(input("Precio plato 2:", ))
precio_3 = int(input("Precio plato 3:", ))

lista_precios = []

lista_precios.append(precio_1)
lista_precios.append(precio_2)
lista_precios.append(precio_3)

precios_por_plato = {}

precios_por_plato[plato_1] = lista_precios[0]
precios_por_plato[plato_2] = lista_precios[1]
precios_por_plato[plato_3] = lista_precios[2]

nombre_restaurante = "Casa Pepe"
aforo = 48

restaurante = {
    "Nombre" : nombre_restaurante,
    "Aforo" : aforo,
    "Menu" : precios_por_plato
}

# Creamos la lista de mesas vacía

mesas = []

mesa_1 = {"num_mesa" : "1", "clientes" : 3, "atendida" : False}
mesa_2 = {"num_mesa" : "2", "clientes" : 4, "atendida" : False}

mesas.append(mesa_1)
mesas.append(mesa_2)

ocupation = 0

restaurante["Mesas"] = mesas

for mesa in restaurante["Mesas"]:
    ocupation += mesa["clientes"]

print("Ocupacion. ", ocupation)

restaurante["Ocupacion"] = ocupation

print(restaurante)

# EJ 2

clientes_nuevos = int(input("Cuantos clientes nuevos son? ", ))

if (restaurante["Ocupacion"] + clientes_nuevos) < restaurante["Aforo"]:
    mesa_nueva = {"num_mesa": len(restaurante["Mesas"]) + 1, "clientes": clientes_nuevos, "atendida": False}
    restaurante["Mesas"].append(mesa_nueva)
else: 
    print("No hay espacio")

print(restaurante)

# EJ 3

mesa_actual = mesas[-1]

solicitudes_list = []

while len(solicitudes_list) < mesa_actual["clientes"]:
    pregunta_camarero = input("Que desean pedir? ", )
    if pregunta_camarero in restaurante["Menu"]:
        solicitudes_list.append(pregunta_camarero)
    if pregunta_camarero not in restaurante["Menu"]:
        print("Plato no esta en el menu")
    if len(solicitudes_list) == mesa_actual["clientes"]:
        mesa_actual["pedidos"] = solicitudes_list
        mesa_actual["atendida"] = True

print(mesa_actual)

## EJ 4

cuenta = 0

for platos in mesa_actual["pedidos"]:
    if platos in restaurante["Menu"]:
        cuenta += restaurante["Menu"][platos]
        mesa_actual["Cuenta"] = cuenta

print(mesa_actual)

# EJ 5

pedidos_totales = []
clientes_sin_atender = 0

for mesas in restaurante["Mesas"]:
    if mesas["atendida"] == False:
        clientes_sin_atender += mesas["clientes"]
        while len(pedidos_totales) < clientes_sin_atender:
            pide_plato = input("Que desea pedir? ", )
            if pide_plato in restaurante["Menu"]:
                pedidos_totales.append(pide_plato)
            if pide_plato not in restaurante["Menu"]:
                print("Pedido no está en el menu, haga otro ", )
            if len(pedidos_totales) == clientes_sin_atender:
                mesas["atendida"] = True
                
print(restaurante["Mesas"])