# Päeva kontroll
päev = input("Mis päev on homme? (tööpäev/puhkepäev): ")

if päev == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif päev == "puhkepäev":
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus – palun sisesta 'tööpäev' või 'puhkepäev'.")


# Finantsnõustaja
print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsioonioste.")

raha = int(input("Kui palju raha sul praegu on?: "))

if raha < 2500:
    print("Sul pole piisavalt raha. Kogu edasi!")
elif raha == 2500:
    print("Palju õnne, sul on täpselt piisavalt raha uue iPhone 17 Pro jaoks!")
else:
    print("Saad osta iPhone 17 Pro ja raha jääb isegi üle.")


# Sammulugeja
eesmärk = 10000
sammud = int(input("Mitu sammu oled juba teinud?: "))

protsent = (sammud / eesmärk) * 100
print(f"{protsent:.2f}%")

if protsent < 50:
    print("Oled alles poolel teel, liigu veel!")
elif protsent < 75:
    print("Tubli, oled peaaegu eesmärgi täitnud!")
elif protsent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi saavutanud!")
