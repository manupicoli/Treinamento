#no python existe heranças múltiplas
class Pessoa:
    def __init__(self): #o self serve para indicar que é uma variável desse tipo
        self.idade = 21

Klismann = Pessoa()
Klismann.idade = 22
print(Klismann.idade)
print(isinstance(Klismann.idade, str))
print(type(Klismann.idade))

class Pessoa:
    def __init__(self, idade): #o self serve para indicar que é uma variável desse tipo
        self.idade: int = idade

Klismann = Pessoa(24)
print(Klismann.idade)
print(isinstance(Klismann.idade, str))
print(type(Klismann.idade))

class Pessoa:
    def __init__(self, nome, idade): #o self serve para indicar que é uma variável desse tipo
        self.nome: str = nome
        self.idade: int = idade

Klismann = Pessoa(nome= 'Klismann', idade = 24)
Valquiria = Pessoa(nome = 'Valquiria', idade = 18)
print(Klismann.nome, Valquiria.nome)

class Pessoa:
    def __init__(self, nome, idade): 
        self.nome: str = nome
        self.idade: int = idade
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
Klismann = Pessoa(nome= 'Klismann', idade = 24)
Valquiria = Pessoa(nome = 'Valquiria', idade = 18)
Klismann.apresentar()
Valquiria.apresentar()