from atividade_prática1 import ContaBancaria

class ContaEspecial(ContaBancaria):
    def bajular_cliente(self):
        print('O senhor gostaria de um cafézinho?')

Klismann = ContaBancaria('Indra', saldo=0.21)

cliente_indra = ContaEspecial('Indra Company', 12000)

cliente_indra.consultar_saldo()

cliente_indra.depositar(30000)

cliente_indra.consultar_saldo()

cliente_indra.sacar(32000)

cliente_indra.consultar_saldo()

cliente_indra.bajular_cliente()