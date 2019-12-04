#Kim Phung
#S1102710
#Sterke wachtwoorden Opdracht 8, week 3
#---------------------------------

#library die helpt met zoeken naar special characters
import re

def main():
    wachtwoorden = []
    #vraag aantal wachtwoorden
    aantalWachtwoorden = int(input("Aantal wachtwoorden: "))
    i = 0
    #vraag naar wachtwoord totdat aantal is bereikt
    for passwords in range(0, aantalWachtwoorden):
        i+=1
        vraag = "Wachtwoord " + str(i) + ": "
        wachtwoorden.append(str(input(vraag)))
    
    #var voor uitkomst
    veiligheidWachtwoorden = checkVeiligheid(wachtwoorden)
    for veiligheid in veiligheidWachtwoorden:
        print(veiligheid)

#function om wachtwoord te checken
def checkVeiligheid(wachtwoorden):
    #teller die punten bij houdt
    check = 0
    veiligheidWachtwoorden = []
    #voor elke wachtwoord loop het loop door
    for wachtwoord in wachtwoorden:
        #if meer dan 8 characters
        if len(wachtwoord) >= 8:
            check += 1
        #if contain uppercase
        if any(char.isupper() for char in wachtwoord):
            check += 1
        #if contain lowercase
        if any(char.islower() for char in wachtwoord):
            check += 1
        #if contain digit
        if any(char.isdigit() for char in wachtwoord):
            check += 1
        #if contain special character
        if bool(re.search('[^A-Za-z0-9]',wachtwoord)):
            check += 1
        
        #puntentelling
        if check <= 2:
            veiligheid = "zwak"
        
        if check > 2 and check <= 4:
            veiligheid = "matig"
            
        if check >= 5:
            veiligheid = "sterk"
            
        #punten weer resetten voor volgende loop
        check = 0
        #plak de uitkomst in de var list
        veiligheidWachtwoorden.append(veiligheid)

    return veiligheidWachtwoorden

if __name__ == "__main__":
    main()