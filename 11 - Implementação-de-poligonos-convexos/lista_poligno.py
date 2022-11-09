from poligno import Poligno
from ponto import Ponto

class Lista_polignos:
    def __init__(self) -> None:
        self.lista = [
            Poligno([Ponto(1, 1), Ponto(3, 1), Ponto(3, 3), Ponto(1, 3)]),
            Poligno([Ponto(1, 1), Ponto(5, 1), Ponto(1, 3)])
        ]