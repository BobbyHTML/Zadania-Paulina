masa_otrzymana = float(input("Podaj masę produktu otrzymanego (w gramach): "))
masa_teoretyczna = float(input("Podaj masę produktu wynikającą z równania reakcji (w gramach): "))

wydajność = (masa_otrzymana / masa_teoretyczna) * 100

if wydajność > 100:
    wydajność = 100

print("Wydajność reakcji wynosi:", wydajność, "%")
