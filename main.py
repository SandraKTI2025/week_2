#Päeva kontroll
day = input("Mis päev on homme? (tööpäev/puhkepäev): ")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist")
else:
    print("Vale väärtus")

#Finantsnõustaja
print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsioonioste.")

money = int(input("Kui palju raha sul on praegu?: "))

if money < 2500:
    print("Sul pole piisavalt raha. Kogu edasi!")
elif money == 2500:
    print("Palju õnne, sul on piisavalt raha uue Iphone 17 Pro jaoks!")
else:
    print("Saad osta Iphone 17 Pro ja raha jääb isegi üle.")


#Sammulugeja
goal = 10000
steps = int(input("Mitu sammu oled juba teinud?: "))

percent = (steps / goal) * 100
print(f"{percent:.2f}%")

if percent < 50:
    print("Oled alles poolel teel, liigu veel!")
elif percent < 75:
    print("Tubli, oled peaaegu eesmärgi täitnud!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi saavutanud!")
