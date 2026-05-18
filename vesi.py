# Vee joomise programm

# Algus

goal = 2000 #Eesmärk 2 L ehk 2000 ml
glasses = int(input("Mitu klaasi vett sa oled täna joonud?:")) # Küsi kasutajalt mitu klaasi vett ta täna joonud on

ml = glasses * 250 #Arvuta joodud milliliitrid klaasid * 250
percent = (ml/goal)*100  #Arvuta protsendiliselt joodud kogus eesmärgist

print(f"{percent}%") # Too tulemus protsentides välja

if percent < 50: # Kui tulemus on alla 50 protsendi siis
    print("Joo rohkem vett, keha vajab seda!") # Väljasta "Joo rohkem vett, keha vajab seda!"
elif percent < 100: # Kui protsent on alla 100 siis
    print("Tubli jätka samas vaimus !") # Väljasta "Tubli, jätka samas vaimus!"
else: # Muidu
    print("Suurepärane, oled oma päevase eesmärgi täitnud!") # Väljasta "Suurepärane, oled oma päevase eesmärgi täitnud!"

# Lõpp
