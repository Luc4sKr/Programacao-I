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
