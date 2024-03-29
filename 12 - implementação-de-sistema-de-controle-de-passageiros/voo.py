from data import Data

class Voo:
    def __init__(self, num_voo, data) -> None:
        self.num_voo = num_voo
        self.data = data
        self.num_assentos = 100

        self.ASSENTO_DISPONIVEL = True
        self.ASSENTO_VAGO = False

        self.lista_assentos = list()
        self.carga_assentos()

    def __str__(self) -> str:
        return f"""--------------------------
VOO NORMAL
--------------------------
Número do voo: {self.getVoo()}
Data do voo: {self.getData()}
Número de assentos: {self.num_assentos}
Número de vagas disponíveis: {self.vagas()}"""

    def proximoLivre(self, num_assento): # retorna o número da próxima cadeira livre
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
        return self.data.data

    def carga_assentos(self):
        # Todas os assentos disponíveis são um valor True na lista
        # Os assentos não disponíveis são False 
        for assento in range(1, self.num_assentos+1):
            self.lista_assentos.append(self.ASSENTO_DISPONIVEL)



class Voo_Mod(Voo):
    def __init__(self, num_voo, data, num_assentos, assento_fumantes) -> None:
        super().__init__(num_voo, data)

        self.num_assentos = num_assentos
        self.assento_fumantes = assento_fumantes

        self.carga_assentos()

    def __str__(self) -> str:
        return f"""--------------------------
VOO MOD
--------------------------
Número do voo: {self.getVoo()}
Data do voo: {self.getData()}
Número de assentos: {self.num_assentos}
Número de assentos para fumantes: {self.assento_fumantes}
Número de vagas disponíveis: {self.vagas()}"""
    
    def maxVagas(self):
        return f"O número maximo de cadeiras é de {self.num_assentos}"

    def cadeirasFumantes(self):
        return f"O número de assentos do voo é de {self.num_assentos} e {self.assento_fumantes} assentos serão destinada a fumantes"

    def tipo(self, num_assento):
        if num_assento >= self.num_assentos - self.assento_fumantes:
            return "F"
        return "N"




