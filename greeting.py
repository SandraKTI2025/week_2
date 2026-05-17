#Programm Greeting
#Algus

last_name = input("Kirjuta oma perekonnanimi: ") #Küsi kasutajalt perekonnanimi
letter = input("Vali sugu M/N: ") #Küsi kasutajalt sugu
if letter == "M": #Kui sugu on mees, siis
    print(f"Tere, härra {last_name}!") #väljasta "Tere, härra [perekonnanimi]!"
elif letter == "N": #Kui sugu on naine, siis
    print(f"Tere, Proua {last_name}!") #väljasta "Tere, proua [perekonnanimi]!"
else: #Muidu
    print(f"Tere tulemast, {last_name} (sugu ei olegi tähtis).")  #väljasta "Tere tulemast, [perekonnanimi] (sugu ei olegi tähtis)!"

#Lõpp
