odleglosc_rzeczywista = 40  # Wartość rzeczywistej odległości w km
skala_mapy = 1_000_000  # Skala mapy (np. 1:1,000,000)

odleglosc_na_mapie = odleglosc_rzeczywista * skala_mapy * 100  # Przeliczamy km na cm

print("Odległość na mapie w skali 1:1,000,000 wynosi", odleglosc_na_mapie, "cm.")
