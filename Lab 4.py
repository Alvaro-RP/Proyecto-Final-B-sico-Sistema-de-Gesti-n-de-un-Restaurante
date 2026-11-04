# EJERCICIO 1
def crear_restaurante (nombre, aforo, menu, max_mesas = -1):
    restaurante = {
        'nombre' : nombre,
        'aforo' : aforo,
        'menu' : menu,
        'mesas' : [],
        'ocupacion' : 0
    }

    if max_mesas > 0:
        restaurante['max_mesas'] = max_mesas

    return restaurante

# EJERCICIO 2
def añadir_mesa (restaurante, clientes):
    if (restaurante['ocupacion'] + clientes) > restaurante['aforo']:
        print('[ERROR] No queda espacio para nuevos clientes')
        return
    
    if 'max_mesas' in restaurante and (len(restaurante['mesas'])) >= restaurante['max_mesas']:
        print('[ERROR] Se ha alcanzado el límite de mesas')
        return
    
    mesa = {
        'num_mesa' : len(restaurante['mesas']) + 1,
        'clientes' : clientes,
        'atendida' : False
    }

    restaurante['mesas'].append(mesa)
    restaurante['ocupacion'] += clientes

# EJERCICIO 3
def tomar_pedido(mesa, menu):
    pedidos = []

    for nCliente in range(1, mesa['clientes'] + 1):
        print(f'El cliente {nCliente} de la mesa {mesa['num_mesa']}')
        plato = ''
        
        while (plato != "Eso es todo"):
            plato = input('Que plato desea pedir')

            if plato in menu:
                pedidos.append(plato)
                
        mesa['pedidos'] = pedidos
        mesa['atendida'] = True

# EJERCICIO 4
def calcular_cuenta(mesa, menu):
    precio_total = 0

    for pedido in mesa['pedidos']:
        cuenta += menu[pedido]
        mesa['cuenta'] = precio_total

    return precio_total

# Ejercicio 5
def atender_todas_las_mesas(restaurante, menu):
    for mesa in restaurante['mesas']:
        if not mesa['atendida']:
            tomar_pedido(mesa, menu)
            calcular_cuenta(mesa, menu)


# EJERCICIO 6
if __name__ == '__main__':
    MENU = {
        'sopa' : 5,
        'pasta' : 8,
        'carne' : 12
    }

    restaurante = crear_restaurante('Casa Pepe', 50, MENU, 5)

    for i in range(4):
        añadir_mesa(restaurante, i + 1)

    atender_todas_las_mesas(restaurante, MENU)

    añadir_mesa(restaurante, 1)
    añadir_mesa(restaurante, 2)

    atender_todas_las_mesas(restaurante, MENU)

    print(restaurante['mesas'])   