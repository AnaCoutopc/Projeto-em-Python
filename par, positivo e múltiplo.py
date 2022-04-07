#par, positivo e múltiplo 
a = int(input())
b = int (input())
if a > 0 and a % b == 0 or b % 2 == 1 and b % a == 0 and a != b:  
    print('SIM')
else:
    print('NÃO')
