#Atividade Avaliativa Questão - 2
import math
x1 = float(input("Entre com um número:\n"))
x2 = float(input("Entre com um número:\n"))
y1 = float(input("Entre com um número:\n"))
y2 = float(input("Entre com um número:\n"))
raiz = math.sqrt(((x2-x1)**2+(y2-y1)**2))

print(f"Sua distância entre os pontos sao: {raiz:.2f}")
