##Atividade Avaliativa Questão - 6
A = int(input("Digite o valor de 'A': " ))

i = A-1
total = 0
pos = 0
lista = []
lista.append(A)
resultado = f"{A}!="
while i<A and i>=1:
    if pos == 0:
        total = A*i
        lista.append(i)
        i-=1
        pos+=1
    else:
        total = total * i
        lista.append(i)
        i-=1
for x in lista:
    if x == lista[-1]:
        resultado+= f"{x}"
    else:
        resultado+= f"{x}x"
               
resultado+= f"={total}"
print("Resultado: ", resultado)
