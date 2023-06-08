temperatura_poczatkowa = 25.0  # Temperatura na wysokości 848 m npm w stopniach Celsiusza
spadek_temperatury_na_100m = 0.5  # Spadek temperatury na 100 m w stopniach Celsiusza

wzniesienia_100m = (8848 - 848) // 100  # Obliczenie liczby pełnych 100-metrowych wzniesień

temperatura_koncowa = temperatura_poczatkowa - (spadek_temperatury_na_100m * wzniesienia_100m)

print("Temperatura na szczycie Mount Everest wynosi:", temperatura_koncowa, "°C")
