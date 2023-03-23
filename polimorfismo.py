#Orientação a objetos: classe, objeto, atributos, métodos (funções), herança, polimorfismo, superclasses
class Bicho:
    def __init__(self, peso):
        self.peso = peso

class Animal(Bicho):
    def __init__(self, peso, nome):
        super().__init__(peso)
        self.__nome = nome #com dois underline, a variavel se torna privada
    
    def fazer_barulho(self):
        print('Fez barulho genérico')

class Cachorro(Animal):
    def fazer_barulho(self):
        print('Au au!')

class Gato(Animal):
    def fazer_barulho(self):
        print('Miau!')

class Ave(Animal):
    def __init__(self, tem_asa):
        super().__init__(80, 'Ricardo') #o super serve para se referenciar à classe SUPERIOR
        self.tem_asa = True

    def fazer_barulho(self):
        return super().fazer_barulho()


cachorro_bob = Cachorro(peso=14, nome='BOB')
cachorro_bob.fazer_barulho()

animal_generico = Animal(peso=80, nome='Cavalo')
animal_generico.fazer_barulho()