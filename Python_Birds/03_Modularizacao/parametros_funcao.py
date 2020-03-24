# Modularização 
# Parametros de Função

def ola(nome):
    return f'Olá {nome}'

ola('Diogo')

ola('Jamile')
# Note que será retornado os itens escritos conforme os parametros passados

def ola2(nome, sobrenome):
    return f'Olá, {nome} {sobrenome} '

ola2('Diogo', 'Miyake')

# é possivel ter parametros que ja possuem valor

def ola3(nome, sobrenome = 'Miyake'):
    return f'Olá, {nome} {sobrenome}'

ola3('Diogo')

# Existem duas formas de passar os parametros para as funções
# justaposição : quando se usa a ordem definida na função
# pelo nome: passa o nome=valor 

ola3(nome='Jamile', sobrenome='Costa')
ola3(sobrenome='Costa',nome='Jamile') # quando se passa por nome a ordem não importa




