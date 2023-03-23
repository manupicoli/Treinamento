#Urna Eletrônica
class UrnaEletronica:
    def __init__(self):
        self.candidatos = [{'nome_candidato': 'Manuela', 'partido': 'Paz'}, #lista de dicionário
                            {'nome_candidato': 'Guilherme', 'partido': 'Amor'},
                            {'nome_candidato': 'Letícia', 'partido': 'Sabedoria'}]

    def exibe_candidatos(self):
        for candidato in self.candidatos:
            print(f'O candidato é', candidato['nome_candidato'])
            print(f'Do partido',candidato['partido'])

    def adicionar_novo_candidato(self, nome_candidato, partido):
        self.candidatos.append({'nome_candidato': nome_candidato, 'partido': partido})
        
    def remover_candidato(self):
        self.candidatos.pop(1)

    def atualizar_candidato(self, index, chave, valor):
        #try: #TENTE algo. se não der...
        self.candidatos[index][chave] = valor
        #except IndexError: #tente isso, exceção

        # try: TENTE algo. se não der...
        #   12/0
        # except Exception as e: tente isso, exceção
        #   print(e) - mostre qual é o erro
        #   print('Esse programa não pode parar') - e mostre a frase

urna = UrnaEletronica()

print('-----------------')

urna.exibe_candidatos()
urna.adicionar_novo_candidato('João', 'Honesto')

print('-----------------')

urna.remover_candidato()
urna.exibe_candidatos()

print('-----------------')

urna.atualizar_candidato(0, 'nome_candidato', 'Vinícius')
urna.atualizar_candidato(0, 'partido', 'Coragem')

urna.exibe_candidatos()

print('------------------')

# urna.atualizar_candidato(3, 'nome_candidato', 'Ademir')
# urna.atualizar_candidato(3, 'partido', 'Bravura')

# urna.exibe_candidatos()