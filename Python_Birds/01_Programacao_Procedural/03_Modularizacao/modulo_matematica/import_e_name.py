# Modularização 
# Import e Name
# Para poder importar modulos use o import

import modulo_matematica.modulo

print(modulo_matematica.modulo.soma(4, 5))

# outras formas

from modulo_matematica import modulo
print(modulo.soma(4, 5))


from modulo_matematica.modulo import soma
print(soma(4, 5))

from modulo_matematica.modulo import soma as s
print(s(4, 5))