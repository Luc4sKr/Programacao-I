from data import Data
from voo import Voo
from voo_modificado import Voo_Modificado

from random import randint

if __name__ == "__main__":

    # Voos
    vooNormal = Voo(1, Data("21 December, 2022"))
    vooMod = Voo_Mod(2, Data("30 July, 2023"), 150, 20)

    # Carga de assentos no voo normal
    for assento in range(vooNormal.num_assentos):
        if randint(1, 2) == 2:
            vooNormal.ocupa(assento)
    
    # Carga de assentos no voo mod
    for assento in range(vooMod.num_assentos):
        if randint(1, 2) == 2:
            vooMod.ocupa(assento)

    for voo in [vooNormal, vooMod]:
        print(f"{voo}\n")

    
    print(vooNormal.verifica(20)) # Verifica se o assento 20 está disponível
    print(vooNormal.proximoLivre(20)) # Retorna o número da próxima cadeira livre
    
    # Retorna o tipo do assento
    print(vooMod.tipo(45))
    print(vooMod.tipo(142))