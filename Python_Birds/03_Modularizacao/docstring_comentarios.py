# Modularização 
# Docstrings e comentários
# A docstring serve como string inicial para o modulo criado

def soma(parcela1, parcela2):
    """ Calcula a soma de duas parcelas
    :param parcela1:  number
    :param parcela2:  number
    :return: number
    """

    return parcela1 + parcela2


if __name__ == '__main__   ':
    # testando a função soma
    print(modulo.soma(1, 2)) # imprimindo

# para testar import o modulo e use o help(modulo.soma())