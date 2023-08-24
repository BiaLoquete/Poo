#é uma forma mais fácil de fazer
class Carro:
    def __init__(self,nome,cor,ano):
        self.nome=nome
        self.cor=cor
        self.ano=ano

#criar objeto
Fusca=Carro('Fusca', 'Azul', 1965)

print('O nome do carro é: ',Fusca.nome)