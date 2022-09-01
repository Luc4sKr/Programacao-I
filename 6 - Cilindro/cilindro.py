from math import pi

class Cilindro:
    def __init__(self, altura, raio):
        self.__altura = altura
        self.__raio = raio

    def calcular_volume(self):
        return pi * self.__raio**2 * self.__altura
    
    def calcular_area_base(self):
        return pi * self.__raio ** 2
    
    def calcular_area_lateral(self):
        return 2 * pi * self.__raio * self.__altura

    def calcular_area_total(self):
        return 2 * self.calcular_area_base() + self.calcular_area_lateral()


    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, raio):
        self.__raio = raio