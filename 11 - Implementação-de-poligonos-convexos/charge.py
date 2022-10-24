from poligno import Poligno
from ponto import Ponto
from random import randint

class Charge:
    def __init__(self, lista_polignos) -> None:
        self.__lista_polignos = lista_polignos

    def run(self):
        lista_pontos = []
        for i in range(1, randint(3, 8)):
            p = [randint(1, 6), randint(1, 6)]
            if p not in lista_pontos:
                lista_pontos.append(p)
        
        poligno = Poligno([])
        for ponto in lista_pontos:
            poligno.addPonto(ponto[0], ponto[1])
        print(poligno)