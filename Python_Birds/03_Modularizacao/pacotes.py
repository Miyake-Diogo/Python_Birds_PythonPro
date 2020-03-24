# Modularização 
# Pacotes

import modulo_matematica.modulo

# como foi criado  um pacote tem de usar o nome do pacote e o modulo
print(modulo_matematica.modulo.soma(4, 5))


# outra opção:

from modulo_matematica.mat import soma

print(soma(4, 5))

# outra opção:
from modulo_matematica.mat import soma as s

print(s(4, 5))