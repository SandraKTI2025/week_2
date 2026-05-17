#Vee joomise programm

#Algus
eesmark = 2000  # Eesmärk 2 L ehk 2000 ml
klaasid = int(input("Mitu klaasi vett sa oled täna joonud?: "))  # Küsi kasutajalt mitu klaasi vett ta täna joonud on

ml = klaasid * 250  # Arvuta joodud milliliitrid (klaasid * 250)
protsent = (ml / eesmark) * 100  # Arvuta protsent eesmärgist

print(f"{protsent:.2f}%")  # Too tulemus protsentides välja (2 komakohta)

if protsent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif protsent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")

#Lõpp
