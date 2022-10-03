capital_inicial = float(input("Cantidad del deposito: "))
interes = 0.04

capital_primero = capital_inicial + (capital_inicial * interes)
capital_segundo = capital_primero + (capital_primero * interes)
capital_tercero = capital_segundo + (capital_segundo * interes)

capital_primero_redondeado = round(capital_primero)
capital_segundo_redondeado = round(capital_segundo)
capital_tercero_redondeado = round(capital_tercero)

print("El primer año dispone de", capital_primero_redondeado,"€")
print("El segundo año dispone de", capital_segundo_redondeado,"€")
print("El tercer año dispone de", capital_tercero_redondeado,"€")