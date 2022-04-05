#Promoção do hotel 
qtdeaptos = float(input())
diaria = int(input())
diaria_com_desc = int
total1 = float
total2 = float
arrecadar = float
arrecadar = diaria * qtdeaptos * 0.25 
diaria_com_desc = diaria * 0.25
diaria -= diaria_com_desc 
total1 = diaria * qtdeaptos 
total2 = total1 * 0.7
print('O valor promocional da diária é: {:.1f}'.format(diaria))
print('O valor arrecadado com ocupação 100%: {:.1f}'.format(total1)) 
print('O valor arrecadado com ocupação 70%: {:.1f}'.format(total2))
print('O hotel deixará de arrecadar: {:.1f} com a promoção'.format(arrecadar))