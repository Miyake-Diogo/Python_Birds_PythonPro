# Containers e Iteração
# Acesso, Tamanho e Fatiamento 

nome='Diogo'
# para acessar os itens(caracteres da string)
nome[0] # retorna o D

# len traz o comprimento da sequencia
len(nome)

# para acessar o último

# tem de colocar o -1 para poder trazer o ultimo, 
# pois o indice começa de zero
nome(len(nome) - 1) 

# na pratica o mais fácil ét razer o indice negativo
nome[-1]
nome[-2]

# Slicing ou fatiamento

nome[0:3]

# do terceiro de tras para frente ao fim
nome[-3:len(nome)]

nome[-3:]

# Do inicio ao quarto
nome[:3]
# para usar o terceiro parametro que seria o passo
nome[:4:2] # vai de 0 a 4 pulando de dois em dois

# inverter string
nome[::-1] # começa de trás para frente

# o mesmo serve para listas e tuplas

lista = list(range(10))

lista[0]
lista[:5]
lista[::-1]
len(lista)

