# Modularização 
# Contagem de caracteres em dicionarios


# quais são os caracteres de uma string e quantas vezes eles aparecem?
# foi removido o return já que foi usado oo retorno em print
def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    ex.:
    >>> contar_caracteres('ola')
    {'a': 1, 'l': 1, 'o': 1}
    >>> contar_caracteres('maca')
    {'a': 2, 'c': 1, 'm': 1}

    :param s: string a ser contada

    """

    caracteres_ordenados = sorted(s)
    caracter_anterior  = caracteres_ordenados[0]
    contagem = 1
    resultado={}
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem+= 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1
    resultado[caracter_anterior] = contagem
    return resultado

if __name__ == '__main__':
    contar_caracteres('ola')
    print()
    contar_caracteres('maca')


