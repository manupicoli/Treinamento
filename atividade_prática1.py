#Conta Bancária

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if (valor <= self.saldo):
            self.saldo = self.saldo - valor
        else:
            print('Saldo insuficiente')

    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

manuela = ContaBancaria(titular='Manuela', saldo=300)

manuela.sacar(10) #vou sacar 10 reais

print(manuela.saldo)

manuela.sacar(300)

manuela.depositar(1000)

print(manuela.saldo)
