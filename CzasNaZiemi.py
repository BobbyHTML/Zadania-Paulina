# Zadanie 1: Obliczanie różnicy czasów miejscowych na podstawie różnicy długości geo.

różnica_długości = 140 - 20  # Różnica długości geograficznej między Krakowem a Tokio
różnica_czasu = różnica_długości * 4  # Różnica czasu miejscowego w minutach
godzina_startowa = 10  # Godzina w Krakowie

godzina_tokio = godzina_startowa + różnica_czasu // 60  # Obliczenie godziny w Tokio

print("W Tokio (140 stopni E) jest godzina:", godzina_tokio)


# Zadanie 2: Obliczanie różnicy długości geo. na podstawie różnicy czasów miejscowych

różnica_czasu = 144  # Różnica czasu miejscowego między Krakowem a innym miastem
różnica_długości = różnica_czasu / 4  # Różnica długości geograficznej w stopniach

print("Miasto, w którym jest godzina 21:24, leży na", różnica_długości, "stopniu długości geograficznej.")
