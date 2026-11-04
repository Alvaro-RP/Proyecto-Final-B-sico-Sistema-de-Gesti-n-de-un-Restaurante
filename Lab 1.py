# Ejercicio 1: Calcular precio de una comida

meal_price = 25
tax_rate = 0.21

total_cost = meal_price + meal_price * tax_rate

print("Precio total", total_cost, "€")

# Ejercicio 2: nombre del restaurante, aforo y menú con 3 platos principales (con precios)

restaurant_name = "El Castellano"
Aforo = 40
plato_1 = 8
plato_2 = 12
plato_3 = 5

print(f"{restaurant_name.upper()}\n Aforo: {Aforo}\n Menú:\n Croquetas de jamón...{plato_1}€\n Torreznos de Soria...{plato_2}€\n Patatas bravas...{plato_3}€\n")

# Ejercicio 3
meal_price = float(input("Total pagado en la comida: "))
tip = int(input("Propina: "))

meal_sin_impuestos = meal_price / 1.21

tip_rate = tip / meal_sin_impuestos

print(tip_rate * 100, "%")

# Ejercicio 4: Cuenta mesa grande

#Usando los precios del menú definidos en el Ejercicio 2, escribe un programa que 
#calcule el precio total de una mesa con varios comensales, en base a cuántos platos 
#han pedido. 
#Instrucciones: - Usa input() para leer cuántos platos de cada tipo han pedido (el programa debe 
#preguntárselo antes). - Convierte a enteros con int(). - Calcula el total y muestra el resultado con print().  

cantidad_plato1 = int(input("Cantidad de Croquetas: "))
cantidad_plato2 = int(input("Cantidad de Torreznos de Soria: "))
cantidad_plato3 = int(input("Cantidad de Patatas bravas: "))

total = cantidad_plato1 * plato_1 + cantidad_plato2 * plato_2 + cantidad_plato3 * plato_3

print(total)

# Ejercicio 5: Pago a partes iguales 

# Precio total de las consumiciones de cada comensal 

comensal_1_croquetas = int(input("Platos de croquetas comensal 1: "))
comensal_1_torreznos = int(input("Platos de torreznos comensal 1: "))
comensal_1_bravas = int(input("Platos de bravas comensal 1: "))

total_comensal_1 = comensal_1_croquetas * plato_1 + comensal_1_torreznos * plato_2 + comensal_1_torreznos * plato_3


comensal_2_croquetas = int(input("Platos de croquetas comensal 2: "))
comensal_2_torreznos = int(input("Platos de torreznos comensal 2: "))
comensal_2_bravas = int(input("Platos de bravas comensal 2: "))

total_comensal_2 = comensal_2_croquetas * plato_1 + comensal_2_torreznos * plato_2 + comensal_2_torreznos * plato_3


comensal_3_croquetas = int(input("Platos de croquetas comensal 3: "))
comensal_3_torreznos = int(input("Platos de torreznos comensal 3: "))
comensal_3_bravas = int(input("Platos de bravas comensal 3: "))

total_comensal_3 = comensal_3_croquetas * plato_1 + comensal_3_torreznos * plato_2 + comensal_3_torreznos * plato_3


total_comensales_pagar = (total_comensal_1 + total_comensal_2 + total_comensal_3) // 3

print("Cuanto debe pagar cada comensal: ", total_comensales_pagar, "€")


# Cuanto debería pagar cada comensal realmente

print("Comensal 1 debería pagar: ", total_comensal_1, "€")
print("Comensal 2 debería pagar: ", total_comensal_2, "€")
print("Comensal 3 debería pagar: ", total_comensal_3, "€")

# Diferencia de lo que ha pagado cada comensal con respecto a lo que deberían haber pagado

diferencia_comensal_1 = total_comensal_1 - total_comensales_pagar
diferencia_comensal_2 = total_comensal_2 - total_comensales_pagar
diferencia_comensal_3 = total_comensal_3 - total_comensales_pagar

print(f"Diferencia comensal 1: {diferencia_comensal_1}€\n Diferencia comensal 2: {diferencia_comensal_2}€\n Diferencia comensal 3: {diferencia_comensal_3}€")


# Cantidad sin pagar por el redondeo

cantidad_perdida = ((total_comensal_1 + total_comensal_2 + total_comensal_3) / 3) - total_comensales_pagar

print("Cantidad perdida: ", cantidad_perdida, "€")

# Reflexión: ¿Qué pasaría con nuestro código si tuviésemos 4 comensales en vez de 3? 
# Respuesta: Añadir una variable más debido al cuarto comensal y en vez de
# hacer la división entre 3 para ver cuánto debería pagar cada comensal se haría entre 4.