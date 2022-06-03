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
        
decompval(input("Digite o valor: "))