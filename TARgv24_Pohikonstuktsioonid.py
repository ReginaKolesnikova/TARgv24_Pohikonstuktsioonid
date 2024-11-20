from random import * # * - all functions    or   randint as rd funktsioonide ümbernimetus
#impor random -> random.randint()
from math import * #pi kasutamiseks

# # Ülesanne 1
# print ("Tere tulemast!")
# nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa,upper()-AAA,capitalize()-Aaa
# print("Tere tulemast! Tervitan sind ", nimi)
# print("Tere tulemast! Tervitan sind "+ nimi)
# vanus=int(input("Kui vana sa oled?"))
# print("Tere tulemast! Tervitan sind "+nimi+". Sa oled ",vanus,"aastat vana.")
# print(f"\tTere tulemast! \nTervitan sind {nimi}. Sa oled {vanus} aastat vana.") #{vanus:.2f}

# #Ülesanne 2
# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print(type(vanus))
# print(type(eesnimi))
# print(type(pikkus))
# print(type(kas_käib_koolis))

# #Ülesanne 3
# kokku=randint(1,1000)
# print(f"Kokku on {kokku} kommi")
# kommi=int(input("Mitu kommi sa tahad? "))
# kokku=kokku-kommi
# print(f"Jääk on {kokku} kommi")

#Ülesanne 4
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")
