def czy_pierwsza(liczba):
    if liczba < 2:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False

    return True


n = int(input("Podaj wartość maksymalną: "))

print("Liczby pierwsze do", n, "to:")
for liczba in range(2, n + 1):
    if czy_pierwsza(liczba):
        print(liczba)
