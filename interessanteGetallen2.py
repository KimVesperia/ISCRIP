# Kim Phung
# S1102710
# Interessante getallen opdracht 4, oplevering 1
# ---------------------------------


def main():

    # Array voor aantal testgevallen
    testgevallen = []

    # Vraag input voor testgevallen en omzetten naar natuurlijke getallen
    t = int(input("Voer een aantal testgevallen in: "))

    # var voor numering
    i = 0

    # while loop om per testgeval een getal te vragen
    while len(testgevallen) < t:

        # numering na elk loop omhoog
        i += 1

        # var voor de console met numering meteen omzetten naar string
        vraag = "Testgeval " + str(i)  # Testgeval 1:.. etc..

        # var voor de input van een natuurlijke getal
        x = int(input(vraag + ": "))

        # voeg de getallen in de array
        testgevallen.append(int(x))

    #  print uitkomst door via de method som te gaan, 2e parameter is voor max in te stellen
    for getal in testgevallen:
        print(som(getal, 10000))


#  som method | parameter getal en max
def som(n, y):

    # natuurlijk
    test_geval = n

    # is getal onder 10000
    while test_geval <= y:
        tmp = test_geval

        # via de method som_cijfer wordt er door een loop gekeken of de som van de cijfer gelijk is aan n
        if som_cijfer(tmp) == n:
            return test_geval

        # testgeval wordt telkens opgeteld door het natuurlijk getal totdat het in de if state komt
        test_geval += n

    return "Uitkomst is groter dan 10000"


#  modulo
def som_cijfer(natuurlijk):
    tmp = 0
    while natuurlijk:
        tmp, natuurlijk = tmp + (natuurlijk % 10), natuurlijk // 10
    return tmp


if __name__ == "__main__":
    main()
