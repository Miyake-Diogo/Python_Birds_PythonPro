# Containers e Iteração
# Loop For

nome = 'Diogo'

# O loop for (para) é uma melhor opção ao invés de usar while.
# para cada iteração valor valores em nome, imprime os caracteres.

for valores in nome: 
    print(valores)

# outra opção é usar da forma abaixo

for i in range(len(nome)):
    print(i, nome[i])

for i, v in enumerate(nome):
    print(i, v)

# enumerate ja retorna o valor da variavel v, 
# uma melhor forma seria usando a função interna enumerate

for v in enumerate(nome):
    print(v)

# Muitas vezes, ao lidar com iteradores, 
# também precisamos manter uma contagem de iterações. 
# O Python facilita a tarefa dos programadores, 
# fornecendo uma função interna enumerate () 
# para esta tarefa.
#O método Enumerate () adiciona um contador a um iterável 
# e o retorna em uma forma de objeto enumerado. 
# Esse objeto enumerado pode então ser usado 
# diretamente em loops ou ser convertido em 
# uma lista de tuplas usando o método list ().