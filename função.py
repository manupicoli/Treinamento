def retira_numero_negativo(numero):
    return abs(numero) #abs = retorna o valor absoluto, sem ser negativo

def soma_dois_inteiros(primeiro_numero, segundo_numero):
    return retira_numero_negativo(primeiro_numero) + retira_numero_negativo(segundo_numero)
print(soma_dois_inteiros(12, 13))


numero = int(input('digite seu cpf: '))
def verifica_se_eh_cpf_ou_cnpj(numero):
    if len(numero) == 11:
        return 'CPF'
    else:
        return 'CNPJ'
    
# def verifica_se_eh_cpf_ou_cnpj(numero):
#     if verifica_e_valida_cpf_e_cnpj == 'CPF':
#         valida_cpf_ou_cnpj
#     else:
#         valida_cpf_ou_cnpj 

    
def valida_cpf_ou_cnpj(numero):
    return 1



