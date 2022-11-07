from poligno import Poligno
from ponto import Ponto


if __name__ == "__main__":
    resp = None
    while True:
        print("=============================")
        print("1 - Criar polígno")
        print("2 - Listar polígnos")
        print("0 - Sair")
        print("=============================")

        try:
            resp = int(input("-> "))
            print("=============================")

            if resp == 1:
                break
            elif resp == 2:
                pass
            elif resp == 0:
                pass
        except:
            print("=============================")
            print("ERRO! Resposta inválida")

        

        