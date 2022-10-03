
#Atividade Avaliativa Questão - 3
while True:
    print("\n*** ESCOLHA A OPÇÃO DESEJADA ***\n")
    
    opcao = int(input("1 Para Adição \n2 Para Subtração \n3 Para Multiplicação\n4 Para Divisão \n5 Para Potenciação \n0 Para parar a execução\n "))
    if 1<= opcao <=5:
        n1 = int(input("digite seu primerio valor: "))
        n2 = int(input("digite seu segundo valor: "))
    
    if opcao == 1:
        soma = n1 + n2
        print(f"SOMA de {n1} + {n2} : {soma} \n")
        
    elif opcao == 2:

        soma = n1 - n2
        print(f"SUBTRAÇÂO de {n1} + {n2} : {soma} \n")
    elif opcao == 3:

        soma = n1 * n2
        print(f"MULTIPLICAÇÂO de {n1} + {n2}: {soma} ")
    elif opcao == 4:

        soma = n1 / n2
        print(f"DIVISÂO de {n1} + {n2} : {soma} ")
    elif opcao == 5:

        soma =n1**n2
        print(f"POTENCIAÇÂO de {n1} + {n2} : {soma} ")
    elif opcao ==0:
        break
    else:
         print("Nenhuma das opções escolhidas\n") 

