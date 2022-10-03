capital = float(input("Cantidad que desea invertir: "))
interes = float(input("Interes anual: "))
years = float(input("Duracion de la inversion en años: "))

print(((capital * interes * years)/100) + capital)