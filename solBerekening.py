# 1 sol duurt 24 uur, 39 minuten en 35,244 seconden: (variable is in seconden)
sol = (60*60*24) + 60*39 + 35.244

# string tekst in de output
solString = "sol ="

# aantal seconden in een dag = 86400
aantalAardseSecondenInDagen=60*60*24
# aantal seconden in een uur = 3600
aantalAardseSecondenInUren=60*60
# aantal seconden in een minuut = 60
aantalAardseSecondenInMinuten=60

# een input sol vragen van gebruiker
solInput = int(input("Hoeveel sol converten?: "))

# het input omrekenen in sol seconden
newSol = solInput * sol

# de nieuwe berekening word verdeeld in dagen
dagen = newSol // aantalAardseSecondenInDagen
newSol = newSol - (dagen * aantalAardseSecondenInDagen)

# de nieuwe berekening word verdeeld in uren
uren = newSol // aantalAardseSecondenInUren
newSol = newSol - (uren * aantalAardseSecondenInUren)

# de nieuwe berekening word verdeeld in minuten
minuten = newSol // aantalAardseSecondenInMinuten
newSol = newSol - (minuten * aantalAardseSecondenInMinuten)

#print van de berekening met een format om strings erbij te zetten
print(solInput,solString, "{0:.0f} dagen, {1:.0f} uren, {2:.0f} minuten en {3:.0f} seconden.".format(
    dagen, uren, minuten, newSol))