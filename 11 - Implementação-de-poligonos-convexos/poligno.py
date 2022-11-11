from math import sqrt

class Poligno:
    def __init__(self, pontos) -> None:
        self.__pontos = pontos

    def __str__(self) -> str:
        s = "\n"
        return f"""-------------------
Polígno
-------------------
Pontos:
{s.join(map(str, self.__pontos))}
Perimetro: {self.perimetro()}
Area: {self.area()}
-------------------"""

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
        self.__pontos.append(ponto)

    @property
    def pontos(self):
        return self.__pontos
