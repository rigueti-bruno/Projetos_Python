# Imprimir apenas os números primos de uma sequência:
50
a = int(input('Informe o último número: '))
seq = []
for num in range(a + 1):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        seq.append(num)
        
print(f'Números primos = {seq}')