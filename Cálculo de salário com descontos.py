#Cálculo de salário com descontos#
salario=float(input('Quanto você ganha por hora?'))
tempo=int(input('Quanto tempo você trabalha por dia?'))
salariobruto=float
imposto=float
inss=float
sindicato=float
salarioliq=float
salariobruto = (salario * tempo) * 30
imposto = salariobruto * 11 / 100
inss = salariobruto * 8 / 100
sindicato = salariobruto * 5 / 100
salarioliq = (salariobruto - imposto - inss - sindicato)
print('salariobruto é de {:.2f}'.format(salariobruto))
print('Quanto pagou ao inss {:.2f}'.format(inss))
print('Quanto pagou ao sindicato {:.2f}'.format(sindicato))
print('salario líquido {:.2f}'.format(salarioliq))