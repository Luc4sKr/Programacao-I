import datetime 
from calendar import isleap

class Data:
    
    def __init__(self, data):
        self.data = data
        self.validaData()

        self.lista_meses = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]
    
    def validaData(self):
        try:
            self.data = datetime.datetime.strptime(self.data, "%d %B, %Y").date()
        except:
            self.data = datetime.date(1, 1, 1)

        return self.data

    def compara(self, novaData):
        novaData = datetime.datetime.strptime(novaData, "%d %B, %Y").date()

        if self.data == novaData:
            return 0
        if self.data > novaData:
            return 1
        if self.data < novaData:
            return -1

    def getDia(self):
        return self.data.day
    
    def getMes(self):
        return self.data.month

    def getMesExtenso(self):
        return self.lista_meses[self.getMes()-1]

    def getAno(self):
        return self.data.year
    
    def isBissexto(self):
        if isleap(self.getAno()):
            return True    
        return False


