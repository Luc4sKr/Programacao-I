import math

class Circuo:
    def __init__(self, raio) -> None:
        self.__raio = raio

    def calcular_area(self):
        return math.pi * self.__raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.__raio

    def imprimir(self):
        return f"Raio: {self.__raio} \nÁrea: {self.calcular_area():.2f} \nPerímetro: {self.calcular_perimetro():.2f}"

    
    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        self.__raio = raio



c1 = Circuo(5)
print("C1 ==========================")
print(c1.imprimir())
print("=============================")

c2 = Circuo(7.89)
print("C2 ==========================")
print(c2.imprimir())
print("=============================")

c3 = Circuo(12)
print("C3 ==========================")
print(c3.imprimir())
print("=============================")
