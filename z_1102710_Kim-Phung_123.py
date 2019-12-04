# Opgave 1
#==========
# Versie    : Z
# Studentnr : 1102710
# Naam      : Kim Phung
# USB-nr: 123
# Opgave 2
def intro():
    print("\nDit programma vraagt om regels tekst, totdat je een lege regel invoert.Als je klaar bent met invoeren, drukt het programma alle regels af.Vervolgens wordt gevraagd of je de tekst wilt opslaan in een bestand.\n")
# =========
# Opgave 3
def voer_tekst_in():
    tekst = []
    
    while tekst != "":
        gebruiker = input("Geef een regel: ")
        if gebruiker != "":
            tekst.append(gebruiker)
        elif gebruiker == "":
            return tekst

#intro()

#print(voer_tekst_in())
        
# =========
# Opgave 4
def druk_tekst_af_op_scherm(tekst_lijst):
    print("\n".join(tekst_lijst))

#tekst = voer_tekst_in()
#druk_tekst_af_op_scherm(tekst)

# =========
# Opgave 5
def vraag_keuze(question, answer):
    count = 0
    while count == 0:
        question_ask = input(question)
        if question_ask in answer:
            return question_ask

#print(vraag_keuze("Wil je één of twee koekjes? (e/t): ", ("e", "t")))

# =========
# Opgave 6
def sla_op_in_bestand(filename, tekst_lijst):
    tekst = "\n".join(tekst_lijst)
    fp = open(filename, "w")
    fp.write(tekst)
    fp.close()      

#tekst = ['Dit is een tekst.', 'Het bestaat uit drie regels.', 'Dit is de derde regel.']
#sla_op_in_bestand("tekst.txt", tekst)

# =========
# Opgave 7
def sla_tekst_op(tekst_lijst):
    opslaan_vraag = vraag_keuze("Wilt u de tekst opslaan in een bestand? (j/n): ", ("j", "n"))
    if opslaan_vraag == "j":
        filename = input("Geef de naam van het bestand: ")
        try:
            my_file = open(filename)
            opslaan_vraag2 = vraag_keuze("Dit bestand bestaat al. Wilt u het overschrijven (j/n): ", ("j", "n"))
            if opslaan_vraag == "j":
                sla_op_in_bestand(filename,tekst_lijst)
            elif opslaan_vraag == "n":
                exit
                
        except IOError:
            sla_op_in_bestand(filename,tekst_lijst)
            
    elif opslaan_vraag == "n":
        exit
    
#tekst = ['Dit is een tekst.', 'Het bestaat uit tweeregels.']
#sla_tekst_op(tekst)# Aangeroepen terwijl het bestand test.txt al bestaat.

# =========
# Opgave 8
def tekstverwerker_app():
    intro()
    
    tekst = voer_tekst_in()
    print("")
    druk_tekst_af_op_scherm(tekst)
    print("")
    sla_tekst_op(tekst)
    weer_vraag = vraag_keuze("Wilt u nog een tekst invoeren? (j/n): ", ("j", "n"))
    
    while weer_vraag == "j":
        tekst = voer_tekst_in()
        print("")
        druk_tekst_af_op_scherm(tekst)
        print("")
        sla_tekst_op(tekst)
        weer_vraag = vraag_keuze("Wilt u nog een tekst invoeren? (j/n): ", ("j", "n"))
        
        if weer_vraag == "n":
            break
        
    if weer_vraag == "n":
        exit
        
# =========
# MAIN
# =====
def main():
    tekstverwerker_app()

if __name__ == '__main__':
    main()
