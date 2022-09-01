from cilindro import Cilindro

cilindro1 = Cilindro(10, 3)
cilindro2 = Cilindro(3, 10)
cilindro3 = Cilindro(7, 7)
cilindro4 = Cilindro(20, 10)

cilindros = [cilindro1, cilindro2, cilindro3, cilindro4]

print("------------------ Cilindros ------------------")
for i, cilindro in enumerate(cilindros):
    print(f"--- Cilindro {i+1} ---")
    print(f"Altura: {cilindro.altura}")
    print(f"Raio: {cilindro.raio}")
    print(f"Volume: {cilindro.calcular_volume():.2f}")
    print(f"Área base: {cilindro.calcular_area_base():.2f}")
    print(f"Área lateral: {cilindro.calcular_area_lateral():.2f}")
    print(f"Área toal: {cilindro.calcular_area_total():.2f}")
print("-----------------------------------------------")
