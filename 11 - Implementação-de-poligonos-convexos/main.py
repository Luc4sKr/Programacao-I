from poligno import Poligno
from ponto import Ponto
from charge import Charge


if __name__ == "__main__":
    charge = Charge([])
    charge.run()


    resp = None
    while True:
        print("1 - Criar polígno")
        print("2 - Listar polígnos")
        print("0 - Sair")

        try:
            resp = int(input("-> "))
        except:
            print("Resposta inválida")

        if resp == 0:
            break
        elif resp == 1:
            pass