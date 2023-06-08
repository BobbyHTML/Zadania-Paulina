import random

liczby = []
for _ in range(5):
    liczba = random.randint(1, 100)
    liczby.append(liczba)

print("Wygenerowane liczby pseudolosowe:")
print(liczby)
