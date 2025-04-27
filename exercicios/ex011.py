"""import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o CONSSENO de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))"""

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o CONSSENO de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))
