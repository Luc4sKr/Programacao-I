from data import Data
from voo import Voo
from voo import Voo_Mod

from random import randint

if __name__ == "__main__":

    # Voos
    voo_normal = Voo(1, Data("21 December, 2022"))
    voo_modificado = Voo_Mod(2, Data("30 July, 2023"), 150, 20)

    # Carga de assentos no voo normal
    for assento in range(voo_normal.num_assentos):
        if randint(0, 1) == 1:
            voo_normal.ocupa(assento)
    
    # Carga de assentos no voo mod
    for assento in range(voo_modificado.num_assentos):
        if randint(0, 1) == 1:
            voo_modificado.ocupa(assento)

    # Imprime informações dos voos
    for voo in [voo_normal, voo_modificado]:
        print(f"{voo}\n")

    
    print(voo_normal.verifica(20)) # Verifica se o assento 20 está disponível
    print(voo_normal.proximoLivre(20)) # Retorna o número da próxima cadeira livre
    
    # Retorna o tipo do assento
    print(voo_modificado.tipo(45))
    print(voo_modificado.tipo(142))