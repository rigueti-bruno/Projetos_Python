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
        
# Essa função imprime um triangulo invertido alinhado à esquerda:
def triangulo_esq_i(n):
    k = 1
    while n > 0:
        print(("*" * n) + (" " * k) + "\n")
        n -= 1
        k += 1

# Essa função imprime um triangulo invertido alinhado à direita:
def triangulo_dir_i(n):
    k = 1
    while n > 0:
        print((" " * k) + ("*" * n) + "\n")
        n -= 1
        k += 1

# Essa função imprime uma pirâmide invertida:
def piramide_i(n):
    k = 1
    while n > 0:
        print((" " * k) + ("*" * n * 2) + (" " * k) + "\n")
        n -= 1
        k += 1

triangulo_esq(8)
triangulo_dir(8)
piramide(8)
triangulo_esq_i(8)
triangulo_dir_i(8)
piramide_i(8)