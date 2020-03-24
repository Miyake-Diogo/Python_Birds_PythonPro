# Containers e Iteração
# Dicionario e Mapas

# equivalente a mapas ou hash tables em outras linguagens

# são usandos chaves {} como delimitadores
# É composto por chave:valor

# criando um dicionário

linguas = {'br':'português', 'en':'ingles', 'jp':'japones'}

linguas # retorna todas as chaves e valores
linguas['br'] # traz os valores da chave br

# outra forma de pegar os itens é usar o metodo get
linguas.get('br')
linguas.get('es', 'Não definido') # o segundo parametro permite colocar um standard quando não encontra o valor

'br' in linguas # retorna verdadeiro se existe
'es' in linguas # retorna falso se não exite

# outro exemplo 
6 in range(10)
11 in range(10)

linguas['es'] = 'spanhol' # cria a chave es com o valor espanhol
linguas
linguas['es'] = 'espanhol' # atualiza a chave corrigindo o valor
linguas
