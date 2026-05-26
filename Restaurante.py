# ---------------------------------------------------------
# Nombre del estudiante: Luis Daniel Alarcón Cañizalez
# Grupo: 213022_965
# Programa: Ingeniería Electrónica
# Código Fuente: Autoría propia 
# ---------------------------------------------------------
# =====================================
# SISTEMA DE MENU RESTAURANTE
# =====================================

# MATRIZ DE PRODUCTOS
# [Nombre, Categoria, Precio]

productos = [
    ["Pizza Hawaiana", "Pizza", 28000],
    ["Pizza Ranchera", "Pizza", 32000],
    ["Hamburguesa", "Comida Rapida", 22000],
    ["Ensalada Cesar", "Saludable", 18000],
    ["Wrap Vegetariano", "Saludable", 26000],
    ["Jugo Natural", "Bebida", 9000]
]

# LISTA PARA GUARDAR LA FACTURA
factura = []


# =====================================
# FUNCION PARA MOSTRAR PRODUCTOS
# =====================================

def mostrar_menu():

    print("\n========== MENU ==========")

    for i in range(len(productos)):

        print(i + 1, ".",
              productos[i][0],
              "- Categoria:",
              productos[i][1],
              "- Precio: $",
              productos[i][2])


# =====================================
# FUNCION PARA MOSTRAR PROMOCIONES
# =====================================

def mostrar_promociones(dia):

    print("\n====== PROMOCIONES ======")

    if dia == "martes" or dia == "jueves":

        print("15% de descuento en pizzas")
        print("Aplica para precios mayores a $25000")

    elif dia == "domingo":

        print("20% de descuento en comida saludable")
        print("Aplica para precios mayores a $20000")

    else:

        print("No hay promociones disponibles")


# =====================================
# FUNCION PARA CALCULAR DESCUENTO
# =====================================

def calcular_descuento(producto, dia):

    categoria = producto[1]
    precio = producto[2]

    descuento = 0

    # DESCUENTO EN PIZZAS
    if (dia == "martes" or dia == "jueves"):

        if categoria == "Pizza" and precio > 25000:

            descuento = precio * 0.15

    # DESCUENTO EN COMIDA SALUDABLE
    elif dia == "domingo":

        if categoria == "Saludable" and precio > 20000:

            descuento = precio * 0.20

    precio_final = precio - descuento

    return precio_final, descuento


# =====================================
# FUNCION PARA AGREGAR PRODUCTOS
# =====================================

def agregar_producto(dia):

    mostrar_menu()

    opcion = int(input("\nIngrese el numero del producto: "))

    if opcion >= 1 and opcion <= len(productos):

        producto = productos[opcion - 1]

        cantidad = int(input("Ingrese la cantidad: "))

        precio_final, descuento = calcular_descuento(producto, dia)

        subtotal = precio_final * cantidad

        factura.append([
            producto[0],
            cantidad,
            producto[2],
            descuento,
            subtotal
        ])

        print("Producto agregado correctamente")

    else:

        print("Opcion no valida")


# =====================================
# FUNCION PARA MOSTRAR FACTURA
# =====================================

def mostrar_factura():

    total = 0

    print("\n========== FACTURA ==========")

    if len(factura) == 0:

        print("No hay productos agregados")

    else:

        for i in range(len(factura)):

            print("\nProducto:", factura[i][0])
            print("Cantidad:", factura[i][1])
            print("Precio base: $", factura[i][2])
            print("Descuento: $", factura[i][3])
            print("Subtotal: $", factura[i][4])

            total = total + factura[i][4]

        print("\nTOTAL A PAGAR: $", total)


# =====================================
# FUNCION PARA ELIMINAR PRODUCTO
# =====================================

def eliminar_producto():

    mostrar_factura()

    if len(factura) > 0:

        opcion = int(input("\nIngrese el numero del producto a eliminar: "))

        if opcion >= 1 and opcion <= len(factura):

            factura.pop(opcion - 1)

            print("Producto eliminado")

        else:

            print("Opcion incorrecta")


# =====================================
# PROGRAMA PRINCIPAL
# =====================================

print("================================")
print(" SISTEMA DE RESTAURANTE ")
print("================================")

dia = input("Ingrese el dia actual: ").lower()

opcion = 0

while opcion != 6:

    print("\n========= MENU PRINCIPAL =========")

    print("1. Ver menu")
    print("2. Ver promociones")
    print("3. Agregar producto")
    print("4. Eliminar producto")
    print("5. Ver factura")
    print("6. Salir")

    opcion = int(input("Seleccione una opcion: "))

    # OPCION 1
    if opcion == 1:

        mostrar_menu()

    # OPCION 2
    elif opcion == 2:

        mostrar_promociones(dia)

    # OPCION 3
    elif opcion == 3:

        agregar_producto(dia)

    # OPCION 4
    elif opcion == 4:

        eliminar_producto()

    # OPCION 5
    elif opcion == 5:

        mostrar_factura()

    # OPCION 6
    elif opcion == 6:

        print("Gracias por usar el sistema")

    else:

        print("Opcion no valida")