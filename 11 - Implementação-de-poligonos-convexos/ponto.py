class Ponto:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return f"({self.__x:.2f}, {self.__y:.2f})"

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
