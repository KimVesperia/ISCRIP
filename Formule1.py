#Kim Phung
#S1102710
#Formule 1 Opdracht 4, week 2
#---------------------------------

#Maak inputs aan en vraag naar de gegevens
prijs = (input("Wat is de prijs?: "))
km = float(input("Hoeveel KM is een ronde?: "))
tijd = float(input("Wat is gemiddelde tijd van een ronde?: "))

#Zet de naam van de race hoofdletters voor netheid en Monaco if statement
newPrijs = prijs[:1].upper() + prijs[1:]

#Bereken hoeveel rondes er zijn
newRound = 305 / km

#Afronden
newRound2 = round(newRound)

#Totaal tijd van de race
totalTime = tijd * newRound2

#Als prijs Monaco is
if (newPrijs == "Monaco"):
    #Ronde staat al vast
    newRound2 = 78
    #Totaal km berekenen
    newKm = newRound2 * km

#Als race langer dan 2uur duurt
if (totalTime > 120):
    
    #Zolang het langer dan 2 uur duurt rondes en tijd eraf halen
    while totalTime > 120:
        newRound2-=1
        totalTime-=tijd
    
    #Uit de loop om ronde af te maken en alles opnieuw berekenen en afronden
    newRound2+=1
    newKm = newRound2 * km
    newKm2 = round(newKm,3)
    kmPower = "(" + str(newKm2) + " km)."
    
    #Print uitkomst
    print ("De grote prijs van",newPrijs,"wordt verreden over",newRound2,"ronden",kmPower)
#Als korter dan 2uur is gaat het hierin
else:
    #Alles berekenen zoals hierboven
    newKm = newRound2 * km
    newKm2 = round(newKm,3)
    kmPower = "(" + str(newKm2) + " km)."
    print ("De grote prijs van",newPrijs,"wordt verreden over",newRound2,"ronden",kmPower)