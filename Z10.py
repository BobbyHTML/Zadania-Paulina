minuty = int(input("Podaj liczbę minut: "))

godziny, pozostale_minuty = divmod(minuty, 60)

print("Czas to:", godziny, "godzin(i) i", pozostale_minuty, "minut(y)")
