liczba_dziesietna = int(input("Podaj liczbę dziesiętną: "))

if liczba_dziesietna < 0:
    print("Podaj liczbę dodatnią.")
else:
    liczba_dwojkowa = bin(liczba_dziesietna)[2:]
    print("Liczba w systemie dwójkowym:", liczba_dwojkowa)
