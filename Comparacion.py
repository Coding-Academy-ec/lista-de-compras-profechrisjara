# Solicitar al usuario que ingrese una lista de compras
compras = input("Ingrese una lista de compras: ")

# Dividir la cadena de entrada en una lista de productos
productos = compras.split(", ")

# Imprimir la lista de productos
print(f"Los productos en la lista de compras son: {productos}")

# Convertir la lista de compras en una tupla
def convertir_lista_a_tupla(lista):
    return tuple(lista)

# Llamar a la función para convertir la lista en una tupla
tupla_productos = convertir_lista_a_tupla(productos)

# Imprimir la tupla de productos
print(f"Los productos en la lista de compras son: {tupla_productos}")
