#Atividade Avaliativa Questão - 5
print("DIGITE SEUS VALORES NO CAMPO ABAIXO \n")
a=0; b=0; c=0; d=0
while True:
    v = int(input("Digite seus valores: "))
    if 0<=v<=25:
        a+=1
    elif 26<=v<=50:
        b+=1
    elif 51<=v<=75:
        c+=1
    elif 76<=v<=100:
        d+=1
    elif v>100:
        print("Valor maximo 100")
    elif v<0:
        break
print(f"entre os valores 0 e 25 foram digitados: {a}\nentre os valores 26 e 50 foram digitados: {b}\nentre os valores 51 e 75 foram digitados: {c}\nentre os valores 76 e 100 foram digitados: {d}")


