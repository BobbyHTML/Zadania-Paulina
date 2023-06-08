x = float(input("Podaj masę wody oceanicznej (w kilogramach): "))
y = float(input("Podaj masę soli rozpuszczonej (w gramach): "))

zasolenie = (y / x) * 1000

print("Średnie zasolenie Wszechoceanu wynosi:", zasolenie, "promili")
