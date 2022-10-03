#Atividade Avaliativa Questão - 4
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso/(altura**2)
print(IMC)
if IMC <= 18.4:
    print(f"Seu IMC: {IMC:.2f}, Você está abaixo do peso.")
elif 18.4 < IMC <= 25:
    print(f"Seu IMC: {IMC:.2f}, Você está no peso ideal. ")
elif 25 < IMC <= 30:
    print(f"Seu IMC: {IMC:.2f}, Você está acima do peso. ")
else:
    print(f"Seu IMC: {IMC:.2f}, Você está obeso ")
    