#list variable voor de ingevoerde muntstukken 
muntstukken = [] 

#invoer muntstuk
munt1 = int(input("Hoeveel 1 eurocent?: "))
#invoer toegevoegd naar de list
muntstukken.append(munt1)

munt2 = int(input("Hoeveel 2 eurocent?: "))
muntstukken.append(munt2)

munt3 = int(input("Hoeveel 5 eurocent?: "))
muntstukken.append(munt3)

munt4 = int(input("Hoeveel 10 eurocent?: "))
muntstukken.append(munt4)

munt5 = int(input("Hoeveel 20 eurocent?: "))
muntstukken.append(munt5)

munt6 = int(input("Hoeveel 50 eurocent?: "))
muntstukken.append(munt6)

munt7 = int(input("Hoeveel 1 euro munt?: "))
muntstukken.append(munt7)

munt8 = int(input("Hoeveel 2 euro munt?: "))
muntstukken.append(munt8)

#aantal ingevoerde munten
totaalMunten = munt1 + munt2 + munt3 + munt4 + munt5 + munt6 + munt7 + munt8

#waarde toekennen aan ingevoerde munt
munt1Value = munt1 * 0.01
munt2Value = munt2 * 0.02
munt3Value = round(munt3 * 0.05, 4)
munt4Value = munt4 * 0.10
munt5Value = munt5 * 0.20
munt6Value = munt6 * 0.50
munt7Value = munt7 * 1.00
munt8Value = munt8 * 2.00

#totale waarde
totaalValue = munt1Value + munt2Value + munt3Value + munt4Value + munt5Value + munt6Value + munt7Value + munt8Value

#print aantal en waarde
print("Totaal aantal munten zijn: ", totaalMunten)
print("Totaal waarde is: ", totaalValue)

