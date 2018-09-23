'''
Created on 17.09.2018

@author: michaelgress
'''

import time
from random import randint

# Spieler
mLP = [100] # myLebenspunbkte, Lebenspunkte des Spielers
mW = ['Faust'] # Ausgerüstete Waffe
mHP = [3] # ausgeübter Schaden
mI = [] # Inventar
mA = ["Unterhose"] # Kleidung, Rüstung
mS = [1] # Schutz der Kleidung
mG = [] #Zerstörte Gegenstände, Muell

# NPC

# Gegner

iWesen1LP = [10]
iWesen1HP = [2]
iWesen1A = [1]




# Einführung-------------------------------------------------


print('-----------------------')
print('\n        Escace')
print("\n-----------------------")
print("...")
print("...")
print("...")
print("Du erwachst.")
print("Nach einigen Sekunden der Gefühlslosigkeit und Desorientierung")
print("übernimmt ein pochender Schmerz an deinem Kopf deine Aufmerksamkeit.")
print("Du fässt an deinen Kopf...")
print("Als du deine Hand herunter nimmst klebt Blut an deinen Fingern.")
print("...")
print("Du versuchst dich daran zu erinnern, was als letztes geschehen ist,")
print("jedoch kannst du dich weder daran erinnern, wer du bist, noch wo du bist.")
print("Du hast nichts an, außer einer Unterhose.")
print("Nach ein paar Minuten fühlst du dich stark genug, um aufzustehen.")



def kryokammer(environment):
    
    cmdlist = ['umsehen',
               'benutze terminal',
               'gehe zu terminal', 
               'gehe zu informationsterminal',
               'benutze informationsterminal',
               'gehe zu Ausgang',
               'gehe zu tür',
               'untersuche kryokapsel',
               'benutze schalter',
               'ziehe kleidung an',
               'ziehe gefangenenoverall an',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        print("Du siehst dich etwas genauer in dem verdunkeltem Raum um.")
        print("So wie es scheint, befindest du dich in einer kleineren Kryokammer.")
        print("Der Raum ist spartanisch eingerichtet, drei Kryokapseln liegen auf")
        print("der gegenüberliegenden Seite des einzigen Ausgangs des Raumes.")
        print("Eine der Kryokapseln ist geöffnet, die anderen zwei sind verschlossen.")
        print("An jedes der Kryokapseln ist ein Informationsterminal angeschlossen.")
        if 'GefangenenOverall' in myAusruestung or 'GefangenenOverall' in myMuell:
            kryokammer(environment)
        else:
            print("Auf dem Boden neben der Kryokapsel, vor der du aufgewacht bist, liegt ein Gefangenenoverall.")
            kryokammer(environment)
        
    elif cmd == 'gehe zu terminal' or cmd == 'benutze terminal' or cmd == 'gehe zu informationsterminal' or cmd == 'benutze informationsterminal':
        time.sleep(0.5)
        print('Vor dir sind drei Terminals.')
        terminal(environment)
            
    elif cmd == 'gehe zu tür' or cmd == 'gehe zu Ausgang':
        time.sleep(0.5)
        print('Du stehst vor dem Ausgang.')
        time.sleep(1.5)
        print('Neben der Tür befindet sich ein Schalter für die Öffnung der Tür.')
        kryokammer(environment)
        
    elif cmd == 'benutze schalter':
        time.sleep(0.5)
        print('Ping\n----\n')
        time.sleep(1)
        print('Die Tür öffnet sich und grell blendendes Licht strahlt in den Raum.')
        time.sleep(2)
        print('Was möchtest du tun?\n')
        time.sleep(1)
        print('(1) Kryokammer weiter untersuchen?')
        print('(2) Kryokammer verlassen?')
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
            
        if cmd == '1':
            time.sleep(0.5)
            print("''Ich sollte mich besser noch etwas genauer umsehen''")
            time.sleep(1)
            print("Die Tür schließt sich nach einigen Sekunden wieder.")
            kryokammer(environment)          
        elif cmd == '2':
            time.sleep(0.5)
            print('Du verlässt den Raum')
            time.sleep(2)
            print("bu betrittst einen langen Gang, hinter dir schließt sich die Tür")
            flurSüd(environment)
                 
    elif cmd == 'untersuche kryokapsel':
        time.sleep(0.5)
        print('Du untersuchst die drei Kapseln.')
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("An der mittleren und linken Kapsel scheint nichts Auffällig zu sein.")
        time.sleep(3)
        print("In jeder der Kapseln liegt eine Person, nackt, die Innenscheibe der Kapsel ist verkratzt")
        time.sleep(3)
        print("'Die Kapseln wurden wohl aufgetaut, doch die Öffnung wurde nicht aktiv und die zwei")
        print("Schläfer sind wohl langsam erstickt.")
        time.sleep(6)
        print("...")
        time.sleep(2)
        print("welch grauenhafter Tod.'")
        time.sleep(3)
        print("Die rechte Kapsel ist offen, die Kapsel, vor der du bewusstlos lagst.")
        time.sleep(2)
        print("Ein kleiner Blutfleck ist genau dort, wo dein Kopf lag.")
        time.sleep(2)
        print("Du berührst deine Wunde, blickst zu den Leichen...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("'Mich hätte es wohl eindeutig schlimmer treffen können.'")
        kryokammer(environment)
        
    elif cmd == 'ziehe kleidung an' or cmd == 'ziehe gefangenenoverall an':
        if 'Gefangenenoverall' in myAusruestung or 'Gefangenenoverall' in myMuell:
            print("Du hattest den Gefangenenoverall bereits angezogen...")
            print("Hier liegt keiner mehr.")
            kryokammer(environment)
        else:
            print("Du ziehst den Gefangenenoverall an")
            print("Er ist recht unbequem und bietet wenig Schutz")
            print("'Immerhin besser als in Unterhosen rumzulaufen")
            myAusruestung.remove('Unterhose')
            myAusruestung.append('Gefangenenoverall')
            mySchutz.remove(1)
            mySchutz.append(2)
            kryokammer(environment)
            
        
                
def terminal(environment):
    
    time.sleep(0.5)
    print('Welches der Terminals willst du benutzen?')
    time.sleep(0.5)
    print('(1) Terminal links')
    time.sleep(0.2)
    print('(2) Terminal mitte')
    time.sleep(0.2)
    print('(3) Terminal rechts')
    time.sleep(0.2)
    print('(4) Beende Bedienung')   
    time.sleep(0.2) 
            
    cmdlist = ['1', '2', '3', '4',]
    cmd = getcmd(cmdlist)
            
    if cmd == '1':
        time.sleep(0.5)
        print('Ein Feld mit verschiedenen Auswahlmöglichkeiten ist auf dem Display zu sehen.')
        terminal1(environment)
    elif cmd == '2':
        print('Ein Feld mit verschiedenen Auswahlmöglichkeiten ist auf dem Display zu sehen.')
        terminal2(environment)
    elif cmd == '3':
        print('Ein Feld mit verschiedenen Auswahlmöglichkeiten ist auf dem Display zu sehen.')
        terminal3(environment)
    elif cmd == '4':
        print('Du wendest dich den Terminals ab.')
        kryokammer(environment)


def terminal1(environment):
    time.sleep(2)
    print("\n(1) ''Information zu Gefangenem''")
    time.sleep(0.2)
    print("(2) ''Status''") 
    time.sleep(0.2)
    print("(3) ''Öffnen''")
    time.sleep(0.2)
    print("(4) Gehe zu anderem Terminal")
    time.sleep(0.2)
    print("(5) Beende Bedienung")
    time.sleep(0.2)
        
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
        
    if cmd == '1':
        time.sleep(1)
        print("''\nDatei wird aufgerufen...")
        time.sleep(2)
        print("...Gefangener 034629/348/23")
        time.sleep(1)
        print("...Verlegung des Straftäters nach Omega Zetha")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...weitere Informationen sind nicht Verfügbar.\n''")
        terminal1(environment)
    elif cmd == '2':
        time.sleep(1)
        print("'' \nDatei wird aufgerufen...")
        time.sleep(2)
        print("...")
        time.sleep(0.8)
        print("Keine Lebenszeichen vorhanden, Subjekt Tod\n''")
        terminal1(environment)
    elif cmd == '3':
        time.sleep(1)
        print("'...")
        time.sleep(2.4)
        print("Das wäre wohl keine gute Idee, das lasse ich lieber bleiben'")
        terminal1(environment)
    elif cmd == '4':
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("Du wendest dich dem Rest des Raumes zu")
        kryokammer(environment)
        
def terminal2(environment):
    time.sleep(2)
    print("(1) ''Information zu Gefangenem''")
    time.sleep(0.2)
    print("(2) ''Status''") 
    time.sleep(0.2)
    print("(3) ''Öffnen''")
    time.sleep(0.2)
    print("(4) Gehe zu anderem Terminal")
    time.sleep(0.2)
    print("(5) Beende Bedienung")
    time.sleep(0.2)
        
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
        
    if cmd == '1':
        time.sleep(1)
        print("''\nDatei wird aufgerufen...")
        time.sleep(2.1)
        print("...Gefangener 946592/836/54")
        time.sleep(1.2)
        print("...Verlegung des Straftäters nach Omega Zetha")
        time.sleep(0.5)
        print("...")
        time.sleep(0.2)
        print("...weitere Informationen sind nicht Verfügbar.\n''")
        terminal1(environment)
    elif cmd == '2':
        time.sleep(1.2)
        print("'' \nDatei wird aufgerufen...")
        time.sleep(2.3)
        print("...")
        time.sleep(0.3)
        print("Keine Lebenszeichen vorhanden, Subjekt Tod\n''")
        terminal1(environment)
    elif cmd == '3':
        time.sleep(1)
        print("'...")
        time.sleep(2.4)
        print("Das wäre wohl keine gute Idee, das lasse ich lieber bleiben'")
    elif cmd == '4':
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("Du wendest dich dem Rest des Raumes zu")
        kryokammer(environment)
        
def terminal3(environment):
    time.sleep(2)
    print("(1) ''Information zu Gefangenem''")
    time.sleep(0.2)
    print("(2) ''Status''") 
    time.sleep(0.2)
    print("(3) ''Öffnen''")
    time.sleep(0.2)
    print("(4) Gehe zu anderem Terminal")
    time.sleep(0.2)
    print("(5) Beende Bedienung")
    time.sleep(0.2)
        
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
        
    if cmd == '1':
        time.sleep(1)
        print("''\nDatei wird aufgerufen...")
        time.sleep(2.1)
        print("...Gefangener 976663/124/11")
        time.sleep(1.2)
        print("...Verlegung des Straftäters nach Omega Zetha")
        time.sleep(0.5)
        print("...")
        time.sleep(0.2)
        print("...weitere Informationen sind nicht Verfügbar.\n''")
        terminal1(environment)
    elif cmd == '2':
        time.sleep(1.2)
        print("'' \nDatei wird aufgerufen...")
        time.sleep(2.3)
        print("...")
        time.sleep(0.3)
        print("...Kryokapsel manuell geöffnet...")
        time.sleep (0.7)
        print("...\n''")
        terminal1(environment)
    elif cmd == '3':
        time.sleep(1.5)
        print("''/n...")
        time.sleep(0.9)
        print("...Kapsel geöffnet")
    elif cmd == '4':
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("Du wendest dich dem Rest des Raumes zu")
        kryokammer(environment)
        
    
    
    
    
def flurSüd(environment):
    print("Du gehst den Gang entlang und kommst an eine Abzweigung")
    print("(1) Biege rechts ab")
    print("(2) Biege links ab")
    print("(3) Gehe zurück")
    
    cmdlist = ['1', '2', '3', 'umsehen',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print('Du entscheidest dich für den rechten Weg.')
        flurSüdRechts(environment)
    elif cmd == '2':
        print("Du gehst nach links")
        flurSüdLinks(environment)
    elif cmd == '3':
        print("Du gehst zurück")
        time.sleep(2)
        print("Du stehst vor der geschlossenen Tür zur Kryokammer.")
        time.sleep(1)
        print("(1) Öffne die Tür und betrete den Raum")
        print("(2) Gehe zurück")
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("Du öffnest die Tür und trittst herein.")
            print("In der Kryokammer ist alles wie zuvor.")
            kryokammer(environment)
        elif cmd == '2':
            flurSüd(environment)
    
    elif cmd == 'umsehen':
        print("Links und rechts führen zwei Gänge fort. Nach etwa")
        print("15 m biegen beide Wege in Richtung geradeaus.")
        flurSüd(environment)
        


def flurSüdRechts(environment):
    time.sleep(1)
    print("Du bewegst dich auf die Biegung nach links zu und schaust vorsichtig um die Ecke.")
    print("Ein leerer Gang führt zu einer Tür, links und rechts den Gang entlang befinden sich weitere Türen.")
    print("(1) Diesen Gang weiter gehen")
    print("(2) Die andere Abzweigung untersuchen")
    
    cmdlist = ['1', '2', 'umsehen',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("Als du langsam und leise den Weg entlang läufst hörst du hinter dir ein Geräusch")
        print("Du drehst dich um und siehst, das eine Art Notschleuse den Weg zurück zur Kryokammer schließt")
        print("Du rennst zurück, doch der Weg ist schon versperrt.")
        print("Als du dich wieder umdrehst, stehen zwei Menschen im Gang, einer weiter hinten, einer fasst direkt vor dir.")
        print("Du willst etwas sagen, da bemerkst du, dass der Mensch vor kaum menschlich aussieht.")
        print("Es streckt seine Arme nach dir aus.")
        print("(1) Angreifen")
        print("(2) Versuchen, mit Wesen zu reden")
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1' or cmd == 'greife an' or cmd == 'greife Wesen an':
            print("Du greifst das Wesen an.")
            KampfFlurSüdRechts1(environment)
            
        elif cmd == '2':
            print("Als du mit dem Wesen reden willst, greift es dich an.")
            KampfFlurSüdRechts2(environment)
            
        else:
            print("Als du etwas anderes machen wolltest, greift dich das Wesen zuerst an")
            KampfFlurSüdRechts2(environment)
        
    elif cmd == '2':
        print("Du entscheidest dich doch lieber für den anderen Weg...")
        flurSüdLinks(environment)
        
    elif cmd == 'umsehen':
        print("Als du dich etwas genauer umschaust, entdeckst du am Ende des Weges")
        print("eine Kamera. Sie scheint aktiv zu sein.")
        flurSüdRechts(environment)
        
        
def KampfFlurSüdRechts1(environment):
    print("hier wird gekämpft")
    kryokammer(environment)
    
def KampfFlurSüdRechts2(environment):
    print("hier wird gekämpft")
    kryokammer(environment)

    
def flurSüdLinks(environment):
    print('Ein Gefühl sagt dir, der linke Weg wird der Richtige sein.')
    print("An der Biegung angekommen, nimmst du Geräusche um die Ecke war.")
    print("Du schaust vorsichtig um die Ecke...")
    print("Du erblickst den Rücken einer auf den Knien sitzenden Person.")
    print("Sie bewegt sich, vor ihr scheint etwas zu liegen, was sie beschäftigt.")
    
    cmdlist = ['1',]
    cmd = getcmd(cmdlist)
    
    hauptzentrale(environment)
    
    # WICHTIG!!! Beschreibung des Raumes noch in flurSüdLinks/Rechts
    # Wichtig!!! Gespräch in eigener Environment
    
def hauptzentrale(environment): 
    print("Hier ist noch ein Mann in Uniform, schlecht geschnitten")
    print("Er schaut dich schockiert an und hält seine Waffe auf dich gerichtet")
    print("Streitgespräch mit verschiedenen Optionen (auch Tod)")
    print("Er stellt sich als einen Techniker des Raumschiffes vor?")
    print("Er bittet dich, einige Aufgaben für ihn zu erledigen")
    print("Aufgabe: Notenergieversorgung im Maschienenraum aktivieren (Untere Decks, Maschinenraum)")
    print("Aufgabe: Freigabe zur Evakuierung einleiten (Kommandozentrale)")
    print("Optional: Waffe beschaffen (Waffenkammer)")
    print("Optional: Nach Überlebenden Ausschau halten")
    
    cmdlist = ['benutze Fahrstuhl',]
    cmd = getcmd(cmdlist)
    
    if cmd == 'benutze Fahrstuhl':
        fahrstuhlEtageHauptzentrale(environment)
     
     
#fahrstühle
        
def fahrstuhlEtageHauptzentrale(environment):
    print('Was möchtest du tun?')
    print("(1) Etage 9 (Kommandozentrale)")
    print("(2) Etage 6 (MannschaftsQuartiere)")
    print("(3) Etage 5 (Waffenkammer)")
    print("(4) Etage 3 (Krankenstation)")
    print("(5) Etage 0 (Maschienendeck)")
    print("(6) steige aus dem Fahrstuhl (etage 4)")
    
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Der Fahrstuhl setzt sich in Bewegung...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")        
        time.sleep(0.5)
        print("...")        
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("Bing")
        time.sleep(1)
        print("Die Tür öffnet sich, du steigst heraus")
        FlurKommandozentrale(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Der Fahrstuhl setzt sich in Bewegung...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")        
        print("Bing")
        time.sleep(1)
        print("Die Tür öffnet sich, du steigst heraus")
        FlurMannschaftsquartiere(environment)
        
    elif cmd == '3':
        time.sleep(0.5)
        print("Der Fahrstuhl setzt sich in Bewegung...")
        time.sleep(0.5)
        print("...")      
        print("Bing")
        time.sleep(1)
        print("Die Tür öffnet sich, du steigst heraus")
        FlurWaffenkammer(environment)
        
    elif cmd == '4':
        time.sleep(0.5)
        print("Der Fahrstuhl setzt sich in Bewegung...")
        time.sleep(0.5)
        print("...")      
        print("Bing")
        time.sleep(1)
        print("Die Tür öffnet sich, du steigst heraus")
        FlurKrankenstation(environment)
        
    elif cmd == '5':
        time.sleep(0.5)
        print("Der Fahrstuhl setzt sich in Bewegung...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")        
        time.sleep(0.5)
        print("...")        
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("Bing")
        time.sleep(1)
        print("Die Tür öffnet sich, du steigst heraus")
        FlurMaschienendeck(environment)
        
    elif cmd == '6':
        print("Du steigst aus dem Fahrstuhl und betrittst die Hauptzentrale")
        hauptzentrale(environment)
        
        
        
# Kämpfe

 
        
    
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Haupteingaben
        
def getcmd(cmdlist):
    
    cmd = input('\nWas tust du: ')
    cmd = cmd.lower() # Eingegebene Großbuchstaben werden klein
    
    if cmd in cmdlist:
        return cmd
    
    elif cmd == 'hilfe':
        print("\n---------------------")
        print("- umsehen --> beschreibt Umgebung")
        print("- nutze 'Objekt/Person'")
        print("- gehe zu 'Objekt/Person'")
        print("- öffne 'Objekt'")
        print("- untersuche 'Gegenstand'")
        print("---------------------")
        return getcmd(cmdlist)
    
    elif cmd == 'siehe inventar':
        for x in myInventar:
            print(x)
        return getcmd(cmdlist)
            
    elif cmd == 'ziehe kleidung aus':
    
        if 'Unterhose' in myAusruestung:
            print("''Warum sollte ich meine Unterhose ausziehen!?...")
            print("  Die lasse ich schön an!...''")
            return getcmd(cmdlist)
        elif 'Gefangenenoverall' in myAusruestung:
            print("Beim Ausziehen des Overalls ist ein Riss entstanden...")
            print("Gegenstand nicht mehr nutzbar.")
            myAusruestung.remove('Gefangenenoverall')
            myAusruestung.append('Unterhose')
            myMuell.append('Gefangenenoverall')
            mySchutz.remove(2)
            mySchutz.append(1)
            return getcmd(cmdlist)
            
    
    else:
        time.sleep(0.5)
        print("\n...")
        time.sleep(0.5)
        print('Das kannst du hier nicht tun')
        time.sleep(1)
        print('...')
        time.sleep(0.5)
        return getcmd(cmdlist)
    
if __name__ == "__main__":
    environment = ['service port']
    kryokammer(environment)
