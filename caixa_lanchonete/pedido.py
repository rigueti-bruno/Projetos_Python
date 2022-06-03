# Biblioteca com as Informações:

menu = {1:("Cachorro Quente", 4), 2:("X-Salada", 4.5),  3:("X-Bacon", 5), 4:("Torrada Simples", 2), 5:("Refrigerante", 1.5)}

# Montar o Pedido:

print("NOTA FISCAL")
print("_" * 15)
opt = print("""
                 Escollha uma opção:
                     1 - Cachorro Quente
                     2 - X-Salada
                     3 - X-Bacon
                     4 - Torrada Simples
                     5 - Refrigerante 
                     """)
print("_" * 15)

totger = []
totite = int(input("Quantos itens: "))
for i in range(totite):    
    item = int(input("Item: "))
    quant = int(input("Quantidade: "))
    valor = float(menu[item][1] * quant)
    totger.append(valor)
    # Resumo por item escolhido:
    print(f'Item Escolhido: {menu[item][0]}\nQuantidade Solicitada: {quant}\nTotal a pagar: R${valor:.2f}')
    print("_" * 15)

# Resumo do Pedido:
print(f'\nTOTAL A PAGAR: {sum(totger)}')
