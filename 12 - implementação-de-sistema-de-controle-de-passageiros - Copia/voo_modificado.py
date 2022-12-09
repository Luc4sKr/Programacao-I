from voo import Voo

class Voo_Modificado(Voo):
    
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




