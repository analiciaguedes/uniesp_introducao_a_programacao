#1)Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário

clubs = []

for time in range(4):
    clubs.append(input("Digite os clubes: "))

print("Digite o nome de seu clube para conferir se está na lista!! ")
print("*"*26)

x = input("verifique aqui: ")
if x in clubs:
    print(f"ACHEI !!! o time {x}, foi selecionado . ")
else:
    print(f"NÃO ACHEI !!! O {x}, não foi selecionado    . ")



#2) Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

import random
list=[]

for x in range(30):
    x = random.randint(1, 15)
    list.append(x)

meu_numero = int(input('Digite um numero de 1 a 30: '))
contador = 0
for x in list:
    if x == meu_numero:
        contador += 1
print(f"Eu escolhi o número: {meu_numero} . ")
print(f"Meu número repetiu, {contador} vezes. ")
print(f"Os números sorteados são: {list}. ")