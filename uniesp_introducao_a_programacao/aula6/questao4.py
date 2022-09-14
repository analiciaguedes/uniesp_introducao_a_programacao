valor = int(input('entre com um número para saber a tabuada: '))
i = 0 
print('*' * 18)
print(f"tabuada de {valor}")
print('*' *18)
while(i <= 10):
    print(f"{valor} x {i} = {i*valor}")
    i += 1 