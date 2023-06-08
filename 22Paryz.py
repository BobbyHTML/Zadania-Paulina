szerokosc_geograficzna = 49  # szerokość geograficzna Paryża
deklinacja_slonca = 23.5

wysokosc_gorowania = 90 - (szerokosc_geograficzna - deklinacja_slonca)

print("Wysokość górowania Słońca nad horyzontem w Paryżu (22 czerwca):", wysokosc_gorowania, "stopni")
