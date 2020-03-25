# Modularização 
# Contagem de caracteres em dicionarios


# quais são os caracteres de uma string e quantas vezes eles aparecem?
# foi removido o return já que foi usado oo retorno em print
def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    ex.:
    >>> contar_caracteres('ola')
    {'o': 1, 'l': 1, 'a': 1}
    >>> contar_caracteres('maca')
    {'m': 1, 'a': 2, 'c': 1}

    :param s: string a ser contada

    """

    resultado={}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1 # se o item dentro do dicionario não estiver disponivel ele inicia a contagem com 0 e ioncrementa

    return resultado

if __name__ == '__main__':
    contar_caracteres('ola')
    print()
    contar_caracteres('maca')


