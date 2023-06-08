def sumuj_do_zadanej_sumy(zadana_suma):
    suma = 0
    while suma < zadana_suma:
        liczba = int(input("Podaj liczbę: "))
        suma += liczba

    print("Osiągnięto lub przekroczono zadaną sumę.")
    print("Suma wynosi:", suma)


zadana_suma = int(input("Podaj zadaną sumę: "))
sumuj_do_zadanej_sumy(zadana_suma)
