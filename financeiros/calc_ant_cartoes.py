parc = int(input("Parcelas: "))
valor = float(input("Valor: ")) / parc

receb = 0 # liquido a receber
adq = float(input("Taxa de Adquirência: ")) / 100 # taxa de adquirência
ant = float(input("Taxa de Antecipação: ")) / 100 # taxa de antecipação

for i in range(parc):
    x = valor * (1 - adq) * (1 - ant * (i + 1))
    receb += x

custo = (valor * parc) - receb # custo da operação

print(f"Liquido a Receber: R${receb:.2f}\nCusto da Operação: R${custo:.2f}")