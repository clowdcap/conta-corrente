import cc, cp

class Cliente:
    def __init__(self):
        self.conta = cc.ContaCorrente(3000)
        self.poup = cp.ContaPoupanca(3000)

    def saldo_cliente(self):
        print(f'Conta Corrente R${self.conta}\nConta Poupanca R${self.poup}')
    

Cliente.saldo_cliente()