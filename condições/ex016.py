from math import radians, sin, cos, tan
an = float(input('Digite um angulo: '))
seno = sin(radians(an))
coss = cos(radians(an))
tan = tan(radians(an))
print(f'O seno de {an} é {seno:.2f}\n O cosseno de {an} é {coss:.2f}\n E a Tangente de {an} é {tan:.2f}')