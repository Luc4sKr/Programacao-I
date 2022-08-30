from pprint import pprint
from eleitor import Eleitor

eleitores = []
while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    numero_eleitor = input("Número de eleitor: ")

    eleitor = Eleitor(nome, idade, numero_eleitor)
    eleitores.append(eleitor)

    resp = input("Cadastrar mais um? [S/N]: ").upper()
    if resp == "N" or resp == "NÃO" or resp == "NAO":
        break


media_idade = 0
for eleitor in eleitores:
    media_idade += eleitor.idade
media_idade /= len(eleitores)

q_idade_acima_media = 0
for i, eleitor in enumerate(eleitores):
    if eleitor.idade > media_idade:
        q_idade_acima_media += 1

    if i == 0:
        maior_idade = eleitor
        menor_idade = eleitor
    
    if eleitor.idade > maior_idade.idade:
        maior_idade = eleitor
    if eleitor.idade < menor_idade.idade:
        menor_idade = eleitor


print("=" * 40)
print(f"Média de idade dos eleitores: {media_idade}")
print(f"Quantidade de eleitores com idade acima da média: {q_idade_acima_media}")
print("-- Eleitor mais novo --")
print(f"Nome: {menor_idade.nome}, Idade: {menor_idade.idade}, Número: {menor_idade.numero_eleitor}")
pprint("-- Eleitor mais velho --")
print(f"Nome: {maior_idade.nome}, Idade: {maior_idade.idade}, Número: {maior_idade.numero_eleitor}")
print("=" * 40)
