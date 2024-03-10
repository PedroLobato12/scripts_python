from math import radians, sin, cos, tan
Angulo = float(input('Digite o Angulo que você deseja: '))
seno = sin(radians(Angulo))
print('O Ângulo de {} tem o seno de {:.2f}'.format(Angulo, seno))
cosseno = cos(radians(Angulo))
print('O Ângulo de {} tem o cosseno de {:.2f}'.format(Angulo, cosseno))
tangente = tan(radians(Angulo))
print('O Ângulo de {} tem a tangente de {:.2f}'.format(Angulo, tangente))
