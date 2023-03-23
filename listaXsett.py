#LISTA X SET
#Lista é para quantidades (pode repetir valores)
#Set dá para filtrar valores, o foco não é a quantidade mas sim o dado (valores não repetidos)
#no Set ele não ordena os elementos como nas listas

lista = [60, 12, 43, 56, 60, 98]
print(lista)
set_de_lista = list(set(lista))
print(set_de_lista)
print(len(lista) == len(set(lista)))

equipamentos = {34, 78, 65, 44, 123, 90}
equipamentos.add(35)
equipamentos.pop()
print(equipamentos)

equipamentos.clear()
print(equipamentos)
