def oblicz_pole_trapezu(a, b, h):
    return (a + b) * h / 2


a = float(input("Podaj długość pierwszej podstawy trapezu: "))
b = float(input("Podaj długość drugiej podstawy trapezu: "))
h = float(input("Podaj wysokość trapezu: "))

if a <= 0 or b <= 0 or h <= 0:
    print("Długości boków i wysokość muszą być dodatnie.")
else:
    pole = oblicz_pole_trapezu(a, b, h)
    print("Pole trapezu wynosi:", pole)
