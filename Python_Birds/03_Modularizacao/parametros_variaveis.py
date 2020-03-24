# Modularização 
# Parametros Variaveis 

# para passar os parametros ao qual não se sabe a quantidade 
# usa-se o *
# Geralmente usa-se o *args, mas pode ser qualquer valor como *parcelas
# sepedir para ver o tipo dos parametros, verá que é do tipo tupla
def tipo(*parcelas):
    print(parcelas)
    print(type(parcelas))

tipo()

tipo(1,2,3)

def soma(*parcelas):
    aux=0
    for valor in parcelas:
        aux += parcelas
    return aux

soma(1,2,3,4,5)
soma(10,5,20)
soma(5,5)

def f(**kwargs):
    print(kwargs)
    print(type(kwargs))

# Note que o kwargs é do tipo dicionario
# para passar o parametro tem de passar o nome(chave) e o valor

# exemplo
f(nome = 'Diogo')

f(nome = 'Diogo', sobrenome = 'Miyake')

# e quando ja se tem uma tupla e um dicionario com o nome usado?
args = (2,3,4)
kwargs = {'nome' = 'Diogo', 'idade' = 30}

# Cria a função com o args seguido do kwargs
def f(*args ,**kwargs):
    print(type(*args))
    print(type(kwargs))

f(30, 28, nome = 'Diogo', nome2='Jamile')


f(args,kwargs) #retorna o que ja tem definido, cem uma tupla
# temos de desempacotar
f(*args)

f(**kwargs)



