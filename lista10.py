#1)Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário

clubs = []

for time in range(10):
    clubs.append(input("Digite os clubes: "))

print("Digite o nome de seu clube para conferir se está na lista!! ")
print("*"*26)

x = input("verifique aqui: ")
if x in clubs:
    print(f"ACHEI !!! o time {x}, foi selecionado . ")
else:
    print(f"NÃO ACHEI !!! O {x}, não foi selecionado    . ")



#2)Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

notas = []
acumuladora = 0
contador = 0

#criação da lista das notas 
for i in range(20):
    notas.append(float(input("Digite sua nota: ")))

#soma
for nota in notas:
    acumuladora = acumuladora + nota

#media
media = acumuladora / len(notas)

for n in notas:
    if n > media: 
        contador += 1 
        #contador = contador +1 

print(f"{contador} foram as notas acima de média. ")


#3)Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
#a)o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#b)o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

vetor = [
    10, 20, 30,
    50, 60, 5000, 70,
    3, 6, 7, 91, 1000
    ]

n = vetor[0]
x = vetor[0]

for q in vetor:

    if q > n: 
        n = q 

    if q < x: 
        x = q 

print(f'o menor valor {x} e seu índice {vetor.index(x)}')
print(f'o maior valor {n} e seu índice {vetor.index(n)}')


#4)Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.

from random import randint 

list_num = []
nova_lista = []

for i in range(10):
    lista_num.append(randint(0, 100))

x = randint(0,9)


for i in range(len(lista_num)):
    nova_lista.append(x * lista_num[i])

print(lista_num)
print(x)
print(nova_lista)


#5)Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. Exemplo: A[0] + B[0] deverá ser salva em N[0].

a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]
n = []

for i in  range(len(a)):
    n.append(a[i] + b[i])

print(n)                                                                                                                        

