# Containers e Iterações

#listas em  python são equivalentes a arrays dinamicos em outras linguagems

# são criadas com colchetes []
# ou com a funcção list()
lista1 = [1,2,3,4,5]
lista2 = ["Brasil", 'Uruguay', 'Argentina']
lista3 = list()  # Lista vazia

print(lista1)
print(lista2)
print(lista3)
# A função Range itera de um inicio até um final
lista4 = list(range(15)) # Cria uma lista de 1 a 15, usando a função range
# Lembrando   que inicia do zero(Inclusivo) e o ultimo (exclusivo-sai da lista)

print(lista4)
# lista decrescente com range
lista5 = list(range(10, 0, -2))
lista5

# Outras funções
lista5 = [6,5,10,80,65,10,47,69,30,1,2,14]
lista5.sort() # ordena a lista
lista5.append(9) # insere um item ao fim da lista
lista5.pop() # remove um item do fim da lista
lista5.extend([15,24])

# concatenando listas, use o +
lista6 = [1,2,3]
lista7 = [5,9,7]
lista8 = lista6 + lista7

lista8 * 2
'Python pro'.split() # sem argumento usa o espaço para separar
'python-pro'.split('-')
lista9 = _

lista10 = 'idade = '
'15'.join(lista10)

