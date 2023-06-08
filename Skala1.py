odleglosc_na_mapie = 7  # Wartość odległości na mapie w cm
skala_mapy = 1_000_000  # Skala mapy (np. 1:1 000 000)

odleglosc_rzeczywista = odleglosc_na_mapie * skala_mapy

print("Odległość rzeczywista z Poznania do Warszawy wynosi", odleglosc_rzeczywista, "cm.")
