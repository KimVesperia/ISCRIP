#Kim Phung
#S1102710
#GSMoniemen Opdracht 10, week 3
#---------------------------------

def main():
    
    print("T9 ('Hallo')")
    print(T9('Hallo'))
    print("\n")
    print("T9 ('aanbod')")
    print(T9('aanbod'))
    print("\n")
    print("T9 ('bamboe')")
    print(T9('bamboe'))
    print("\n")
    print("aanbod | bamboe")
    GSMoniemen('aanbod', 'bamboe')
    print("\n")
    print("maandag | vrijdag")
    GSMoniemen('maandag', 'vrijdag')

#functie t9
def T9(woord):
    #maak het toetsenbord aan voor t9
    toetsenbord = ['abc','def', 'ghi', 'jkl',  'mno', 'pqrs', 'tuv', 'wxyz']
    #geen onderscheid tussen upper en lowercase
    wLowercase = woord.lower()
    woordcijferlijst = []
    #voor elk letter
    for letter in wLowercase:
        #voor elk toets
        for blok in toetsenbord:
            #kijk of de letter in het blok zit
            if letter in blok:
                #via de index de juiste nummer toegekend
                woordcijfer = int(toetsenbord.index(blok))
                #elke blok wordt cijfer opgeteld, want eerste cijfer begint bij 2 en list begint bij 0
                toets = int(woordcijfer) + 2
                #append elke toets naar het toetsenbord list
                woordcijferlijst.append(toets)
                #join de nummers in de list
                t9text = ''.join(str(i) for i in woordcijferlijst)
    return(t9text)

#functie die 2 woorden geeft, in de functie t9 zet en if else of het GSMoniem is
def GSMoniemen(woord1, woord2):
    if T9(woord1) == T9(woord2):
        print(True)

    else:
        print(False)
        
if __name__ == "__main__":
    main()