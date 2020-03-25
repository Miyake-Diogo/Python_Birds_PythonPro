# Modularização 
# Modulos

# Modulos são arquivos de scripts python como estes que temos com aextensão .py


def soma(parcela1, parcela2):
    return parcela1 + parcela2


if __name__ == '__main__   ': #executa um teste com este modulo
    print(modulo.soma(1, 2))
# pode ser executado no modo interativo do vsccode (shift+enter)
# ou usando o run tanto do vscode quanto do pycharm 

# o __name__ == __main__ evita que o codigo de teste execute ao chamar o modulo