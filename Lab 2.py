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

precio_medio = sum(lista_precios) / len(lista_precios)

print(lista_precios)

print(f"Numero de platos: {len(lista_precios)}\nPrecio medio: {precio_medio:.2f}")

############# EJERCICIO 2 ##############

precios_por_plato = {}

precios_por_plato[plato_1] = lista_precios[0]
precios_por_plato[plato_2] = lista_precios[1]
precios_por_plato[plato_3] = lista_precios[2]

print(precios_por_plato)
print("Precio de carne: ", precios_por_plato["carne"])

######### EJERCICIO 3 ##########

nombre_restaurante = "Casa Pepe"
aforo = 48

restaurante = {
    "Nombre" : nombre_restaurante,
    "Aforo" : aforo,
    "Menu" : precios_por_plato
}

print(restaurante)

cantidad_clientes = int(input("¿Cauntos clientes son? ", ))
pueden_entrar = cantidad_clientes <= aforo

print("¿Pueden entrar?", pueden_entrar)

########## EJERCICIO 4 ########
pedido_1 = str(input("Primer plato: ", ))
pedido_2 = str(input("Segundo plato: ", ))
pedido_3 = str(input("Tercer plato: ", ))

#################################################
assert(pedido_1) in restaurante["Menu"].keys()
assert(pedido_2) in restaurante["Menu"].keys()
assert(pedido_3) in restaurante["Menu"].keys()
#################################################

cantidad_pedido_1 = int(input("Cantidad primer plato: "))
cantidad_pedido_2 = int(input("Cantidad segundo plato: "))
cantidad_pedido_3 = int(input("Cantidad tercer plato: "))

print("Sopa en menu?: ", pedido_1 in restaurante["Menu"].keys())
print("Carne en menu?: ", pedido_2 in restaurante["Menu"].keys())
print("Pasta en menu?: ", pedido_3 in restaurante["Menu"].keys())

precio_total = cantidad_pedido_1 * restaurante["Menu"][pedido_1] + cantidad_pedido_2 * restaurante["Menu"][pedido_2] + cantidad_pedido_3 * restaurante["Menu"][pedido_3]
print("Precio total: ", precio_total)