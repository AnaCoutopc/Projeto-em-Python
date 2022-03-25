#Ordenação crescente#
x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))
z = int(input("Digite um numero: "))
aux = int
if x > z:
    aux = z
    z = x
    x = aux
if x > y:
    aux = y
    y = x
    x = aux
if y > z:
    aux = z
    z = y
    y = aux
print("%d,"%x, end="")
print("%d,"%y, end="")
print("%d"%z)
