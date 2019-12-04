#Kim Phung
#S1102710
#Caesarrotatie Opdracht 7, week 3
#---------------------------------

#max variable rotatie
aantalRotaties = 26

def main():
    #function input voor decrypt of decrypt
    # def getMode():
    #
    #     print('Wil je encrypten of decrypten?')
    #     print('Toets "e" of "d"')
    #     mode = input().lower()
    #
    #     if mode in 'encrypt e decrypt d'.split():
    #         return mode
    #
    #     else:
    #         print('"encrypt" of "e" of "decrypt" of "d".')

    #function input bericht
    def getMessage():
        rot_input = input('Voer het gecodeerd bericht in: ')
        return rot_input

    #function input rotatie
    def getKey():
        # key = 0

        key = int(input('Voer Caesarrotatie in (1-26): '))

        if (key >= 1 and key <= aantalRotaties):
            return key

    #function voor vertaling
    def getTranslatedMessage(message, key):
        #decrypt mode
        # if mode[0] == 'd':
        #     #rotatie
        key = -key
        #
        translated = ''

        for symbol in message:
            #if check alfabet only
            if symbol.isalpha():
                #convert de letter naar ASCII
                num = ord(symbol)
                num += key
                
                #if kleine letter
                if symbol.isupper():

                    #groter dan ASCII Z
                    if num > ord('Z'):
                        num -= 26
                    
                    #kleiner dan ASCII A
                    elif num < ord('A'):
                        num += 26
                
                #if groote letter
                elif symbol.islower():

                    #groter dan ASCII z
                    if num > ord('z'):
                        num -= 26

                    #groter dan ASCII a
                    elif num < ord('a'):
                        num += 26
                
                #vertaal met correcte rotatie
                translated += chr(num)

        return translated

    #start functies
    # mode = getMode()
    key = getKey()
    message = getMessage()

    print('Vertaalde tekst is: ' + getTranslatedMessage(message, key))
    

if __name__ == "__main__":
    main()