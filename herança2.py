class Carros:
    def __init__(self, marca_do_carro, velocidade_atual, ano_de_fabricação):
        self.marca_do_carro = marca_do_carro
        self.velocidade_atual = velocidade_atual
        self.ano_de_fabricação = ano_de_fabricação
    def acelera(self):
        self.velocidade_atual += 10
    def freiar(self):
        self.velocidade_atual -= 5


mercedes = Carros(marca_do_carro = 'Mercedes', velocidade_atual = 0, ano_de_fabricação = 2023)

mercedes.acelera()

print(mercedes.velocidade_atual)

mercedes.freiar()

print(mercedes.velocidade_atual)