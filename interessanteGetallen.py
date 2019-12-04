#Kim Phung
#S1102710
#Interessante getallen Opdracht 5, week 2
#---------------------------------

#functie om uit te rekenen of n deelbaar is
def verkrijg_antwoord(testgeval: int) -> int:

    #natuurlijk_getal
    natuurlijk_getal = 1

    #een niet eindige loop
    while True:

        #totdat is_deelbaar en controleer_som beide waar zijn
        if is_deelbaar(testgeval, natuurlijk_getal) and controleer_som(
                testgeval, natuurlijk_getal):
            #stop de loop
            break

        #zo niet tel het getal op
        natuurlijk_getal += 1

    #geef het getal terug
    return natuurlijk_getal

#controleer of het getal deelbaar is || testgeval opgeven als integer, natuurlijkgetal als integer
def is_deelbaar(testgeval: int, natuurlijk_getal: int) -> bool:

    #True of False op basis van de boven gestelde vraag.
    return natuurlijk_getal % testgeval is 0

#contoleer of de losse digits van het natuurlijk getal gelijk zijn aan het opgegeven testgeval
def controleer_som(testgeval: int, natuurlijk_getal: int) -> bool:

    #de som van de digits/getallen lijst
    som = sum(list(map(int, str(natuurlijk_getal))))

    #geef terug of de getallen gelijk zijn aan elkaar
    return testgeval is som

#vraag input voor het aantal testgevallen
def verkrijg_aantal_testgevallen() -> int:

    #vraag
    vraag = "Aantal testgevallen"

    #vraag het aantal testgevallen
    aantal_testgevallen = stel_interger_vraag(vraag)

    #controleer of het wel minder dan 50 testgevallen zijn.
    while 0 < aantal_testgevallen > 50:
        #vraag het aantal testgevallen.
        aantal_testgevallen = stel_interger_vraag(vraag)

    #geef het aantal testgevallen terug.
    return aantal_testgevallen

#vraag input voor de testgeval(len)
def verkrijg_testgevallen(aantal_testgevallen: int) -> list:

    #lege array
    testgevallen = []

    #loop door elk testgeval heen
    for testgeval in range(0, aantal_testgevallen):

        #vraag in var
        vraag = "Testgeval " + str(testgeval + 1)

        #vraag het testgeval
        gegeven_testgeval = stel_interger_vraag(vraag)

        #controleer of het testgeval wel tussen de 0 en de 101 ligt
        while 0 < gegeven_testgeval > 100:
            #als niet loop de while loop en vraag weer
            gegeven_testgeval = stel_interger_vraag(vraag)

        #voeg testgeval aan de array
        testgevallen.insert(testgeval, gegeven_testgeval)

    #return de array
    return testgevallen

#vraag input met :
def stel_interger_vraag(vraag: str) -> int:

    return int(input(vraag + ": "))

#start de functies
def main() -> None:

    #verkrjg het aantal testgevallen
    aantal_testgevallen = verkrijg_aantal_testgevallen()

    #verkrijg het opgegeven aantal testgevallen
    testgevallen = verkrijg_testgevallen(aantal_testgevallen)

    #ga door elk testgeval heen
    for testgeval in testgevallen:
        #geef het antwoord op elk testgeval
        print(verkrijg_antwoord(int(testgeval)))

#start
if __name__ == "__main__":
    main()