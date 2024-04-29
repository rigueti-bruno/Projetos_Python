# Criação da Classe para gerar os Objetos Salario Liquido:
class Salario:  
    def __init__(self,remuneracao,he,insa):
        self.remuneracao = remuneracao
        self.he = he
        self.insa = insa
        
    def hextra(self):
        return ((self.remuneracao / 220) * 1.5) * self.he

    def insalub(self):
        if self.insa == True:
            return self.remuneracao * 0.15
        else:
            return 0
        
    def descinss(self):
        self.saltot = self.remuneracao + self.hextra() + self.insalub()
        if self.saltot <= 1412:
            return self.saltot * 0.075
        elif self.saltot <= 2666.68:
            return (self.saltot * 0.09) - 21.18
        elif self.saltot <= 4000.03:
            return (self.saltot * 0.12) - 101.18
        elif self.saltot > 7786.02:
            return (self.saltot * 0.14) - 181.18
    
    def descir(self):
        self.saltot = self.remuneracao + self.hextra() + self.insalub()
        if self.saltot <= 2259.20:
            return 0
        elif self.saltot <= 2826.65:
            return (self.saltot * 0.075) - 169.44
        elif self.saltot <= 3751.05:
            return (self.saltot * 0.15) - 381.44
        elif self.remuneracao <= 4664.68:
            return (self.saltot * 0.225) - 662.77
        elif self.saltot > 4664.68:
            return (self.saltot * 0.275) - 896
          
    def liquido(self):
        return self.remuneracao + self.hextra() + self.insalub() - self.descinss() - self.descir()
    
    def contracheque(self):
        return f"Salario Bruto: R${self.remuneracao:.2f}\n(+) Horas Extras: R${self.hextra():.2f}\n(+) Insalubridade: R${self.insalub():.2f}\n(-) INSS: R${self.descinss():.2f}\n(-) IRPF: R${self.descir():.2f}\n\n(=) Salario Liquido: R${self.liquido():.2f}"

salario = float(input("Insira o valor do Salario: "))
hextra = int(input("Insira a quantidade de Horas Extras: "))
ins = input("Tem Insalubridade? Insira Sim ou Nao: ")
insalubridade = False
if ins == "Sim" or ins == "sim":
    insalubridade = True

nome = input("Insira o Nome do Colaborador: ")

contcheque = Salario(salario,hextra,insalubridade)

with open(f"Contra-Cheque {nome}.txt","w") as f:
    f.write(contcheque.contracheque())