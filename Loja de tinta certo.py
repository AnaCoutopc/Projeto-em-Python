#Loja de tinta
import math
m2 = float(input())
litros = m2 / 3
print('Você precisará de: {} litros de tinta.'.format(math.ceil((litros))))
galoes = litros /3.6
latas = litros / 18
if latas % 18 != 0: 
    latas += 1
    preco = latas * 79
if galoes % 3.6 != 0:
    galoes += 1
    preco2 = galoes * 24.5
print('A tinta Custará R${} em latas de 18 litros.'.format(math.ceil((preco))))
print('A tinta Custará R${} em galões de 3.6 litros.'.format(math.ceil((preco2))))
# mistura de latas e galoes
mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)
if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1
totalzao = ((mistura_lata * 80) + (mistura_galao * 25))
#print('A tinta custará R$%.2f o menor: %d latas e %d galoes' %totalzao,mistura_lata,mistura_galao)
#print('galoes = %d Mistura: %d latas e %d' %totalzao, mistura_lata, mistura_galao)
print('A tinta Custará R${} se for comprado {} latas e {} galões.'.format(totalzao, mistura_lata, mistura_galao))

