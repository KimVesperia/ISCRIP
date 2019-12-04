#Kim Phung
#S1102710
#Levensverwachting Opdracht 9, week 3
#---------------------------------

def main():
    #geen invoer dus direct in de main printen
    #print de functie en stel de variable in
    print("1: ", levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True))
    print("2: ", levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True))
    print("3: ", levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False))
    print("4: ", levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True))
    print("5: ", levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False))

#function voor levensverwachting en zet variable in
def levensverwachting(geslacht, roker, sport, alcohol, fastfood):
    #default leven
    verwachting = 70
    
    #if vrouw +4
    if geslacht == "vrouw":
        verwachting += 4
    else:
        verwachting
    
    #als je niet rookt +5 else -5
    if roker is False:
        verwachting += 5 
    else:
        verwachting -= 5

    #als je sport keer aantal uren else -3 niet sport
    if sport > 0:
        verwachting += sport
    else:
        verwachting -= 3
     
    #als je niet drinkt +2
    if alcohol is 0:
        verwachting += 2
    else:
        #meer dan 7 drinkt half jaar eraf
        if alcohol > 7:
            verwachting = verwachting -(alcohol - 7) / 2
        #onder de 7
        else:
            verwachting += 0
    
    #fastfood boolean check
    #if geen fastfood dan +3
    if fastfood is False:
        verwachting += 3
    else:
        verwachting += 0

    return verwachting

if __name__ == "__main__":
    main()