

class ContaPoupanca:
    def __init__(self, init):
        self.saldo_cc = init
        self.juros = self.saldo_cc * 0.04
    
    def saque(self, valor):
        if valor > self.saldo_cc:
            print('Saldo insuficiente')
        else:
            print('Saque efetuado')
            self.saldo_cc = self.saldo_cc - valor
            
    def deposito(self, valor):
        if valor <= 0:
            print('Valor insuficiente')
        else: 
            print('Deposito efetuado')
            self.saldo_cc = self.saldo_cc + valor
            self.saldo_cc = self.saldo_cc + self.juros
            
    def saldo(self):
        print(f'Saldo: R${self.saldo_cc}')