print('[ ! ] PROMOÇÃO: Apartir de 12 macas, o valor de cada uma séra R$ 1,00. Valor normal sera R$ 1,30 [ ! ]')
macas = int(input('Digite o numero de maças que deseja comprar (0 para sair do programa): '))

preco_promocao = 1.00
preco_normal = 1.30 

if macas == 0: # se digitado 0, encerra o programa
    print('ate mais!')
    exit(0)
elif macas < 0: # caso digite numero digitado negativo, mostra nessa mensagem de "erro"
    print(f'O numero digitado e negativo: {macas}')
    exit(1)
elif macas >= 12: #calcula o valor total incluso da promocao
    total= preco_promocao * macas
    print(f'voce comprou {macas} e fez parte da promocao. valor total; {total}')
else: # calculando com o valor normal 
    total= preco_normal * macas 
    print(f'voce comprou {macas} e nao faz parte da promocao. valor total: R$ {total}')