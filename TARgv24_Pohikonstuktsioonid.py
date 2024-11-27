from random import * # * - all functions    or   randint as rd funktsioonide ümbernimetus
#impor random -> random.randint()
from math import * #pi kasutamiseks

# Ülesanne 1
print ("Tere tulemast!")
nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa,upper()-AAA,capitalize()-Aaa
print("Tere tulemast! Tervitan sind ", nimi)
print("Tere tulemast! Tervitan sind "+ nimi)
try:
   vanus=int(input("Kui vana sa oled?"))
   print("Tere tulemast! Tervitan sind "+nimi+". Sa oled ",vanus,"aastat vana.")
   print(f"\tTere tulemast! \nTervitan sind {nimi}. Sa oled {vanus} aastat vana.") #{vanus:.2f}
except:
    print("On vaja numbreid sisestada!")

#Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

#Ülesanne 3
kokku=randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi=int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print(f"Jääk on {kokku} kommi")

#Ülesanne 4
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")

#Ülesanne 5
n=int(input("length 1: "))
m=int(input("length 2: "))
d=sqrt(n**2+m**2)
print("the length of the diagonal of a rectangular equals: ")
print(d)

#Ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg #changed places of teepikkus and aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesanne 7
a=float(input("1st number: "))
b=float(input("2nd number: "))
c=float(input("3rd number: "))
d=float(input("4th number: "))
e=float(input("5th number: "))


summa=float(a+b+c+d+e)
print("Sum is: ")
print(summa)
end=summa/5
print("Arithmetic mean of given integers is: ")
print(end)
