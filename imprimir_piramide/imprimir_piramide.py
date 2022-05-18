# Essa função imprime um triangulo alinhado à esquerda:
def triangulo_esq(n):
    i = 1
    k = n - i + 1
    while i < n:
        print(("*" * i) + (" " * k) + "\n")
        k -= 1
        i += 1

# Essa função imprime um triangulo alinhado à direita:
def triangulo_dir(n):
    i = 1
    k = n - i + 1
    while i < n:
        print((" " * k) + ("*" * i) + "\n")
        k -= 1
        i += 1

# Essa função imprime uma pirâmide:
def piramide(n):
    i = 1
    k = n - i + 1
    while i < n:
        print((" " * k) + ("*" * i * 2) + (" " * k) + "\n")
        k -= 1
        i += 1

triangulo_esq(8)
triangulo_dir(8)
piramide(8)