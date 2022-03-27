#Cálculando o custo de uma viagem
distância=float(input('Qual é a distância da sua viagem?'))
print ('Você está prestes a cancelar uma viagem de {}km'.format(distância))
if distância <= 200:
    valor = distância * 0.50
else:
    valor = distância * 0.45
print ('E o preço da sua passagem será de R${:.2f}'.format(valor))