print("Cual es su peso en kg?")
peso = float(input())
print("Cual es su estatura en m?")
estatura = float(input())

imc = (peso / estatura ** 2)
imcround = round(imc, 2)
print(imcround)