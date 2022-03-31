# Verificar se um número é primo:
a = int(input('Insira um número: '))
div = 0

for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1

if div == 2:
    print(f'O número {a} é primo.')
else:
    print(f'O número {a} não é primo.')