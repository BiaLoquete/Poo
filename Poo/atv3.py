class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def depositar(self,valor):
        self.saldo+=valor

    def sacar(self, valor):
        self.saldo-=valor

    def exSaldo(self):
        print(self.saldo)

Gi = ContaBancaria("Gi", 1000, 2032)
Gi.depositar(200)
Gi.sacar(100)
Gi.exSaldo()