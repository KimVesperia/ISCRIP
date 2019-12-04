#Kim Phung
#S1102710
#Slaapkwaliteit Opdracht 6, week 2
#---------------------------------

#importeer datum en tijd library
import datetime

#Vraag input voor tijd slapen en wakker worden
uurSlaap = int(input("Welke uur slaap je: "))
minSlaap = int(input("Welke minuut slaap je: "))

uurOpstaan = int(input("Welke uur sta je op: "))
minOpstaan = int(input("Welke minuut sta je op: "))

sleepTime = datetime.time(uurSlaap, minSlaap)
wakeTime = datetime.time(uurOpstaan, minOpstaan)

#importeer voor meer toegankelijkheden
from datetime import datetime, date, time

#Trek gewenste opstaan tijd met slaaptijd voor verschillen
printTime = datetime.combine(date.min, wakeTime) - datetime.combine(date.min, sleepTime)

#Convert integers van input naar datetime
sleepDelta = datetime.combine(date.min, sleepTime)
wakeDelta = datetime.combine(date.min, wakeTime)

import datetime

#if statement om datum(dag) niet op te tellen
if (printTime > datetime.timedelta(days=0)):
    newTime = printTime 
    
else:
    newTime = printTime + datetime.timedelta(days=1)

#If statements om te kijken hoe lang de gebruiker slaapt voor elk uur
    #Tussen 1 en 2 uur
if (newTime <= datetime.timedelta(0, 3600) or newTime >= datetime.timedelta(0, 3600) and newTime < datetime.timedelta(0, 7200)):
    #Slaaptijd + de juiste REM slaap berekent door in de juiste if statement te zijn en daarbij de juiste aantal seconden erbij gerekent
    finishTime = sleepDelta + datetime.timedelta(0, 5400)
    #print("na 1 uur, opstaan om", finishTime) <----- voor elke if hierbinnen een eigen print voor het testen
    
#Elke elif hieronder geldt hetzelde als hierboven maar met de juiste berekening en uren    
elif (newTime >= datetime.timedelta(0, 7200) and newTime < datetime.timedelta(0, 10800)):
    finishTime = sleepDelta + datetime.timedelta(0, 10800)
    #print("na 2 uur", finishTime)
    
elif (newTime >= datetime.timedelta(0, 10800) and newTime < datetime.timedelta(0, 14400)):
    finishTime = sleepDelta + datetime.timedelta(0, 10800)
    #print("na 3 uur", finishTime)
    
elif (newTime >= datetime.timedelta(0, 14400) and newTime < datetime.timedelta(0, 18000)):
    finishTime = sleepDelta + datetime.timedelta(0, 16200)
    #print("na 4 uur", finishTime)
    
elif (newTime >= datetime.timedelta(0, 18000) and newTime < datetime.timedelta(0, 21600)):
    finishTime = sleepDelta + datetime.timedelta(0, 21600)
    #print("na 5 uur", finishTime)
    
elif (newTime >= datetime.timedelta(0, 21600) and newTime < datetime.timedelta(0, 25200)):
    finishTime = sleepDelta + datetime.timedelta(0, 21600)
    #print("na 6 uur", finishTime)
    
elif (newTime >= datetime.timedelta(0, 25200) and newTime < datetime.timedelta(0, 28800)):
    finishTime = sleepDelta + datetime.timedelta(0, 27000)
    #print("na 7 uur", finishTime)
    
elif (newTime >= datetime.timedelta(0, 28800)):
    finishTime = sleepDelta + datetime.timedelta(0, 32400)
    #print("Langer dan 8 uur geslapen.. you lazy", finishTime)

#print ("Verschil is",newTime) <--- verschil uitprinten van wakker en slaap tijd
    
#Print de uitkomst van het beste tijd om wakker te worden en haal de datum en seconden weg en 24modus
print (finishTime.strftime("%H:%M"))

#Eigen berekening voor REM slaap
#1.30 uur slaap is 90min
#3.00 = 180
#4.30 = 270
#6.00 = 360
#7.30 = 450
#9.00 = 540

