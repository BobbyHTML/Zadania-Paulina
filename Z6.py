stężenie = float(input("Podaj stężenie roztworu soli A (w g/dm³): "))
temperatura = float(input("Podaj temperaturę roztworu (w °C): "))

if stężenie >= 100 and temperatura >= 20:
    print("Roztwór soli A jest nasycony z osadem.")
elif stężenie >= 100:
    print("Roztwór soli A jest nasycony.")
else:
    print("Roztwór soli A jest nienasycony.")
