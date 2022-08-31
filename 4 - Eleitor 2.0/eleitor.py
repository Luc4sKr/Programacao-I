class Eleitor:
    def __init__(self, nome, idade, numero_eleitor) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__numero_eleitor = numero_eleitor


    def verificar(self):
        if self.__idade < 16:
            return f"{self.__nome} ainda não pode votar. Tem apenas {self.__idade} anos de idade."
        elif self.__idade >= 16 and self.__idade < 18 or self.__idade > 65:
            return f"{self.__nome} - {self.__idade}. Voto facultativo"
        else:
            return f"{self.__nome} - {self.__idade}. Deve votar."
    

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
        self.__idade = idade

    @property
    def numero_eleitor(self):
        return self.__numero_eleitor
    
    @numero_eleitor.setter
    def numero_eleitor(self, num):
        self.__numero_eleitor = num


        