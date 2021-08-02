# calculando o desvio padrão
lista = []
while True:
    x = input('Digite um valor ou enter para sair: ')
    if x == '':
        break
    elif x != '':
        lista.append(int(x))

soma = 0

for valor in lista:
    soma += valor

media = soma / len(lista)
elevar = [valor - media for valor in lista]
quadrados = [valor ** 2 for valor in elevar]

soma = sum(quadrados)

variancia = soma / len(lista)
desviopadrao_popu = variancia ** 0.5
coeficiente_de_variacao = (desviopadrao_popu / media) * 100

print(f'n° digitados: {lista}')
print(f'média: {media}')
print(f'Variância: {variancia}')
print(f'Desvio padrão da população: {desviopadrao_popu}')
print(f'Coeficiente de variação: {coeficiente_de_variacao}')
