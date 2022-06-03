# Sistema de Caixa de Lanchonete:

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
print(f'\nTOTAL A PAGAR: R${sum(totger)}')

totreceb = float(input("Valor entregue: "))

troco = totreceb - sum(totger)

def decompval(valor):
    # Entradas:
    
    valor = float(valor)
    cedulas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

    # Cálculos:

    quantced = [] # quantidades de cedulas
    quantmoe = [] # quantidades de moedas
    while valor >= 1:
        
        for i in range(len(cedulas)):
            quantced.append(int(valor//cedulas[i]))
            valor = valor % cedulas[i]
        
        for j in range(len(moedas)):
            quantmoe.append(int(valor//moedas[j]))
            valor = valor % moedas[j]

    # Saída:

    print('Cédulas:')
    for i in range(len(quantced)):
        if quantced[i] > 0:
            print(f'{quantced[i]} nota(s) de R${cedulas[i]:.2f}')
        
    print('\nMoedas:')
    for i in range(len(quantmoe)):
        if quantmoe[i] > 0:
            print(f'{quantmoe[i]} moeda(s) de R${moedas[i]:.2f}')

print(f'Valor Recebido: R${totreceb:.2f}')
print(f'Troco: R${troco:.2f}')
decompval(troco)