class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        self.__idade = None
        self.__peso = None

    @staticmethod
    def __validar_valor(valor):
        if valor < 0:
            return 0
        return valor

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = self.__validar_valor(idade)

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = self.__validar_valor(peso)


def divisoria(num=40):
    return "=" * num

pessoas = []
media_peso = 0
mais_leve = 999
mais_velho = -1

while True:
    print(divisoria())
    nome = input("Nome: ").title().strip()

    if nome == "Fim":
        print(divisoria())
        break

    pessoa = Pessoa(nome)

    idade = input(("Idade: "))
    while not idade.isnumeric():
        print("-- Idade Inválida --")
        idade = input(("Idade: "))
    idade = int(idade)

    peso = input("Peso: ")
    while not peso.isnumeric():
        print("-- Peso Inválido --")
        peso = input("Peso: ")
    peso = float(peso)

    pessoa.idade = idade
    pessoa.peso = peso
    pessoas.append(pessoa)
    print(divisoria())

if len(pessoas) > 0:
    for pessoa in pessoas:
        media_peso += pessoa.peso
        if pessoa.idade > mais_velho:
            mais_velho = pessoa.idade
        if pessoa.peso < mais_leve:
            mais_leve = pessoa.peso
    
    print(f"Média peso: {media_peso / len(pessoas)}")

    for pessoa in pessoas:
        if pessoa.peso == mais_leve:
            print(f"Pessoa mais leve: {pessoa.nome}, {pessoa.peso}")
        
        if pessoa.idade == mais_velho:
            print(f"Pessoa mais velha: {pessoa.nome}, {pessoa.idade}")
        
    for pessoa in pessoas:
        print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade} - Peso: {pessoa.peso}")
    
    print(divisoria())


def divisoria():
    return "=" * 40