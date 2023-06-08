m = float(input("Podaj masę ciała (w kilogramach): "))
h = float(input("Podaj wysokość (w metrach): "))

g = 9.8  # Przyjęta wartość przyspieszenia ziemskiego w m/s^2

energia_potencjalna = m * g * h

print("Energia potencjalna wynosi:", energia_potencjalna, "jouli")
