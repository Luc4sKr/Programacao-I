from math import sqrt
from ponto import Ponto

class Poligno:
    def __init__(self, pontos):
        self.__pontos = pontos

    def __str__(self) -> str:
        s = "\n"
        return f"""---------------
Polígno
---------------
Pontos:
{s.join(map(str, self.__pontos))}
---------------
"""

    def area(self):
        a = 0
        for i, ponto in enumerate(self.__pontos): 
                try:
                    #print(f"x{i+1} * y{i+2} - x{i+2} * y{i+1}")
                    a += ponto.x * self.__pontos[i+1].y - self.__pontos[i+1].x * ponto.y
                except:
                    #print(f"x{i+1} * y1 - x1 * y{i+1}")
                    a += ponto.x * self.__pontos[0].y - self.__pontos[0].x * ponto.y
        return f"{1/2 * a:.2f}"

    def perimetro(self):
        p = 0
        for i, ponto in enumerate(self.__pontos):
            try:
                d = sqrt((self.__pontos[i+1].x - ponto.x) ** 2 + (self.__pontos[i+1].y - ponto.y) ** 2)
            except:
                d = sqrt((self.__pontos[0].x - ponto.x) ** 2 + (self.__pontos[0].y - ponto.y) ** 2)
            p += d
        return f"{p:.2f}"
    
    def addPonto(self, ponto):
        self.__pontos.append(Ponto(ponto[0], ponto[1]))

    @property
    def pontos(self):
        return self.__pontos


pol1 = Poligno([Ponto(1, 1), Ponto(3, 1), Ponto(3, 3), Ponto(1, 3)])
# pol2 = Poligno([Ponto(4, 1), Ponto(7, 3), Ponto(6, 6), Ponto(2, 7), Ponto(1, 4)])

# print(pol1.perimetro())
# print(pol1.area())
print(pol1)