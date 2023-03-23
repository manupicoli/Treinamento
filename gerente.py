class Gerente:
    def __init__(self, numero_funcionarios):
        self.numero_funcionarios = numero_funcionarios
    
    def atribuir_tarefas(self):
        pass

class GerenteRH(Gerente): #quer dizer que vai herdar as mesmas coisas de Gerente
    def atribuir_tarefas(self):
        print('Atribuir um funcionário para admissão')
        self.numero_funcionarios = self.numero_funcionarios

class GerenteDeEstoque(Gerente):
    def atribuir_tarefas(self):
        print('Atribuir 5 funcionários para checagem de estoque')
        self.numero_funcionarios = self.numero_funcionarios

class GerenteInventário(GerenteDeEstoque, GerenteRH):
    def validar_inventário(self):
        return True
    
