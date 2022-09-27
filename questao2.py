nascimento = int(input("digite seu ano de nascimento:"))
ano_atual = 2022 
idade = ano_atual - nascimento 

if idade < 16: 
    print(f"idade atual {idade}, voce nao pode votar esse ano!")
if idade >= 16: 
    print(f"idade atual {idade}, voce pode votar esse ano!")