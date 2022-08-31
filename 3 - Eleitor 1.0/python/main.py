from eleitor import Eleitor

e1 = Eleitor("Lucas", 17, 122)
e2 = Eleitor("Maria", 16, 123)
e3 = Eleitor("Josefino", 77, 27)
e4 = Eleitor("Carlos", 22, 98)

print("----------- Eleitores -----------")
print(e1.verificar())
print(e2.verificar())
print(e3.verificar())
print(e4.verificar())
print("---------------------------------")
