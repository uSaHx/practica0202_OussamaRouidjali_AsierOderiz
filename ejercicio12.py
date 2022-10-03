barra_nueva = 3.49
numero_barras_pasadas = int(input("Introduzca las barra no vendidas: "))
descuento = 0.6
descuento_barra = (barra_nueva * descuento)
barra_pasada = barra_nueva - (barra_nueva * descuento)

print("Precio de una barra fresca es de: ")
print(barra_nueva, "€")
print("Descuento por no ser barra de pan fresca es de:")
print(descuento_barra, "€")
print("El precio de las barras no frescas es de")
print(barra_pasada, "€")
print("Ganancia total es de: ")
print(barra_pasada * numero_barras_pasadas, "€")

