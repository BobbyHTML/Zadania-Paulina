objetosc = float(input("Podaj objętość wody (w litrach): "))
energia_dostarczona = float(input("Podaj ilość dostarczonej energii (w kJ): "))

cieplo_wlasciwe = 4200  # Ciepło właściwe wody w J/(kg K)
masa = objetosc * 1000  # Przeliczamy objętość wody na masę w gramach

przyrost_temperatury = energia_dostarczona / (masa * cieplo_wlasciwe)

print("Temperatura wzrośnie o:", przyrost_temperatury, "stopni Celsjusza")
