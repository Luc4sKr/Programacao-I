from data import Data

class Voo:
    def __init__(self, num_voo, data) -> None:
        self.num_voo = num_voo
        self.data = data
        self.max_passageiros = 100

        self.ASSENTO_DISPONIVEL = True
        self.ASSENTO_VAGO = False

        self.lista_assentos = list()
        self.carga_assentos()

    def proximoLivre(self, num_assento):
        for i, assento in enumerate(self.lista_assentos):
            if i >= num_assento:
                if assento:
                    return f"Assento {i+1} livre"

    def verifica(self, num_assento): # Verifica se o número da cadeira recebido como parâmetro está ocupada
        if self.lista_assentos[num_assento-1]:
            return "Não está ocupada"
        return "Está ocupada"

    def ocupa(self, num_assento): # Ocupa determinda cadeira do voô
        if self.lista_assentos[num_assento-1]:
            self.lista_assentos[num_assento-1] = self.ASSENTO_VAGO
            return "Operação bem sucedida"
        return "Operação mal sucedida"

    def vagas(self):
        return self.lista_assentos.count(self.ASSENTO_DISPONIVEL)

    def getVoo(self): # Retorna o número do voô
        return self.num_voo

    def getData(self): # Retorna a data do voô (na forma de objeto)
        return self.data

    def carga_assentos(self):
        # Todas os assentos disponíveis são um valor True na lista
        # Os assentos não disponíveis são False 
        for assento in range(1, self.max_passageiros+1):
            self.lista_assentos.append(self.ASSENTO_DISPONIVEL)



class Voo_Mod(Voo):
    def __init__(self, num_voo, data, num_assentos, assento_fumantes) -> None:
        super().__init__(num_voo, data)

        self.num_assentos = num_assentos
        self.assento_fumantes = assento_fumantes
    
    def max_vagas(self):
        pass

    def cadeirasFumantes(self):
        pass

    def tipo(self, num_assento):
        if num_assento >= self.num_assentos - self.assento_fumantes:
            return "F"
        return "N"


voo = Voo(1, Data("21 December, 2022"))
vooMod = Voo_Mod(2, Data("21 December, 2022"), 100, 20)

