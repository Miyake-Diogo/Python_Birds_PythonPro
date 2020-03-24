# Containers e Iteração
# Iteração em Dicionários

# Definindo o dicionário

linguas = {'br':'português', 'en':'ingles', 'jp':'japones', 'es','espanhol'}

# os dicionários aceitam 
# as formas de iteração que vimos anteriormente
# este imprime as chaves
for chave inlinguas:
    print(chave)

# uma melhor forma é utilizar seus metodos
# para poder utilizar o loop pelas chaves e pelos valores 

for chave in linguas.keys():
    print(chave)

for valores in linguas.values():
    print(valores)

# para percorrer os dois usando o metodo .items()
# para a impressão desempacote em tuplas

for chave, valor in linguas.items():
    print(chave, valor)

# para remover items use o pop
linguas.pop('br') # tem de especificar o elemento

# verificando os items em linguas
linguas

# usando o del de delete
del linguas['es']
linguas


