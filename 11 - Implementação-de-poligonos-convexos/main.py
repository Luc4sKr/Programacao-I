from poligno import Poligno
from ponto import Ponto
from lista_poligno import Lista_polignos

def criar_poligno():
    print("=============================")
    print("Criar Polígno")
    print("=============================")

    lista_pontos = []
    i = 0

    while True:
        pontox = float(input(f"Ponto x{i}: "))
        pontoy = float(input(f"Ponto y{i}: "))
        ponto = Ponto(pontox, pontoy)
        lista_pontos.append(ponto)

        if input("Continuar? [S/N]: ").upper() == "N":
            break

        i += 1

    poligno = Poligno(lista_pontos)
    lista_polignos.lista.append(poligno)

def listar_polignos():
    for poligno in lista_polignos.lista:
        print(poligno)

    

if __name__ == "__main__":
    global lista_pontos
    global lista_polignos

    lista_polignos = Lista_polignos()

    resp = None
    while True:
        print("=============================")
        print("1 - Criar polígno")
        print("2 - Listar polígnos")
        print("0 - Sair")
        print("=============================")

        
        resp = int(input("-> "))
        print("=============================")
        if resp == 1:
            criar_poligno()
        elif resp == 2:
            listar_polignos()
        elif resp == 0:
            break
        else:
            print("Resposta inválida!")
        

        




            