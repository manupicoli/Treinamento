nome_do_instrutor = 'Klismann'

def mostra_nome(nome):
    global nome_do_instrutor # o global faz a ariável sair do escopo da função dela (def)

    nome_do_instrutor = 'Rodolpho'

    print('Seu nome é: ', nome_do_instrutor)


print(nome_do_instrutor)
mostra_nome(nome_do_instrutor)
print(nome_do_instrutor)