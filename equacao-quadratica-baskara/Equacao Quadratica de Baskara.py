from math import sqrt

print("Para uma equacao no formato ax² + bx + c, insira os valores:")
a = float(input("Insira a "))
b = float(input("Insira b "))
c = float(input("Insira c "))

delta = (b ** 2) - (4 * a * c)

if delta >= 0:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    if x1 == x2:
        print(f"Solucao: x = {x1}")
    else:
        print(f"Solucao: x'= {x1}"f"\nx'' = {x2}")
else:
    print('Sem solução!')