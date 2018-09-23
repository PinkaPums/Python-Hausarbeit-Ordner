'''
Created on 21.09.2018

@author: michaelgress
'''

import time
from random import randint

# Spieler
mLP = [90] # myLebenspunbkte, Lebenspunkte des Spielers
mW = ['Faust'] # Ausgerüstete Waffe
mHP = [3] # ausgeübter Schaden
mI = [ ] # Inventar
mAus = ["Unterhose"] # Kleidung, Rüstung
mS = [1] # Schutz der Kleidung
mLuck = [1]

mG = [] #Zerstörte Gegenstände, Muell
mG2 = [] #Zerstörte Gegenstände, Muell
mG3 = [] #Zerstörte Gegenstände, Muell
mG4 = [] #Zerstörte Gegenstände, Muell
mG5 = []
mG6 = []
mG7 = []
mG8 = []

# Dauerhafte Schäden

mLippeAb = ['Dran']
mLosungswort = ['Bitteschön']
mStoffKuscheltier = ['Rotauge']
mMonsterGesehen = ['Nein']
iVerProf = ['Verrückt']
iBewFrau = ['Aggressiv']
iMedAbtEingang = ['Verschlossen']
iTürHPasswort = ['Unbekannt']
iNarrezMerana = ['Unwissend']
iGenerator = ['Aus']
iKleineRüstung = ['Raum']

# Verbrauchbare Gegenstände

medikit1 = ['Unbenutzt']

# Gegner

iWesen1LP = [6]
iWesen1HP = [2]
iWesen1S = [1]

iWesen2LP = [8]
iWesen2HP = [3]
iWesen2S = [1]

iEtwasLP = [11]
iEtwasHP = [4]
iEtwasS = [1]

iNarrezLP = [70]
iNarrezHP = [12]
iNarrezS = [6]

iWulffLP = [30]
iWulffHP = [8]
iWulffS = [2]
iWulffLuck = []

iMMonsterLP = [100]
iMMonsterHP = [25]
iMMonsterS = [1]

iRotAuge1LP = [16]
iRotAuge1HP = [6]
iRotAuge1S = [2]
iRotAuge1Luck = []

iRotAuge2LP = [13]
iRotAuge2HP = [7]
iRotAuge2S = [2]
iRotAuge2Luck = []

iRotAuge3LP = [20]
iRotAuge3HP = [8]
iRotAuge3S = [3]
iRotAuge3Luck = []

iRotAuge4LP = [18]
iRotAuge4HP = [8]
iRotAuge4S = [2]

iRotAuge5LP = [15]
iRotAuge5HP = [9]
iRotAuge5S = [1]

iRotAuge6LP = [12]
iRotAuge6HP = [10]
iRotAuge6S = [3]




# Einführung-------------------------------------------------
print("PROUDLYPRESENTEDGAMES proudly presents")
print("a HAEFEM gamestudio gamy game")
print("in cooperation with PYTHONKURSFU+00FCREINSTEIGER animation studios")

def startBildschirm(environment):
    print("---------------------------------------------------------\n")
    time.sleep(0.1)
    print("                        DYSTOPIA                        ")
    print("")
    print("                          oder:                            ")
    print("")
    print("  Entkomme aus dem Raumschiff und geh dabei nicht drauf  ")
    time.sleep(0.1)
    print("\n---------------------------------------------------------\n")
    print("                            play")
    time.sleep(0.2)
    print("                            help")
    time.sleep(0.2)
    print("                            quit")
    time.sleep(0.2)
    
    cmdlist = ['play', 'quit', 'help', 'pay', 'skip']
    cmd = getcmd(cmdlist)
    
    if cmd == 'play':
        time.sleep(1)
        print("Spiel wird gestartet")
        time.sleep(1)
        print("Bevor wir mit dem Spiel starten, hier noch ein kleiner Tipp:")
        time.sleep(1)
        print("    Es ist fast immer hilfreich, sich in Räumen umzusehen   ")
        time.sleep(1)
        print("            Gebe hierzu den Befehl 'umsehen' ein            ")
        time.sleep(1)
        print("                Nun viel Spaß beim Spielen...               ")
        time.sleep(1)
        intro(environment)
    elif cmd == 'quit':
        time.sleep(1)
        print("Spiel wird beendet")
        time.sleep(1)
        exit()
    elif cmd == 'help':
        time.sleep(1)
        print("Falls du während dem Spiel Probleme bekommst, gebe 'hilfe' ein, um")
        print("Möglichkeiten der Eingabe zu erhalten.")
        time.sleep(2)
        print()
        time.sleep(2)
        print()
        startBildschirm(environment)
    elif cmd == 'pay':
        time.sleep(1)
        print("Vielen Dank für ihren Einkauf")
        print("Es werden 10.000 Mark an den Entwickler überwiesen")
        print("Beehren Sie uns bald wieder :)")
        time.sleep(4)
        startBildschirm(environment)
    elif cmd == 'skip':
        treppenhausGZ(environment)
        
    
def intro(environment):    
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Du erwachst.")
    time.sleep(3)
    print("Nach einigen Sekunden der Gefühlslosigkeit und Desorientierung")
    print("übernimmt ein pochender Schmerz an deinem Kopf deine Aufmerksamkeit.")
    time.sleep(5)
    print("Du fässt an deinen Kopf...")
    time.sleep(2)
    print("Als du deine Hand herunter nimmst klebt Blut an deinen Fingern.")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("Du versuchst dich daran zu erinnern, was als letztes geschehen ist,")
    print("jedoch kannst du dich weder daran erinnern, wer du bist, noch wo du bist.")
    print("Du hast nichts an, außer einer Unterhose.")
    time.sleep(7)
    print("Nach ein paar Minuten fühlst du dich stark genug, um aufzustehen.")
    time.sleep(3)
    kryokammer(environment)


# Umgebung - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def kryokammer(environment):
    
    cmdlist = ['umsehen',
               'benutze terminal',
               'gehe zu terminal', 
               'gehe zu informationsterminal',
               'benutze informationsterminal',
               'gehe zu ausgang',
               'gehe zu tür',
               'untersuche ausgang',
               'untersuche tür',
               'benutze ausgang',
               'benutze tür',
               'untersuche kryokapsel',
               'benutze schalter',
               'ziehe kleidung an',
               'ziehe gefangenenoverall an',
               'ziehe overall an',
               'skip'
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich etwas genauer in dem verdunkeltem Raum um.")
        time.sleep(1.5)
        print("So wie es scheint, befindest du dich in einer kleineren Kryokammer.")
        time.sleep(1.5)
        print("Der Raum ist spartanisch eingerichtet, drei KRYOKAPSELn liegen auf")
        print("der gegenüberliegenden Seite des einzigen AUSGANGs des Raumes.")
        time.sleep(4)
        print("Zwei der Kryokapseln sind geöffnet, die andere ist verschlossen.")
        time.sleep(1.5)
        print("An jedes der Kryokapseln ist ein INFORMATIONSTERMINAL angeschlossen.")
        time.sleep(1.5)
        if 'Gefangenenoverall' in mAus or 'Gefangenenoverall' in mG:
            kryokammer(environment)
        else:
            print("Auf dem Boden neben der Kryokapsel, vor der du aufgewacht bist, liegt ein GEFANGENENOVERALL.")
            kryokammer(environment)
        
    elif cmd == 'gehe zu terminal' or cmd == 'benutze terminal' or cmd == 'gehe zu informationsterminal' or cmd == 'benutze informationsterminal':
        time.sleep(0.5)
        print('Vor dir sind drei Terminals.')
        time.sleep(0.5)
        terminal(environment)
            
    elif cmd == 'gehe zu tür' or cmd == 'gehe zu ausgang' or cmd == 'benutze ausgang' or cmd == 'benutze tür' or cmd == 'öffne ausgang' or cmd == 'öffne tür':
        time.sleep(0.5)
        print('Du stehst vor dem Ausgang.')
        time.sleep(1)
        print('Neben der Tür befindet sich ein SCHALTER für die Öffnung der Tür.')
        time.sleep(1)
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
        time.sleep(0.5)
        print('(2) Kryokammer verlassen?')
        time.sleep(0.5)
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
            
        if cmd == '1':
            time.sleep(0.5)
            print("''Ich sollte mich besser noch etwas genauer umsehen.''")
            time.sleep(1)
            print("Die Tür schließt sich nach einigen Sekunden wieder.")
            time.sleep(0.5)
            kryokammer(environment)          
        elif cmd == '2':
            time.sleep(0.5)
            print('Du verlässt den Raum.')
            time.sleep(2)
            print("bu betrittst einen langen Gang, hinter dir schließt sich die Tür.")
            time.sleep(0.5)
            print("Du gehst den Gang entlang und kommst an eine Abzweigung.")
            time.sleep(0.5)
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
        time.sleep(0.5)
        kryokammer(environment)
        
    elif cmd == 'ziehe kleidung an' or cmd == 'ziehe gefangenenoverall an' or cmd == 'ziehe overall an':
        if 'Gefangenenoverall' in mAus or 'Gefangenenoverall' in mG:
            time.sleep(0.5)
            print("Du hattest den Gefangenenoverall bereits angezogen...")
            time.sleep(1)
            print("Hier liegt keiner mehr.")
            time.sleep(1)
            kryokammer(environment)
        elif mAus[0] != "Unterhose":
            time.sleep(0.5)
            print("Ziehe dir erst deine Kleidung aus, bevor du dir neue anziehst.")
            time.sleep(1.5)
            kryokammer(environment)
        else:
            time.sleep(0.5)
            print("Du ziehst den Gefangenenoverall an.")
            time.sleep(1)
            print("Er ist recht unbequem und bietet wenig Schutz.")
            time.sleep(1)
            print("'Immerhin besser als in Unterhosen rumzulaufen.'")
            mAus.remove('Unterhose')
            mAus.append('Gefangenenoverall')
            mS.remove(1)
            mS.append(2)
            time.sleep(1.5)
            kryokammer(environment)
            
    elif cmd == 'skip':
        hauptzentrale(environment)
                
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
        time.sleep(1)
        terminal1(environment)
    elif cmd == '2':
        print('Ein Feld mit verschiedenen Auswahlmöglichkeiten ist auf dem Display zu sehen.')
        time.sleep(1)
        terminal2(environment)
    elif cmd == '3':
        print('Ein Feld mit verschiedenen Auswahlmöglichkeiten ist auf dem Display zu sehen.')
        time.sleep(1)
        terminal3(environment)
    elif cmd == '4':
        print('Du wendest dich den Terminals ab.')
        time.sleep(1)
        kryokammer(environment)


def terminal1(environment):
    time.sleep(0.5)
    print("\n(1) ''Information zu Gefangenem''")
    time.sleep(0.4)
    print("(2) ''Status''") 
    time.sleep(0.3)
    print("(3) ''Öffnen''")
    time.sleep(0.7)
    print("(4) Gehe zu anderem Terminal")
    time.sleep(0.1)
    print("(5) Beende Bedienung")
    time.sleep(0.6)
        
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
        
    if cmd == '1':
        time.sleep(1)
        print("''\nDatei wird aufgerufen...")
        time.sleep(2.1)
        print("...Gefangener 034629/348/23")
        time.sleep(0.8)
        print("...Name: Irc Zoek")
        time.sleep(1.2)
        print("...Verlegung des Straftäters nach Karion 4")
        time.sleep(0.1)
        print("...")
        time.sleep(0.4)
        print("...weitere Informationen sind nicht Verfügbar.\n''")
        time.sleep(0.5)
        terminal1(environment)
    elif cmd == '2':
        time.sleep(1)
        print("'' \nDatei wird aufgerufen...")
        time.sleep(1.7)
        print("...")
        time.sleep(0.8)
        print("Keine Lebenszeichen vorhanden, Subjekt Tod\n''")
        time.sleep(0.5)
        terminal1(environment)
    elif cmd == '3':
        time.sleep(1)
        print("'...")
        time.sleep(2.4)
        print("Das wäre wohl keine gute Idee, das lasse ich lieber bleiben'")
        time.sleep(0.5)
        terminal1(environment)
    elif cmd == '4':
        time.sleep(0.5)
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("Du wendest dich dem Rest des Raumes zu")
        time.sleep(0.5)
        kryokammer(environment)
        
def terminal2(environment):
    time.sleep(1.1)
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
        time.sleep(1.4)
        print("...Name: Izzin Quin")
        time.sleep(1.2)
        print("...Verlegung der Straftäterin nach Karion 4")
        time.sleep(0.5)
        print("...")
        time.sleep(0.2)
        print("...weitere Informationen sind nicht Verfügbar.\n''")
        time.sleep(0.5)
        terminal2(environment)
    elif cmd == '2':
        time.sleep(1.2)
        print("'' \nDatei wird aufgerufen...")
        time.sleep(2.3)
        print("...")
        time.sleep(0.3)
        print("...Kryokapsel manuell geöffnet...")
        time.sleep (0.7)
        print("...\n''")
        time.sleep(0.5)
        terminal2(environment)
    elif cmd == '3':
        time.sleep(1.5)
        print("''/n...")
        time.sleep(0.9)
        print("...Kapsel geöffnet")
        time.sleep(0.5)
        terminal2(environment)
    elif cmd == '4':
        time.sleep(0.5)
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("Du wendest dich dem Rest des Raumes zu")
        time.sleep(0.5)
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
        time.sleep(0.3)
        print("...Name: Narilyn Rezamo")
        time.sleep(0.2)
        print("...Verlegung des Straftäters nach Omega Zetha")
        time.sleep(0.2)
        print("...")
        time.sleep(0.2)
        print("...weitere Informationen sind nicht Verfügbar.\n''")
        time.sleep(0.5)
        terminal3(environment)
    elif cmd == '2':
        time.sleep(1.2)
        print("'' \nDatei wird aufgerufen...")
        time.sleep(2.3)
        print("...")
        time.sleep(0.3)
        print("...Kryokapsel manuell geöffnet...")
        time.sleep (0.7)
        print("...\n''")
        time.sleep(0.5)
        terminal3(environment)
    elif cmd == '3':
        time.sleep(1.5)
        print("''/n...")
        time.sleep(0.9)
        print("...Kapsel geöffnet")
        time.sleep(0.5)
        terminal3(environment)
    elif cmd == '4':
        time.sleep(0.5)
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("Du wendest dich dem Rest des Raumes zu")
        time.sleep(0.5)
        kryokammer(environment)
        
    
    
    
    
def flurSüd(environment):
    time.sleep(0.5)
    print("(1) Biege rechts ab")
    time.sleep(0.5)
    print("(2) Biege links ab")
    time.sleep(0.5)
    print("(3) Gehe zurück")
    
    cmdlist = ['1', '2', '3', 'umsehen',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print('Du entscheidest dich für den rechten Weg.')
        time.sleep(1.5)
        flurSüdRechts(environment)
    elif cmd == '2':
        time.sleep(0.5)
        print("Du entscheidest dich für den linken Weg")
        time.sleep(1.5)
        flurSüdLinks(environment)
    elif cmd == '3':
        time.sleep(0.5)
        print("Du gehst zurück")
        time.sleep(2)
        print("Du stehst vor der geschlossenen Tür zur Kryokammer.")
        time.sleep(1)
        print("(1) Öffne die Tür und betrete den Raum")
        time.sleep(0.5)
        print("(2) Gehe zurück")
        time.sleep(0.5)
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("Du öffnest die Tür und trittst herein.")
            time.sleep(1)
            print("In der Kryokammer ist alles wie zuvor.")
            time.sleep(1)
            kryokammer(environment)
        elif cmd == '2':
            time.sleep(0.5)
            print("Du gehst den Gang entlang und kommst an eine Abzweigung.")
            time.sleep(0.5)
            flurSüd(environment)
    
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Links und rechts führen zwei Gänge fort. Nach etwa")
        time.sleep(1.5)
        print("15 m biegen beide Wege in Richtung geradeaus.")
        time.sleep(1.5)
        flurSüd(environment)
        


def flurSüdRechts(environment):
    time.sleep(0.5)
    print("Du bewegst dich auf die Biegung nach links zu und schaust vorsichtig um die Ecke.")
    time.sleep(2)
    print("Ein leerer Gang führt zu einer Tür, links und rechts den Gang entlang befinden sich weitere Türen.")
    time.sleep(3)
    print("(1) Diesen Gang weiter gehen")
    time.sleep(0.5)
    print("(2) Die andere Abzweigung untersuchen")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'umsehen',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Als du langsam und leise den Weg entlang läufst, hörst du hinter dir ein Geräusch.")
        time.sleep(2)
        print("Du drehst dich um und siehst, das eine Art Notschleuse den Weg zurück zur Kryokammer schließt.")
        time.sleep(3)
        print("Du rennst zurück, doch der Weg ist schon versperrt.")
        time.sleep(1.5)
        print("Als du dich wieder umdrehst, stehen zwei Menschen im Gang, einer weiter hinten, einer fast direkt vor dir.")
        time.sleep(3.5)
        print("Du willst etwas sagen, da bemerkst du, dass der Mensch vor dir kaum menschlich aussieht.")
        time.sleep(2.5)
        print("Es streckt seine Arme nach dir aus.")
        time.sleep(1.5)
        print("(1) Angreifen")
        time.sleep(0.5)
        print("(2) Versuchen, mit dem Wesen zu reden")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', 'greife an', 'angreifen']
        cmd = getcmd(cmdlist)
        
        if cmd == '1' or cmd == 'greife an' or cmd == 'angreifen':
            time.sleep(0.5)
            kampf1FlurSüdRechts(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("Als du mit dem Wesen reden willst, greift es dich an.")
            mLP[0] = mLP[0] - 7
            time.sleep(0.5)
            kampf1FlurSüdRechts(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Du entscheidest dich doch lieber für den anderen Weg...")
        time.sleep(1.5)
        flurSüdLinks(environment)
        
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Als du dich etwas genauer umschaust, entdeckst du am Ende des Weges")
        print("eine Kamera. Sie scheint aktiv zu sein.")
        time.sleep(3)
        flurSüdRechts(environment)
        
        
def flurSüdRechtsGeschlossen(environment):
    time.sleep(0.5)
    print("Du befindest dich im Flur in der nähe der Kryokammer.")
    
    cmdlist = ['umsehen',
               'untersuche wesen',
               'untersuche leiche',
               'untersuche leichen',
               'untersuche gegner',
               'untersuche tür',
               'untersuche türen',
               'öffne tür',
               'öffne türen',
               'untersuche ausgang',
               'öffne ausgang',
               'untersuche kamera',
               'untersuche überwachungskamera',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich im Raum um.")
        time.sleep(1.5)
        print("Die zwei LEICHEN der seltsamen Wesen liegen auf dem Boden.")
        time.sleep(1.5)
        print("Eine ÜBERWACHUNGSKAMERA ist direkt auf dich gerichtet, sie hängt")
        print("über dem einzigen AUSGANG am Ende des Ganges. Sie scheint aktiv zu sein.")
        time.sleep(5)
        print("Zwei der vier TÜREN an den Seiten sind geöffnet, vermutlich kamen")
        print("aus diesen die Angreifer heraus.")
        time.sleep(3)
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'untersuche wesen' or cmd == 'untersuche leiche' or cmd == 'untersuche leichen' or cmd == 'untersuche gegner':
        print("Die zwei Leichen tragen die selben Overalls wie die Zwei in den")
        if mAus[0] == 'Gefangenenoverall':
            time.sleep(0.5)
            print("Kryokapseln und wie ich momentan.")
            time.sleep(1.5)
            print("Sie atmen nicht mehr und zeigen keine Spur von Leben.")
            time.sleep(1.5)
            print("Die Gesichter sind bleich, ihre Augen vollkommen rot.")
            time.sleep(1.5)
            print("Keiner der beiden hat etwas interessantes bei sich.")
            time.sleep(1.5)
            flurSüdRechtsGeschlossen(environment)
        else:
            time.sleep(0.5)
            print("Kryokapseln. Sie atmen nicht mehr und zeigen keine Spur von Leben.")
            time.sleep(2)
            print("Die Gesichter sind bleich, ihre Augen vollkommen rot.")
            time.sleep(1.5)
            print("Keiner der beiden hat etwas interessantes bei sich.")
            time.sleep(1.5)
            flurSüdRechtsGeschlossen(environment)
            
    elif cmd == 'untersuche tür' or cmd == 'untersuche türen':
        time.sleep(0.5)
        print("Die zwei verschlossenen Türen lassen sich nicht öffnen.")
        time.sleep(1.5)
        print("Hinter den zwei offenen Türen befinden sich spärlich eingerichtete Räume.")
        time.sleep(2)
        print("Der Raum ist ausgestattet mit einer Toilette, einem Wasserspender und einem harten Bett.")
        time.sleep(1.8)
        print("Mehr findest du nicht.")
        time.sleep(1)
        flurSüdRechtsGeschlossen(environment)
    
    elif cmd == 'öffne tür' or cmd == 'öffne türen':
        time.sleep(0.5)
        print("Zwei der Türen können nicht geöffnet werden.")
        time.sleep(1.5)
        print("Die anderen sind offen.")
        time.sleep(0.5)
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'untersuche kamera' or cmd == 'untersuche überwachungskamera':
        time.sleep(0.5)
        print("Du gehst zur Kamera.")
        time.sleep(1)
        print("Sie bleibt starr und du erkennst, dass sie abgeschaltet ist.")
        time.sleep(1.5)
        print("Die Kamera hängt zu hoch, um sie zu berühren.")
        time.sleep(1.5)
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'untersuche ausgang' or cmd == 'öffne ausgang':
        time.sleep(0.5)
        print("Als du dich direkt vor den Ausgang stellst, öffnet sich die Schleuse.")
        time.sleep(1.5)
        print("(1) Gehe hindurch")
        time.sleep(0.5)
        print("(2) Raum weiter untersuchen")
        time.sleep(0.5)
        
        cmdlist =['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("Du gehst in den Raum...")
            time.sleep(2)
            narrezGespräch(environment)
        
        elif cmd == '2':
            time.sleep(0.5)
            print("Du siehst dich noch etwas in dem Raum um.")
            time.sleep(1)
            print("Die Schleuse schließt sich wieder.")
            flurSüdRechtsGeschlossen(environment)
        
            

    
def flurSüdLinks(environment):
    time.sleep(0.5)
    print('Ein Gefühl sagt dir, der linke Weg wird der Richtige sein.')
    time.sleep(1.5)
    print("An der Biegung angekommen, nimmst du Geräusche von weiter weg war.")
    time.sleep(1.5)
    print("Du schaust vorsichtig um die Ecke...")
    time.sleep(1)
    print("Du erblickst den Rücken einer auf den Knien sitzenden Person.")
    time.sleep(1.5)
    print("Sie bewegt sich, vor ihr scheint etwas zu liegen, was sie beschäftigt.")
    time.sleep(2)
    print("(1) Zur Person gehen")
    time.sleep(0.5)
    print("(2) Den anderen Weg nehmen")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'umsehen']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du entscheidest dich dafür nachzuschauen, was da hinten los ist.")
        time.sleep(2)
        print("Bei der Person angekommen, schließt sich hinter dir eine Notschleuse.")
        time.sleep(2)
        print("Du drehst dich um und bist erstmal verwundert.")
        time.sleep(1.5)
        print("Als du dich wieder umdrehst, packt dich die Person, oder besser gesagt, das 'Etwas', an den Schultern...")
        time.sleep(3)
        print("Das ETWAS ist an Mund, Backen und Stirn mit Blut beschmiert.")
        time.sleep(1.5)
        print("Es reißt sein Maul auf und versucht dich zu beißen.")
        time.sleep(1.5)
        print("(1) Angreifen")
        time.sleep(0.5)
        print("(2) Dem Angreifer in einem vernünftigen Gespräch bitten, es zu unterlassen, dich auffressen zu wollen")
        time.sleep(3)
        
        cmdlist = ['1', '2', 'angreifen',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1' or cmd == 'angreifen':
            time.sleep(0.5)
            print("Du greifst an!")
            time.sleep(1.5)
            kampfFlurSüdLinks(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("Bevor du das Etwas mit deinen Argumenten angreifen kannst, beißt es dir ein Teil deiner Lippe ab.")
            mLippeAb.remove('Dran')
            mLippeAb.append('Abgebissen')
            mLP[0] = mLP[0] - 12
            time.sleep(3.5)
            kampfFlurSüdLinks(environment)
    
    elif cmd == '2':
        time.sleep(0.5)
        print("Du entscheidest dich doch lieber für den anderen Weg...")
        time.sleep(1.5)
        flurSüdRechts(environment)
    
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Als du dich etwas genauer umschaust, entdeckst du am Ende des Weges")
        print("eine Kamera. Sie scheint aktiv zu sein.")
        time.sleep(1.5)
        flurSüdLinks(environment)

def flurSüdLinksGeschlossen(environment):
    time.sleep(0.5)
    print("Du befindest dich im Flur.")    
    
    cmdlist = ['umsehen',
               'untersuche leiche',
               'untersuche etwas',
               'untersuche mann',
               'untersuche toten',
               'öffne ausgang',
               'öffne tür',
               'gehe zu tür',
               'gehe zu ausgang',
               'nehme Rohr'
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich im Raum um.")
        time.sleep(1)
        print("Es liegt die LEICHE des ETWAS vor die auf dem Boden.")
        time.sleep(1.5)
        print("In der Nähe der TÜR, die der einzige AUSGANG ist, nach dem")
        print("die Schleuse dir den anderen Weg versperrt, findest du einen TOTEN,")
        print("der wohl mal ein MANN war.")
        time.sleep(4)
        print("Sonst ist nichts weiter auffällig in diesem Flur.")
        time.sleep(1.5)
        flurSüdLinksGeschlossen(environment)
        
    elif cmd == 'untersuche leiche' or cmd == 'untersuche etwas':
        time.sleep(0.5)
        print("Das Gesicht des Etwas ist bleich und die Augen vollkommen rot.")
        time.sleep(1.5)
        print("Das Blut um sein Gesicht scheint wohl das des toten Mannes weiter hinten zu sein.")
        time.sleep(2.5)
        print("Es trägt einen Gefangenenoverall, sonst ist nicht auffälliges daran zu finden.")
        time.sleep(2.5)
        flurSüdLinksGeschlossen(environment)
    
    elif cmd == 'untersuche toten' or cmd == 'untersuche mann':
        time.sleep(0.5)
        print("Ein übel zugerichteter Mann liegt vor dir auf dem Boden.")
        time.sleep(1.5)
        print("Er normaler Mensch... der tot ist.")
        time.sleep(3)
        print("Du siehst, dass der Mann wohl ein ROHR zur Verteidigung genutzt hatte.")
        time.sleep(1.5)
        flurSüdLinksGeschlossen(environment)
        
    elif cmd == 'nehme rohr':
        if 'Rohr' in mAus or 'Rohr' in mG4:
            time.sleep(0.5)
            print("Rohr kaputt.")
            time.sleep(1)
            flurSüdLinksGeschlossen(environment)
        elif mW[0] != 'Faust':
            time.sleep(0.5)
            print("Rohr kaputt.")
            time.sleep(1)
            flurSüdLinksGeschlossen(environment)
        else:
            time.sleep(0.5)
            print("Du nimmst das Rohr.")
            time.sleep(1.5)
            print("Herzlichen Glückwunsch!!!")
            time.sleep(1.5)
            mW.remove('Faust')
            mW.append('Rohr')
            mHP.remove(3)
            mHP.append(7)
            print("Sie sind nun stolzer Besitzer eines Rohres!!!")
            time.sleep(3)
            flurSüdLinksGeschlossen(environment)
        
    elif cmd == 'öffne tür' or cmd == 'öffne ausgang' or cmd == 'gehe zu tür' or cmd == 'gehe zu ausgang':
        time.sleep(0.5)
        print("Als du dich direkt vor den Ausgang stellst, öffnet sich die Schleuse.")
        time.sleep(2)
        print("(1) Gehe hindurch")
        time.sleep(0.5)
        print("(2) Raum weiter untersuchen")
        time.sleep(0.5)
        
        cmdlist =['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("Du gehst in den Raum...")
            time.sleep(3)
            narrezGespräch(environment)
        
        elif cmd == '2':
            time.sleep(0.5)
            print("Du siehst dich noch etwas im Flur um.")
            time.sleep(1)
            print("Die Schleuse schließt sich wieder.")
            flurSüdLinksGeschlossen(environment)
        
def gefangenentraktZentrale(environment):
    
    
    cmdlist = ['umsehen', 
               'gehe zu mann', 
               'gehe zu narrez',
               'untersuche narrez',
               'untersuche mann',
               'rede mit mann' ,
               'rede mit narrez',
               'gehe zu schleuse', 
               'öffne schleuse', 
               'untersuche schleuse', 
               'untersuche fluchtkapsel',
               'gehe zu fluchtkapsel',
               'benutze fluchtkapsel',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        time.sleep(0.5)
        print("Du schaust dich im Raum um.")
        time.sleep(1.5)
        print("Viele verschlossene Schränke stehen auf der gegenüberliegenden Seite")
        print("des Rechners, vor dem der Mann steht und wütend auf die Tasten eines")
        print("Mischpultes tippt.")
        time.sleep(6)
        print("Eine FLUCHTKAPSEL ist neben dem Rechner zu sehen, allerdings scheint")
        print("sie momentan gesperrt zu sein.")
        time.sleep(3)
        print("Eine SCHLEUSE ist da, wo der Mann vorhin hingedeutet hatte.")
        time.sleep(1.5)
        gefangenentraktZentrale(environment)
        
    elif cmd == 'gehe zu narrez' or cmd == 'gehe zu mann' or cmd == 'untersuche mann' or cmd == 'untersuche narrez' or cmd == 'rede mit mann' or cmd == 'rede mit narrez' or cmd == 'untersuche fluchtkapsel' or cmd == 'gehe zu fluchtkapsel' or cmd == 'benutze fluchtkapsel':
        if iMMonsterLP[0] <= 0:
            time.sleep(0.5)
            print("Narrez dreht sich erwartungsvoll zu dir um")
            print("'Hast du dich um unser Problem gekümmert?'")
            time.sleep(0.5)
            print("Du antwortest ihm mit ja")
            time.sleep(0.5)
            print("'Sehr gut, dann musst du ja nur noch den Generator zum laufen bringen.")
            print(" Beeil dich mal lieber!'")
            time.sleep(0.5)
            print("Du wendest dich von ihm ab.")
            time.sleep(0.5)
            gefangenentraktZentrale(environment)
        elif mMonsterGesehen[0] != 'Ja':
            time.sleep(0.5)
            print("'Was suchst du hier noch!")
            time.sleep(1)
            print(" Geh runter und reparier den Generator!!")
            time.sleep(1.5)
            print(" Oder soll ich dir Beine machen!!!'")
            time.sleep(1.5)
            gefangenentraktZentrale(environment)
        elif mMonsterGesehen[0] == 'Ja':
            time.sleep(0.5)
            print("Du gehst zu Narrez und sagst ihm, dass dort unten ein riesiges Monster lungert,")
            print("und es Unmöglich ist, ohne die richtige Ausrüstung da rein zu marschieren.")
            time.sleep(5)
            print("Er schaut dich aggresiv und genervt an.")
            print("'Dann geh nach oben zur Waffenkammer und hol dir etwas, was das Ding weg fegt!'")
            time.sleep(5)
            print("Er dreht sich um und schaut wieder die Monitore an.")
            time.sleep(2)
            gefangenentraktZentrale(environment)
        
            
    elif cmd == 'gehe zu schleuse' or cmd == 'öffne schleuse' or cmd == 'untersuche schleuse' or cmd == 'gehe zu ausgang' or  cmd == 'öffne ausgang' or  cmd == 'untersuche ausgang':
        time.sleep(0.5)
        print("Du bewegst dich in Richtung Schleuse.")
        time.sleep(1.5)
        print("Die Schleuse öffnet sich und du gehst hindurch.")
        time.sleep(1.5)
        print("Du bist in einem Treppenhaus.")
        time.sleep(1)
        print("Auf einer Karte an der Wand siehst du, das über dir")
        print("die Mannschaftsquartiere sein müssten und unter dir ")
        print("der Maschinenraum.")
        time.sleep(4)
        print("Ein Weg führt nach oben, der andere nach unten.")
        time.sleep(1.5)
        treppenhausGZ(environment)
        
        
def treppenhausGZ(environment):
    time.sleep(0.5)
    print("Momentane Position: Treppenhaus")
    time.sleep(0.5)
    print("(1) Gehe zum Maschinenraum")
    time.sleep(0.5)
    print("(2) Gehe zu den Mannschaftsquartieren")
    time.sleep(0.5)
    print("(3) Gehe zum Gefangenentrakt")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', '3', 'umsehen',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst in Richtung Maschinenraum.")
        time.sleep(1.5)
        maschinenraumFlur(environment)
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst zu den Mannschaftsquartieren.")
        time.sleep(1.5)
        mannschaftsquartiereFlur(environment)
    elif cmd == '3':
        if iGenerator[0] == 'An' and iNarrezMerana[0] != 'Wissend':
            endeKeineFluchtkapsel(environment)
        if iGenerator[0] == 'An' and iBewFrau[0] != 'Traurig':
            endeKeineFluchtkapsel(environment)
        elif iBewFrau[0] == 'Traurig' or iNarrezMerana[0] == 'Wissend':
            time.sleep(0.5)
            print("Du gehst zum Gefangenentrakt.")
            time.sleep(1.5)
            gefangenentraktZentraleKeinNarrezMehr(environment)
        else:
            time.sleep(0.5)
            print("Du gehst zum Gefangenentrakt.")
            time.sleep(1.5)
            gefangenentraktZentrale(environment)
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich ein wenig um.")
        time.sleep(1.5)
        print("Es scheint nichts besonderes in diesem Raum zu geben.")
        time.sleep(2)
        treppenhausGZ(environment)
    
def maschinenraumFlur(environment):
    time.sleep(0.5)
    print("Momentane Position: Maschinenraumflur")
    time.sleep(0.5)
    print("(1) gehe Richtung Maschinenraum")
    time.sleep(0.5)
    print("(2) gehe Richtung Gefangenentrakt")
    time.sleep(0.5)
    print("( ) sonstige Befehle")
    time.sleep(0.5)
    
    cmdlist = ['1', '2','untersuche schränke', 'öffne jonas schrank', 'öffne hannahs schrank','umsehen',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst in Richtung Maschinenraum")
        time.sleep(1.5)
        maschinenraum(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst in Richtung Gefangenentrakt")
        time.sleep(1.5)
        treppenhausGZ(environment)
        
    elif cmd == 'untersuche schränke':
        time.sleep(0.5)
        print("-Welchen der beiden Schränke möchtest du ÖFFNEN?-")
        time.sleep(2)
        print("-JONAS SCHRANK oder HANNAHS SCHRANK?-")
        time.sleep(1.5)
        maschinenraumFlur(environment)
        
    elif cmd == 'öffne jonas schrank':
        if iTürHPasswort[0] != 'Izzin':
            time.sleep(0.5)
            print("Du findest einen Zettel auf dem folgendes steht:")
            print("Passwort: Izzin")
            iTürHPasswort.remove('Unbekannt')
            iTürHPasswort.append('Izzin')
            time.sleep(1.5)
            maschinenraumFlur(environment) 
        else:
            time.sleep(0.5)
            print("Du findest ein Zettel auf dem folgendes steht:")
            print("Passwort: Izzin")
            time.sleep(1.5)
            maschinenraumFlur(environment)
     
    elif cmd == 'öffne hannahs schrank':
        if 'Technikeroverall' in mAus or 'Technikeroverall' in mG3:
            time.sleep(0.5)
            print("Der Schrank ist leer.")
            time.sleep(1.5)
            maschinenraumFlur(environment)  
        elif mAus[0] != 'Unterhose':
            time.sleep(0.5)
            print("Du öffnest den Schrank und darin befindet sich eine Technikeroverall.")
            time.sleep(2)
            print("Du hast jedoch schon Kleidung an und kannst den Overall nicht anziehen.")
            time.sleep(2.5)
            print("ziehe deine Kleidung aus, bevor du etwas neues anziehst.")
            time.sleep(2)
            maschinenraumFlur(environment)
        else:    
            time.sleep(0.5)
            print("Du öffnest den Schrank und darin befindet sich eine Technikeroverall.")
            time.sleep(2)
            print("(1) Ziehe Technikeroverall an")
            time.sleep(1.5)
            print("(2) Technikeroverall liegen lassen")
            time.sleep(1.5)
        
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("Du ziehst den Overall an.")
                time.sleep(1.5)
                print("Etwas eng, aber er passt und ist bequem.")
                mAus.remove('Unterhose')
                mAus.append('Technikeroverall')
                mS.remove(1)
                mS.append(4)
                time.sleep(2)
                maschinenraumFlur(environment)      
                
            elif cmd == '2':
                time.sleep(0.5)
                print("Du lässt den Overall lieber liegen.") 
                time.sleep(1)
                maschinenraumFlur(environment)
        
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich um.")
        time.sleep(1.5)
        print("Du stehst in einem dunklen, langen Flur.")
        time.sleep(1.5)
        print("Über dir gehen verschiedene Rohre in alle Richtungen, der Boden")
        print("fühlt sich kalt und hart an, die Luft ist stickig und du riechst")
        print("Verschmutzung in der Luft.")
        time.sleep(6)
        print("Als du den Weg entlang läufst, bemerkst du vor dir etwas großes")
        print("Auf dem Boden liegen.")
        time.sleep(3)
        print("Du gehst näher heran.")
        time.sleep(1.5)
        print("...")
        time.sleep(1)
        print("Ein kalter Schauer geht dir den Rücken runter...")
        time.sleep(1.5)
        print("Vor dir liegt ein Leichenhaufen.")
        time.sleep(1.5)
        print("Mindestens 10 Frauen und Männer in Technikeroveralls liegen tot")
        print("vor dir.")
        time.sleep(3)
        print("Zwei SCHRÄNKE sind in der nähe der nächsten Tür.")
        time.sleep(1.5)
        print("Auf dem einen steht JONAS SCHRANK, auf dem anderen HANNAHS SCHRANK.")
        time.sleep(1.5)
        maschinenraumFlur(environment)
        
def maschinenraum(environment):
    if iMMonsterLP[0] >= 0 and mMonsterGesehen[0] == 'Ja':
        mMonsterGesehen.remove('Ja')
        mMonsterGesehen.append('Nein')
        time.sleep(0.5)
        print("Die Tür zum Maschinenraum ist schwer und quitscht beim Öffnen.")
        time.sleep(1.5)
        print("Die Tür schließt sich hinter dir, im selben Moment schaltet sich das Licht an.")
        time.sleep(3)
        print("Das Monster hat schon auf dich gewartet und greif wieder an.")
        time.sleep(2)
        mMonsterGesehen.remove('Nein')
        mMonsterGesehen.append('Ja')
        kampfMMonster(environment)
    elif iMMonsterLP[0] >= 0:
        time.sleep(0.5)
        print("Die Tür zum Maschinenraum ist schwer und quitscht beim Öffnen.")
        time.sleep(1.5)
        print("Die Tür schließt sich hinter dir, im selben Moment schaltet sich das Licht an.")
        time.sleep(3)
        print("Du glaubst deinen Augen nicht!")
        time.sleep(1.5)
        print("Ein riesiges Monster sitzt neben der Tür zum Generatorraum und beobachtet dich.")
        time.sleep(2)
        print("Mit seinen roten, toten Augen verfolgt es dich und geht schließlich auf dich los.")
        time.sleep(4)
        time.sleep(2)
        mMonsterGesehen.remove('Nein')
        mMonsterGesehen.append('Ja')
        kampfMMonster(environment)
    else:
        time.sleep(0.5)
        print("Momentane Position: Maschinenraum")
        time.sleep(0.5)
        print("(1) Gehe Richtung Gefangenentrakt")
        time.sleep(0.5)
        print("( ) Sonstiges")
        time.sleep(0.5)
    
        cmdlist = ['1', 'umsehen', 'gehe zu generatorraum',]
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            time.sleep(0.5)
            print("Du gehst in Richtung Gefangenentrakt")
            time.sleep(1.5)
            maschinenraumFlur(environment)
        
        elif cmd == 'umsehen':
            time.sleep(0.5)
            print("Du siehst dich ein wenig um.")
            print("An einer Tür steht groß GENERATORRAUM.")
            print("Der Kadaver des Monsters liegt in der Mitte des Raumes, sein Gestank verpestet")
            print("die Luft.")
            print("Ansonsten siehst du große Maschinen, Schalter, Räder und Terminals.")
            time.sleep(1.5)
            maschinenraum(environment)
        
        elif cmd == 'gehe zu generatorraum':
            time.sleep(0.5)
            print("Du öffnest die Tür zum Generatorraum und trittst ein.")
            generatorraum(environment)
            
def generatorraum(environment):
    time.sleep(0.5)
    print("Momentane Position: Generatorraum")
    time.sleep(0.5)
    print("(1) Gehe Richtung Gefangenentrakt")
    time.sleep(0.5)
    print("( ) sonstige Befehle")
    time.sleep(0.5)
    
    cmdlist = ['1', 'umsehen', 'benutze generator', 'untersuche generator', 'untersuche luke']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("Du gehst in Richtung Gefangenentrakt.")
        maschinenraum(environment)
        
    elif cmd == 'umsehen':
        print("Du siehst dich ein wenig um.")
        print("Viele Generatoren sorgen für die Energieversorung des Raumschiffes.")
        if iGenerator[0] == 'Aus':
            print("Einige sind ausgefallen, darunter auch der Generator 4FK, von dem Narrez")
            print("gesprochen hatte.")
            generatorraum(environment)
        else:
            print("Einige sind ausgefallen, jedoch hast du den Generator 4FK neu gestartet.")
            generatorraum(environment)
            
    elif cmd == 'untersuche generator' or cmd == 'benutze generator':
        print("Du gehst zu dem Generator 4FK")
        print("(1) Generator einschalten")
        print("(2) Generator ausschalten")
        print("(3) Generator so lassen und wegtreten")
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            if iGenerator[0] == 'Aus':
                print("Du drückst auf einen Knopf und plötzlich springt der Generator wieder an.")
                iGenerator.remove('Aus')
                iGenerator.append('An')
                generatorraum(environment)
            else:
                print("Generatot aktiviert.")
                generatorraum(environment)
                
        elif cmd == '2':
            if iGenerator[0] == 'An':
                print("Du drückst auf einen Knopf und der Generator hört auf zu laufen.")
                iGenerator.remove('An')
                iGenerator.append('Aus')
                generatorraum(environment)
            else:
                print("Generator deaktiviert.")
                generatorraum(environment)
                
        elif cmd == '3':
            print("'Das lasse ich lieber bleiben'")
            generatorraum(environment)
            
    elif cmd == 'untersuche luke':
        print("Die Luke ist von dieser Seite aus nicht zu öffnen.")
        generatorraum(environment)
            
    
    

def mannschaftsquartiereFlur(environment):
    time.sleep(0.5)
    print("Du bist im Flur der Mannschaftsquartiere.")
    iRotAuge1Luck.append(randint(1,2))
    if iRotAuge1LP[0] >= 0 and mLuck[0] in iRotAuge1Luck:
        time.sleep(0.5)
        print("Ein Rotäugiger greift dich an!")
        iRotAuge1Luck.remove(1)
        time.sleep(1)
        kampfRotAuge1(environment)
    elif mLuck[0] in iRotAuge1Luck:
        iRotAuge1Luck.remove(1)
        time.sleep(0.5)
        print("An einer Wand siehst du einen Geländeplan für dieses Stockwerk.")
        print("Weiter gerade aus führt ein weiteres Treppenhaus weiter nach oben zur")
        print("Hauptzentrale.")
        time.sleep(5)
        mannschaftsquartiereFlur1(environment)
    else:
        time.sleep(0.5)
        iRotAuge1Luck.remove(2)
        print("An einer Wand siehst du einen Geländeplan für dieses Stockwerk.")
        print("Weiter gerade aus führt ein weiteres Treppenhaus weiter nach oben zur")
        print("Hauptzentrale.")
        time.sleep(5)
        mannschaftsquartiereFlur1(environment)

def mannschaftsquartiereFlur1(environment):
    time.sleep(0.5)
    print("Momentane Position: Flur der Mannschaftsquartiere")
    time.sleep(0.5)
    print("(1) gehe Richtung Hauptzentrale")
    time.sleep(0.5)
    print("(2) gehe zum Gefangenentrakt")
    time.sleep(0.5)
    print("( ) sonstige Befehle")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'umsehen', 'untersuche wasserspender', 'benutze wasserspender']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst weiter in Richtung Hauptzentrale.")
        time.sleep(0.5)
        print("Du schlenderst den Flur weiter entlang und gehst durch die Tür, die  dich in den nächsten Raum führt.")
        time.sleep(2)
        print("Ein betrittst einen weiteren Flur, 2 geschlossene Türen rechts und 2 links sind in diesem Flur.")
        time.sleep(0.5)
        print("Auf den Türen sind folgende Buchstaben eingraviert: A, B, C, D")
        time.sleep(0.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst zurück ins Treppenhaus.")
        time.sleep(0.5)
        treppenhausGZ(environment)
    
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich um, entdeckst aber nichts interessantes außer den Weg")
        print("zurück zum Treppenhaus, der Tür, die dich weiter Richtung Hauptzentrale")
        print("bringt und einen Wasserspender.")
        time.sleep(0.5)
        mannschaftsquartiereFlur1(environment)
        
    elif cmd == 'untersuche wasserspender':
        time.sleep(0.5)
        print("Als du dich dem Wasserspender näherst, kommt ein schöner Strahl Wasser heraus.")
        time.sleep(1.5)
        print("Du bist etwas beunruhigt, da die Farbe des Wassers einen roten Unterton hat.")
        time.sleep(1.5)
        mannschaftsquartiereFlur1(environment)
        
    elif cmd == 'benutze wasserspender':
        time.sleep(0.5)
        print("Du trinkst das Wasser des Spenders.")
        time.sleep(2)
        print("Etwas an diesem Wasser schmeckt seltsam...")
        time.sleep(2.5)
        print("Du fühlst dich seltsam benommen und deine Augen beginnen zu jucken...")
        time.sleep(3)
        print("Du verlierst die Kontrolle über deinen Körper und dir wird schwarz vor Augen...")
        time.sleep(3.5)
        exit()
        
def mannschaftsquartiereFlur2(environment):
    time.sleep(0.5)
    print("Momentane Position: Flur der Mannschaftsquartiere")
    time.sleep(0.5)
    print("(1) gehe Richtung Hauptzentrale")
    time.sleep(0.5)
    print("(2) gehe Richtung Gefangenentrakt")
    time.sleep(0.5)
    print("() sonstige Befehle")
    time.sleep(0.5)
    
    cmdlist = ['1', 
               '2', 
               'umsehen', 
               'öffne tür a', 
               'öffne tür b', 
               'öffne tür c', 
               'öffne tür d', 
               'untersuche wasserspender', 
               'benutze wasserspender'
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst weiter in Richtung Hauptzentrale")
        time.sleep(1.5)
        print("Du gehst den Flur weiter entlang und gehst durch die nächste Tür in den nächsten Raum.")
        iRotAuge2Luck.append(randint(1,2))
        if iRotAuge2LP[0] >= 0 and mLuck[0] in iRotAuge2Luck:
            time.sleep(0.5)
            print("Ein Rotäugiger greift dich an!")
            iRotAuge2Luck.remove(1)
            time.sleep(1.5)
            kampfRotAuge2(environment)
        elif mLuck[0] in iRotAuge2Luck:
            iRotAuge2Luck.remove(1)
            time.sleep(0.5)
            print("Ein weiterer Flur, 2 geschlossene Türen rechts und 2 links.")
            time.sleep(2)
            print("Auf den Türen sind Buchstaben eingraviert: E, F, G, H.")
            time.sleep(2)
            mannschaftsquartiereFlur3(environment)
        else:
            iRotAuge2Luck.remove(2)
            time.sleep(0.5)
            print("Ein weiterer Flur, 2 geschlossene Türen rechts und 2 links.")
            time.sleep(2)
            print("Auf den Türen sind Buchstaben eingraviert: E, F, G, H.")
            time.sleep(2)
            mannschaftsquartiereFlur3(environment)
            
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst in Richtung Gefangenentrakt")
        time.sleep(1)
        print("Du gehst den Flur entlang und gehst durch die Tür in den nächsten Raum.")
        time.sleep(2)
        print("Es befinden nur zwei Türen in diesem Raum.")
        time.sleep(2)
        mannschaftsquartiereFlur1(environment)
    
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst folgende Türen:")
        time.sleep(1)
        print("TÜR A")
        time.sleep(0.5)
        print("TÜR B")
        time.sleep(0.5)
        print("TÜR C")
        time.sleep(0.5)
        print("TÜR D")
        time.sleep(0.5)
        print("Wie wäre es, wenn du versuchen würdest eine davon zu ÖFFNEN?")
        time.sleep(0.5)
        print("Außerdem siehst du einen WASSERSPENDER.")
        time.sleep(2)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'öffne tür a':
        time.sleep(0.5)
        print("Diese Tür ist verschlossen.")
        time.sleep(0.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'öffne tür b':
        time.sleep(0.5)
        print("Diese Tür lässt sich öffnen.")
        time.sleep(0.5)
        if medikit1[0] == 'Unbenutzt':
            time.sleep(0.5)
            print("Du findest ein Medikit und benutzt es, um deine Wunden zu versorgen.")
            time.sleep(3)
            mLP[0] = mLP[0] + 30
            medikit1.remove('Unbenutzt')
            medikit1.append('Benutzt')
            print("Mehr findest du nicht.")
            time.sleep(1)
            mannschaftsquartiereFlur2(environment)
        else:
            time.sleep(0.5)
            print("Hier war mal ein Medikit drin...")
            time.sleep(0.5)
            print("Welch schöne Zeiten das doch waren...")
            time.sleep(0.5)
            mannschaftsquartiereFlur2(environment)
    
    elif cmd == 'öffne tür c':
        if iKleineRüstung[0] == 'Besitz':
            print("Diesen Raum hast du schon durchsucht und die Kleidung mitgenommen.")
            mannschaftsquartiereFlur2(environment)
        elif iKleineRüstung[0] == 'Dame':
            print("Diesen Raum hast du schon durchsucht und die Kleidung mitgenommen.")
            mannschaftsquartiereFlur2(environment)
        else:
            time.sleep(0.5)
            print("Diese Tür lässt sich öffnen.")
            time.sleep(1)
            print("Auf einem Bett liegt Kleidung, die guten Schutz bieten würde,")
            print("Jedoch bist du zu groß, um diese anzuziehen.")
            print("(1) Kleidung mitnehmen und Raum verlassen")
            print("(2) Kleidung liegen lassen und Raum verlassen")
            
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("Du nimmst die Kleidung vorsichtshalber mit.")
                iKleineRüstung.remove('Raum')
                iKleineRüstung.append('Besitz')
                time.sleep(0.5)
                print("Du verlässt den Raum.")
                mannschaftsquartiereFlur2(environment)
                
            elif cmd == '2':
                time.sleep(0.5)
                print("Du lässt sie lieber liegen.")
                print("Du verlässt den Raum.")
                mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'öffne tür d':
        time.sleep(0.5)
        print("Diese Tür ist verschlossen.")
        time.sleep(1.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'untersuche wasserspender':
        time.sleep(0.5)
        print("Als du dich dem Wasserspender näherst, kommt ein schöner Strahl Wasser heraus.")
        time.sleep(1.5)
        print("Du bist etwas beunruhigt, da die Farbe des Wassers einen roten Unterton hat.")
        time.sleep(1.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'benutze wasserspender':
        time.sleep(0.5)
        print("Du trinkst das Wasser des Spenders.")
        time.sleep(2)
        print("Etwas an diesem Wasser schmeckt seltsam...")
        time.sleep(2.5)
        print("Du fühlst dich seltsam benommen und deine Augen beginnen zu jucken...")
        time.sleep(3)
        print("Du verlierst die Kontrolle über deinen Körper und dir wird schwarz vor Augen...")
        time.sleep(3.5)
        exit()
        
def mannschaftsquartiereFlur3(environment):
    time.sleep(0.5)
    print("Momentane Position: Flur der Mannschaftsquartiere")
    time.sleep(0.5)
    print("(1) gehe Richtung Hauptzentrale")
    time.sleep(0.5)
    print("(2) gehe Richtung Gefangenentrakt")
    time.sleep(0.5)
    print("() sonstige Befehle")
    time.sleep(0.5)
    
    cmdlist = ['1', 
               '2', 
               'umsehen', 
               'öffne tür e', 
               'öffne tür f', 
               'öffne tür g', 
               'öffne tür h', 
               'untersuche wasserspender', 
               'benutze wasserspender'
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst weiter in Richtung Hauptzentrale.")
        time.sleep(1.5)
        print("Die nächste Tür bringt dich in ein Treppenhaus.")
        time.sleep(1.5)
        print("Auf einem Gebäudeplan an der Wand siehst du, dass es weiter nach oben")
        print("zur Hauptzentrale geht.")
        time.sleep(3)
        treppenhausHZ(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst in Richtung Gefangenentrakt.")
        time.sleep(1)
        print("Du gehst den Flur entlang und gehst durch die Tür in den nächsten Raum.")
        time.sleep(3)
        print("Du befindest dich in den Raum mit den Türen A, B, C, D")
        time.sleep(2.5)
        mannschaftsquartiereFlur2(environment)
    
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst folgende Türen:")
        time.sleep(0.5)
        print("TÜR E")
        time.sleep(0.5)
        print("TÜR F")
        time.sleep(0.5)
        print("TÜR G")
        time.sleep(0.5)
        print("TÜR H")
        time.sleep(0.5)
        print("Wie wäre es, wenn du versuchen würdest eine davon zu ÖFFNEN?")
        time.sleep(0.5)
        print("An einer Wand ist außerdem ein WASSERSPENDER angebracht.")
        time.sleep(2.5)
        mannschaftsquartiereFlur3(environment)
        
    elif cmd == 'öffne tür e':
        time.sleep(0.5)
        print("Diese Tür lässt sich öffnen.")
        time.sleep(1.5)
        print("Du hörst ein Knacksen...")
        time.sleep(1.5)
        iRotAuge3Luck.append(randint(1,2))
        if iRotAuge3LP[0] >= 0 and mLuck[0] in iRotAuge3Luck:
            time.sleep(0.5)
            print("...und ein Rotäugiger greift dich an!")
            iRotAuge3Luck.remove(1)
            time.sleep(2.5)
            kampfRotAuge3(environment)
        elif mLuck[0] in iRotAuge3Luck:
            iRotAuge3Luck.remove(1)
            time.sleep(0.5)
            if mStoffKuscheltier[0] == 'Meins':
                time.sleep(1)
                print("Das musst du dir wohl eingebildet haben...")
                time.sleep(1.5)
                print("In dem Raum befinden sich die Unterkünfte von 6 Leuten.")
                time.sleep(1.5)
                print("Und niemand hat etwas nützliches hier gelassen...")
                print("Du verlässt den Raum")
                time.sleep(2.5)
                mannschaftsquartiereFlur3(environment)
            else:
                time.sleep(1)
                print("Du gehst in den Raum und siehst das blutverschmierte Stoffebenbild eines Affen.")
                time.sleep(3)
                print("Du kannst nicht anders und nimmst ihn in deine Arme.")
                mStoffKuscheltier.remove('Rotauge')
                mStoffKuscheltier.append('Meins')
                time.sleep(2)
                print("Du verlässt den Raum.")
                time.sleep(1)
                mannschaftsquartiereFlur3(environment)
        else:
            iRotAuge3Luck.remove(2)
            time.sleep(1)
            print("Das musst du dir wohl eingebildet haben...")
            time.sleep(1.5)
            print("In dem Raum befinden sich die Unterkünfte von 6 Leuten.")
            time.sleep(2)
            print("Und niemand hat etwas nützliches hier gelassen...")
            print("Du verlässt den Raum.")
            time.sleep(3)
            mannschaftsquartiereFlur3(environment)    
        
    elif cmd == 'öffne tür f':
        time.sleep(0.5)
        print("Diese Tür ist verschlossen.")
        time.sleep(1.5)
        mannschaftsquartiereFlur3(environment)
    
    elif cmd == 'öffne tür g':
        time.sleep(0.5)
        print("Diese Tür ist verschlossen.")
        time.sleep(1.5)
        mannschaftsquartiereFlur3(environment)
    
    elif cmd == 'öffne tür h':
        time.sleep(0.5)
        if iTürHPasswort[0] != 'Izzin':
            print("Diese Tür lässt sich nicht öffnen.")
            print("Du siehst, dass die Türsteuerung Passwort geschützt ist.")
            print("Wenn du doch nur das Passwort wüsstest...")
            mannschaftsquartiereFlur3(environment)
        else:
            print("Diese Tür lässt sich nicht öffnen.")
            print("Du siehst, dass die Türsteuerung Passwort geschützt ist.")
            print("Dir fällt die Notiz im Maschinendeck wieder ein.")
            print("''Izzin''")
            print("PING")
            print("...")
            print("Die Tür geht auf und du gehst herein.")
            raumH(environment)
            
    elif cmd == 'untersuche wasserspender':
        time.sleep(0.5)
        print("Als du dich dem Wasserspender näherst, kommt ein schöner Strahl Wasser heraus.")
        time.sleep(1.5)
        print("Du bist etwas beunruhigt, da die Farbe des Wassers einen roten Unterton hat.")
        time.sleep(1.5)
        mannschaftsquartiereFlur3(environment)
        
    elif cmd == 'benutze wasserspender':
        time.sleep(0.5)
        print("Du trinkst das Wasser des Spenders.")
        time.sleep(2)
        print("Etwas an diesem Wasser schmeckt seltsam...")
        time.sleep(2.5)
        print("Du fühlst dich seltsam benommen und deine Augen beginnen zu jucken...")
        time.sleep(3)
        print("Du verlierst die Kontrolle über deinen Körper und dir wird schwarz vor Augen...")
        time.sleep(3.5)
        exit()
            
def raumH(environment):
    print("Du befindest dich in Raum H.")
    print("(1) Hinaus gehen")
    print("( ) sonstige Befehle")
    
    cmdlist = ['1', 
               'umsehen', 
               'öffne schrank', 
               'öffne schränke', 
               'untersuche bett', 
               'untersuche betten', 
               'öffne arzneischrank',
               'untersuche kisten',
               'untersuche kiste',
               'untersuche nachttisch',
               'untersuche nachttische']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("Du gehst aus den Raum.")
        mannschaftsquartiereFlur3(environment)
    
    elif cmd == 'umsehen':
        print("Du siehst dich im Raum etwas um.")
        print("In dem Raum befindet sich:")
        print("Vier SCHRÄNKE,")
        print("einige KISTEN,")
        print("Mehrere BETTEN,")
        print("ein ARZNEISCHRANK")
        print("und NACHTTISCHE")
        raumH(environment)
        
    elif cmd == 'öffne schrank' or cmd == 'öffne schränke':
        if 'Jonas Laserkanone' in mAus or 'Jonas Laserkanone' in mG2:
            time.sleep(0.5)
            print("Der Schrank ist leer.")
            time.sleep(1)
            raumH(environment) 
        elif mW[0] != 'Faust':
            time.sleep(0.5)
            print("Du öffnest den Schrank und darin befindet sich eine Laserkanone.")
            time.sleep(2)
            print("Jedoch hast du schon eine Waffe in der Hand.")
            time.sleep(1.5)
            print("Lege die Waffe ab, um eine neue auszurüsten.")
            time.sleep(1.5)
            raumH(environment)
        else:    
            time.sleep(0.5)
            print("Du öffnest den Schrank und darin befindet sich eine Laserkanone.")
            time.sleep(2)
            print("(1) Nehme Jonas Laserkanone")
            time.sleep(1.5)
            print("(2) Jonas Laserkanone liegen lassen")
            time.sleep(1.5)
        
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("Du nimmst dir Jonas Laserkanone.")
                time.sleep(1.5)
                print("Danke Jonas")
                mW.remove('Faust')
                mW.append('Jonas Laserkanone')
                mHP.remove(3)
                mHP.append(10)
                time.sleep(1.5)
                raumH(environment)
            
            elif cmd == '2':
                time.sleep(0.5)
                print("Du lässt die Laserkanone lieber liegen.") 
                time.sleep(1)
                raumH(environment)
        
    elif cmd == 'untersuche bett' or cmd == 'untersuche betten':
        time.sleep(0.5)
        print("Du untersuchst die Betten.")
        time.sleep(1)
        print("Als du ein Kopfkissen hoch nimmst, entdedckst du eine Notiz.")
        time.sleep(0.5)
        print("(1) Notiz lesen")
        time.sleep(0.5)
        print("(2) Notiz zurücklegen")
        time.sleep(0.5)
                
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("Du entscheidest dich, die Notiz zu lesen.")
            time.sleep(1.5)
            print("\n'Aufzeichnungen vom 13.05.49201")
            print(" ")
            print(" Mex und ich sind so gut wie ohne Probleme auf das Schiff gekommen. Das größte")
            print(" Problem der ganzen Unternehmung ist also hinter uns gebracht. Jetzt müssen wir")
            print(" Nur noch Izzin finden, für Chaos sorgen und von diesem Schiff entkommen. Alles")
            print(" ist geplant und der Plan ist idiotensicher.")
            print(" ")
            print(" ")
            print(" Aufzeichnungen vom 11.06.49201")
            print(" ")
            print(" Zum Glück habe ich Mex dabei! Seit fast einem Monat versuche ich es, in den")
            print(" Gefangenentrakt zu wechseln, aber kaum zu glauben, wie viele Schiffstechniker")
            print(" vom Maschinenraum versetzt werden wollen. Wegen diesem riesigen Viech dort")
            print(" unten bleibe ich nicht nur hier, ich wurde sogar befördert, weil sich, außer mir,") 
            print(" niemand an das Ding rantraut! Ich bin jetzt im komfortabelsten Mannschaftsquartier")
            print(" untergekommen, und habe dort einen Schrank, in dem ich endlich meine Lizzy verstecken")
            print(" kann. Mex hingegen hat sich so blöd dort unten angestellt, der wurde in den")
            print(" Gefangenenetrakt verlegt. Jetzt kann er sich dort umsehen und Bericht erstatten.")
            print(" Wenn wir hier draußen sind, werde ich ihn dir vorstellen, er ist wirklich ein sehr")
            print(" netter Mensch.")
            print(" ")
            print(" Aufzeichnungen vom 19.06.49201")
            print(" ")
            print(" Heute ist es so weit.")
            print(" Nach dem Frühstück werden wir mit der Operation anfangen. Ich werde für Verwirrung")
            print(" im Maschinenraum sorgen, in dem ich ein paar Stecker im Generatorraum ziehe und die")
            print(" Stromversorgung lahm lege. Um mir Zeit dafür Zeit zu verschaffen, werde ich das Viech")
            print(" im Maschienenraum freilassen. Es ist zwar riskant, aber ich werde schon irgendwie da")
            print(" wieder raus kommen. Mex wird diese rote Substanz in die Wasserversorgung kippen, die ich")
            print(" von diesem komischen Kauz auf Vega 7 ergaunert habe. Das wird die Crew für einige Zeit")
            print(" lahm legen. Wenn die Stromversorgung dann gekappt ist, wird Mex im Gefangenentrakt deine")
            print(" Kryokammer öffnen und dich da raus holen. Ich habe ihm gesagt, er soll noch eine weitere")
            print(" öffnen, damit das Verschwinden von Izzin nicht all zu auffällig aussieht. Wie schon gesagt,")
            print(" der Plan ist idiotensicher! Bald werden wir wieder vereint sein meine Izzin. Wir werden dann")
            print(" mit der Fluchtkapsel im Gefangenentrakt verschwinden, sobald die AStromversorgung wieder")
            print(" hergestellt ist.")
            print(" Die Lichter gehen an.")
            print(" Ich muss los.'")
            print(" ")
            time.sleep(10)
            print("Nachdem du die Notiz gelesen hast, legst du sie wieder zurück.")
            time.sleep(0.5)
            raumH(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("Du legst die Notiz wieder zurück.")
            time.sleep(0.5)
            raumH(environment)
        
    elif cmd == 'öffne arzneischrank':
        time.sleep(0.5)
        if iKleineRüstung[0] == 'Dame':
            if 'Monsterhunter' in mAus or 'Monsterhunter' in mG6:
                time.sleep(0.5)
                print("Der Schrank ist leer.")
                time.sleep(1)
                raumH(environment) 
            elif mW[0] != 'Faust':
                time.sleep(0.5)
                print("Du öffnest den Arzneischrank und darin befindet sich eine riesige Wumme.")
                print("Es steht 'Monsterhunter' auf der überdimsensionalen Knarre.")
                time.sleep(2)
                print("Jedoch hast du schon eine Waffe in der Hand.")
                time.sleep(1.5)
                print("Lege die Waffe ab, um eine neue auszurüsten.")
                time.sleep(1.5)
                raumH(environment)
            else:    
                time.sleep(0.5)
                print("Du öffnest den Arzneischrank und darin befindet sich eine riesige Wumme.")
                print("Es steht 'Monsterhunter' auf der überdimsensionalen Knarre.")
                time.sleep(2)
                print("(1) Nehme den Monsterhunter")
                time.sleep(1.5)
                print("(2) Den Monsterhunter liegen lassen")
                time.sleep(1.5)
            
                cmdlist = ['1', '2']
                cmd = getcmd(cmdlist)
                
                if cmd == '1':
                    time.sleep(0.5)
                    print("Du nimmst den Monsterhunter.")
                    time.sleep(1.5)
                    print("Danke Edith")
                    mW.remove('Faust')
                    mW.append('Monsterhunter')
                    mHP.remove(3)
                    mHP.append(30)
                    time.sleep(1.5)
                    raumH(environment)
                
                elif cmd == '2':
                    time.sleep(0.5)
                    print("Du lässt den Monsterhunter lieber liegen.") 
                    time.sleep(1)
                    raumH(environment)
        
        else:
            print("Die Tür ist verschlossen.")
            raumH(environment)
            
    elif cmd == 'untersuche nachttisch' or cmd == 'untersuche nachttische':
        time.sleep(0.5)
        print("Du untersuchst alle Nachttische in diesem Raum,")
        print("jedoch befindet sich in keiner etwas nützliches.")
        time.sleep(3)
        raumH(environment)
        
    elif cmd == 'untersuche kiste' or cmd == 'untersuche kisten':
        time.sleep(0.5)
        print("Du untersuchst alle Listen in diesem Raum,")
        print("jedoch befindet sich in keiner etwas nützliches.")
        time.sleep(3)
        raumH(environment)
            
        
def treppenhausHZ(environment):
    time.sleep(0.5)
    print("Momentane Position: Treppenhaus Mannschaftsquartiere/Hauptzentrale")
    time.sleep(0.5)
    print("(1) gehe Richtung Hauptzentrale")
    time.sleep(0.5)
    print("(2) gehe Richtung Mannschaftsquartiere")
    time.sleep(0.5)
    print("( ) Sonstiges")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'umsehen']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst die Treppe hinauf und durch die Tür.")
        if mLosungswort[0]=='Dystopia':
            time.sleep(0.5)
            hauptzentraleFlur(environment)
        elif iWulffLP[0] <= 0:
            time.sleep(0.5)
            hauptzentraleFlurNachKampf(environment)
        else:
            time.sleep(0.5)
            print("Das erste was du siehst, ist ein älterer Mann, der mit einer Waffe auf dich ziehlt.")
            time.sleep(2.5)
            print("...")
            time.sleep(0.5)
            print("''Nicht schon wieder''")
            time.sleep(0.5)
            print("...")
            time.sleep(2)
            begegnungMitWulff(environment)
    
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst in Richtung Gefangenentrakt.")
        time.sleep(1)
        print("Du gehst den Flur entlang und gehst durch die Tür in den nächsten Raum.")
        time.sleep(2.5)
        print("Du befindest dich in den Raum mit den Türen E, F, G, H.")
        time.sleep(2)
        mannschaftsquartiereFlur3(environment)
        
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich ein wenig um.")
        print("Jedoch gibt es in diesem Treppenhaus nichts Interessantes zu entdecken.")
        time.sleep(1)
        treppenhausHZ(environment)
        
    
def begegnungMitWulff(environment):
    if mLippeAb[0] == 'Abgebissen':
        time.sleep(0.5)
        print("'Du bist das also, der den Vater der Ehrwürdigen tötete', sagt der alte Mann")
        time.sleep(2.5)
        print("und schießt ohne zu zögern mit seiner Waffe auf dich.")
        mLP[0] = mLP[0] - 6
        time.sleep(2)
        kampfWulff(environment)
        
    else:
        time.sleep(0.5)
        wulffGespräch(environment)
        
def hauptzentraleFlur(environment):
    time.sleep(0.5)
    print("Wulff grüßt dich herzlichst.")
    time.sleep(2)
    print("Momentane Position: Flur")
    time.sleep(0.5)
    print("(1) Gehe Richtung Mannschaftsquartiere")
    time.sleep(0.5)
    print("(2) Gehe Richtung Hauptzentrale")
    time.sleep(0.5)
    print("()  Sonstiges")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'umsehen', 'rede mit wulff']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst in Richtung Mannschaftsquartiere")
        time.sleep(0.5)
        treppenhausHZ(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst in Richtung Hauptzentrale")
        time.sleep(0.5)
        hauptzentrale(environment)
        
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich ein wenig um.")
        print("Hier scheint nichts zu sein, außer der Wache WULFF.")
        time.sleep(0.5)
        hauptzentraleFlur(environment)
        
    elif cmd == 'rede mit wulff':
        time.sleep(0.5)
        print("Du gehst zu Wulff.")
        time.sleep(0.5)
        print("'Ah, du bist es.")
        time.sleep(0.7)
        print(" Früher war ich auch ein Abenteurer,")
        time.sleep(1.2)
        print(" doch dann habe ich einen Pfeil ins Knie bekommen.'")
        time.sleep(1.8)
        print("...")
        time.sleep(1)
        print("Du gehst ohne etwas zu sagen weg.")
        hauptzentraleFlur(environment)
        
    
def hauptzentraleFlurNachKampf(environment):
    time.sleep(0.5)
    print("Wulff liegt tot auf dem Boden.")
    time.sleep(2)
    print("Momentane Position: Flur")
    time.sleep(0.5)
    print("(1) Gehe Richtung Mannschaftsquartiere")
    time.sleep(0.5)
    print("(2) Gehe Richtung Waffenkammer")
    time.sleep(0.5)
    print("()  Sonstiges")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'umsehen', 'untersuche wulff']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du gehst in Richtung Mannschaftsquartiere")
        time.sleep(1)
        treppenhausHZ(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst in Richtung Hauptzentrale")
        time.sleep(1)
        hauptzentrale(environment)
        
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich ein wenig um.")
        print("In diesem Flur scheint nichts interessantes zu sein,")
        print("außer dem toten WULFF auf dem Boden.")
        time.sleep(1)
        hauptzentraleFlurNachKampf(environment)
        
    elif cmd == 'untersuche wulff':
        time.sleep(0.5)
        print("Als du den Leichnam von Wulff untersuchst, findest du eine Pfeilspitze")
        print("in einer seiner Taschen. Du lässt sie lieber dort, wo du sie gefunden hast.")
        hauptzentraleFlurNachKampf(environment)
    
        
def hauptzentrale(environment):
    time.sleep(0.5)
    print("Momentane Position: Hauptzentrale")
    time.sleep(0.5)
    print("(1) Gehe Richtung Mannschaftsquartiere")
    time.sleep(0.5)
    print("(2) Gehe Richtung Waffenkammer")
    time.sleep(0.5)
    print("(3) Gehe Richtung Labor")
    time.sleep(0.5)
    print("(4) Gehe Richtung medizinische Abteilung")
    time.sleep(0.5)
    print("()  sonstige Befehle")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', '3', '4', 'umsehen', 'rede mit frau', 'rede mit merana', 'gehe zu frau', 'gehe zu merana',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Du betrittst den Flur Richtung Treppenhaus")
        time.sleep(0.5)
        if mLosungswort[0]=='Dystopia':
            hauptzentraleFlur(environment)
        elif iWulffLP[0] <= 0:
            hauptzentraleFlurNachKampf(environment)
        else:
            hauptzentraleFlur(environment)
            
            
    elif cmd == '2':
        time.sleep(0.5)
        print("Du gehst Richtung Waffenkammer")
        time.sleep(1)
        waffenkammerFlur(environment)
        
    elif cmd == '3':
        time.sleep(0.5)
        print("Du gehst in Richtung Labor")
        time.sleep(1)
        laborFlur(environment)
        
    elif cmd == '4':
        time.sleep(0.5)
        print("Du gehst in Richtung der medizinischen Abteilung")
        time.sleep(1)
        medAbteilungFlur(environment)
    
    elif cmd == 'umsehen':
        time.sleep(0.5)
        print("Du siehst dich ein wenig um.")
        time.sleep(1)
        print("Von der imposanten Einrichtung der Hauptzentrale abgesehen, ist hier recht wenig los.")
        time.sleep(2)
        print("Die zwei Wachen stehen in der Nähe der Frau, jedoch versucht der eine, der mit dir")
        print("das Gespräch führte, angestrengt nicht in deine Richtung zu schauen.")
        time.sleep(5)
        print("Die FRAU sitzt ruhig auf ihrem Stuhl und hat die Augen geschlossen.")
        time.sleep(2)
        print("Von der Hauptzentrale führen vier Wege in vier verschiedene Richtungen.")
        time.sleep(2)
        hauptzentrale(environment)
        
    elif cmd == 'rede mit frau':
        time.sleep(0.5)
        print("Du gehst an den zwei Wachen vorbei zu der Frau auf dem Kapitäsnsitz.")
        print("Sie trägt eine elegante grau-grüne Robe, öffnet die Augen und sieht ")
        print("dich seelenruhig an.")
        time.sleep(5)
        gesprächMerana(environment)
    
def waffenkammerFlur(environment):
    if iRotAuge4HP[0] >= 0:
        time.sleep(0.5)
        print("Als du den Raum betrittst, greift dich ein Rotäugiger an!")
        time.sleep(0.5)
        kampfRotAuge4(environment)
        
    else:
        time.sleep(0.5)
        print("Momentane Position: Flur Richtung Waffenkammer")
        time.sleep(0.5)
        print("(1) Gehe Richtung Hauptzentrale")
        time.sleep(0.5)
        print("(2) Gehe Richtung Waffenkammer")
        time.sleep(0.5)
        print("()  Sonstiges")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', 'umsehen']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("Du gehst in Richtung Hauptzentrale.")
            time.sleep(1)
            hauptzentrale(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("Du gehst in Richtung Waffenkammer.")
            time.sleep(1)
            waffenkammer(environment)
            
        elif cmd == 'umsehen':
            time.sleep(0.5)
            print("Du siehst dich ein wenig um.")
            time.sleep(0.8)
            print("Ein WASSERSPENDER ist an der rechten Wand befestigt.")
            print("Anonsten scheint hier nichts auffälliges zu sein.")
            time.sleep(2.5)
            waffenkammerFlur(environment)
            
        elif cmd == 'untersuche wasserspender':
            time.sleep(0.5)
            print("Als du dich dem Wasserspender näherst, kommt ein schöner Strahl Wasser heraus.")
            time.sleep(1.5)
            print("Du bist etwas beunruhigt, da die Farbe des Wassers einen roten Unterton hat.")
            time.sleep(1.5)
            waffenkammerFlur(environment)
            
        elif cmd == 'benutze wasserspender':
            time.sleep(0.5)
            print("Du trinkst das Wasser des Spenders.")
            time.sleep(2)
            print("Etwas an diesem Wasser schmeckt seltsam...")
            time.sleep(2.5)
            print("Du fühlst dich seltsam benommen und deine Augen beginnen zu jucken...")
            time.sleep(3)
            print("Du verlierst die Kontrolle über deinen Körper und dir wird schwarz vor Augen...")
            time.sleep(3.5)
            exit()
        
def waffenkammer(environment):
    if 'Jonas Laserkanone' in mW and iBewFrau[0] == 'Aggressiv':
        print("Du betritts die Waffenkammer.")
        print("Eine bis an die Zähne bewaffnete Frau kommt auf dich zu.")
        print("'He, was suchst d...'")
        print("Sie blickt auf deine Laserpistole.")
        print("'Wo hast du die her?! Die hat doch Jonas gehört!'")
        print("Du erzählst ihr, dass du die Laserkanone in einem Schrank in Jonas Quartier")
        print("gefunden hast.")
        print("Außerdem erzählst du ihr wie es dort unten aussah.")
        print("Als du ihr die Geschichte erzählst, werden ihre Augen ganz glasig")
        print("und Tränen strömen ihr Gesicht herunter.")
        print("Tiefes Mitgefühl ergreift dich.")
        print("Du gibst ihr Jonas Laserkanone.")
        mW.remove('Jonas Laserkanone')
        mW.append('Faust')
        mG2.append('Jonas Laserkanone')
        mHP.remove(10)
        mHP.append(3)
        print("'Danke...', sagt die Frau und wischt sich mit einem Ärmel die Tränen vom Gesicht.")
        print("'Ich gehe jetzt weg von hier, du kannst dir nehmen, was du willst.")
        print(" Und nochmal, danke.'")
        iBewFrau.remove('Aggressiv')
        iBewFrau.append('Traurig')
        print("Die Frau schenkt dir ein erschöpftes Lächeln und tritt aus der Waffenkammer heraus.")
        waffenkammer(environment)
    elif iBewFrau[0] == 'Aggressiv':
        print("Du betritts die Waffenkammer.")
        print("Ein lauter Knall ist zu hören!")
        print("...")
        print("Ein Schuss verfehlte dich nur knapp am Kopf.")
        print("Eine Stimme ist auf einmal zu hören, jedoch kannst du nicht genau ausmachen,")
        print("von wo sie zu hören ist.")
        print("'Noch ein Schritt näher und du bist einen Kopf kürzer'")
        print("(1) Einen Schritt näher gehen")
        print("(2) Zurück zum Flur gehen")
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            print("Du machst einen Schritt weiter vorwärts.")
            print("Leider hatte die Stimme recht behalten.")
            print("Einen Kopf kürzer kannst du leider nicht weiter gehen und bleibst deshalb liegen.")
            exit()
        
        elif cmd == '2':
            print("Du ergreifst schleunigst die Flucht.")
            waffenkammerFlur(environment)
        
        
    else:    
        print("Momentane Position: Waffenkammer")
        print("(1) Gehe Richtung Hauptzentrale")
        print("( ) Sonstiges")
    
        cmdlist = ['1', 'umsehen', 'öffne schrank']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            time.sleep(0.5)
            print("Du gehst in Richtung Hauptzentrale.")
            time.sleep(0.5)
            waffenkammerFlur(environment)
        
        elif cmd == 'umsehen':
            time.sleep(0.5)
            print("Du siehst dich ein wenig um.")
            time.sleep(0.5)
            print("Die Waffenkammer wurde komplett geplündert!")
            print("'So wie die Frau vorhin ausgestattet war, hat sie wohl alles mitgenommen...'")
            print("Ein SCHRANK in dem Raum scheint noch etwas nützliches zu beinhalten.")
            waffenkammer(environment)
            
        elif cmd == 'öffne schrank':
            if 'Monsterjäger' in mAus or 'Monsterjäger' in mG8:
                time.sleep(0.5)
                print("Der Schrank ist leer.")
                time.sleep(1.5)
                maschinenraumFlur(environment)  
            elif mAus[0] != 'Unterhose':
                time.sleep(0.5)
                print("Du öffnest den Schrank und darin befindet sich eine Monsterjäger Rüstung.")
                time.sleep(2)
                print("Du hast jedoch schon Kleidung an und kannst die Rüstung nicht anziehen.")
                time.sleep(2.5)
                print("ziehe deine Kleidung aus, bevor du etwas neues anziehst.")
                time.sleep(2)
                maschinenraumFlur(environment)
            else:    
                time.sleep(0.5)
                print("Du öffnest den Schrank und darin befindet sich eine Monsterjäger Rüstung.")
                time.sleep(2)
                print("(1) Ziehe Rüstung an")
                time.sleep(1.5)
                print("(2) Rüstung liegen lassen")
                time.sleep(1.5)
            
                cmdlist = ['1', '2']
                cmd = getcmd(cmdlist)
                
                if cmd == '1':
                    time.sleep(0.5)
                    print("Du ziehst die Rüstung an.")
                    time.sleep(1.5)
                    print("Jetzt bin gewappnet für eine Monsterjagd, zumindest was das Aussehen betrifft.")
                    mAus.remove('Unterhose')
                    mAus.append('Monsterjäger')
                    mS.remove(1)
                    mS.append(13)
                    time.sleep(2)
                    maschinenraumFlur(environment)      
                    
                elif cmd == '2':
                    time.sleep(0.5)
                    print("Du lässt den Overall lieber liegen.") 
                    time.sleep(1)
                    maschinenraumFlur(environment)
            
    
def laborFlur(environment):
    if iRotAuge5HP[0] >= 0:
        time.sleep(0.5)
        print("Als du den Raum betrittst, greift dich ein Rotäugiger an!")
        time.sleep(0.5)
        kampfRotAuge5(environment)
        
    else:
        print("Momentane Position: Flur")
        print("(1) Gehe Richtung Hauptzentrale")
        print("(2) Gehe Richtung Labor")
        print("()  Sonstiges")
        
        cmdlist = ['1', '2', 'umsehen', 'öffne truhe',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("Du gehst in Richtung Hauptzentrale")
            hauptzentrale(environment)
            
        elif cmd == '2':
            print("Du gehst in Richtung Labor")
            labor(environment)
            
        elif cmd == 'öffne truhe':
            if 'Laserschwert' in mAus or 'Laserschwert' in mG7:
                time.sleep(0.5)
                print("Die Truhe ist leer.")
                time.sleep(1)
                laborFlur(environment) 
            elif mW[0] != 'Faust':
                time.sleep(0.5)
                print("Du öffnest die Truhe und darin befindet sich ein Offiziersschwert.")
                time.sleep(2)
                print("Darauf eingraviert steht: Eigentum von L. Aser.")
                time.sleep(2)
                print("Jedoch hast du schon eine Waffe in der Hand.")
                time.sleep(1.5)
                print("Lege die Waffe ab, um eine neue auszurüsten.")
                time.sleep(1.5)
                raumH(environment)
            else:    
                time.sleep(0.5)
                print("Du öffnest die Truhe und darin befindet sich ein Offiziersschwert.")
                time.sleep(2)
                print("Darauf eingraviert steht: Eigentum von L. Aser.")
                time.sleep(2)
                print("(1) Nehme das Schwert")
                time.sleep(1.5)
                print("(2) Schwert liegen lassen")
                time.sleep(1.5)
            
                cmdlist = ['1', '2']
                cmd = getcmd(cmdlist)
                
                if cmd == '1':
                    time.sleep(0.5)
                    print("Du nimmst das L. Aser Schwert.")
                    time.sleep(1.5)
                    print("Das habe ich mir schon immer gewünscht...")
                    mW.remove('Faust')
                    mW.append('Laserschwert')
                    mHP.remove(3)
                    mHP.append(15)
                    time.sleep(1.5)
                    raumH(environment)
                
                elif cmd == '2':
                    time.sleep(0.5)
                    print("Du lässt das Schwert lieber liegen.") 
                    time.sleep(1)
                    raumH(environment)
                
            
        elif cmd == 'umsehen':
            print("Du siehst dich ein wenig um.")
            print("Ein WASSERSPENDER ist an einer Seite des Raumes zu finden.")
            print("Darunter befindet sich eine TRUHE.")
            waffenkammerFlur(environment)
            
        elif cmd == 'untersuche wasserspender':
            time.sleep(0.5)
            print("Als du dich dem Wasserspender näherst, kommt ein schöner Strahl Wasser heraus.")
            time.sleep(1.5)
            print("Du bist etwas beunruhigt, da die Farbe des Wassers einen roten Unterton hat.")
            time.sleep(1.5)
            laborFlur(environment)
            
        elif cmd == 'benutze wasserspender':
            time.sleep(0.5)
            print("Du trinkst das Wasser des Spenders.")
            time.sleep(2)
            print("Etwas an diesem Wasser schmeckt seltsam...")
            time.sleep(2.5)
            print("Du fühlst dich seltsam benommen und deine Augen beginnen zu jucken...")
            time.sleep(3)
            print("Du verlierst die Kontrolle über deinen Körper und dir wird schwarz vor Augen...")
            time.sleep(3.5)
            exit()
    
    
def labor(environment):
    if iVerProf[0] == 'Verrückt':
        print("Als du in das Labor eintrittst, kommt dir ein Mann mit zerzaustem, langem Haar entgegen.")
        print("Er fragt dich: 'Hast du meinen Schnuffi dabei?!")
        if mStoffKuscheltier[0] == 'Rotauge':
            print("Er sieht dich erwartungsvoll an, als er jedoch merkt, wie verwirrt du bist,")
            print("dreht er um und läuft haareraufend im Kreis.")
            print("Du verlässt vorsichtshalber den Raum.")
            laborFlur(environment)
        else:
            print("'DU HAST MEINEN SCHNUFFI GEFUNDEN!!!")
            print(" Vielen Dank dafür!")
            print(" Wenn ich dir irgendwie helfen kann, sag einfach bescheid, ja?'")
            iVerProf.remove('Verrückt')
            iVerProf.append('Schnuffi')
            labor(environment)
    else:
        print("Momentane Position: Labor")
        print("(1) Gehe Richtung Hauptzentrale")
        print("( ) Sonstiges")
    
    cmdlist = ['1', 'umsehen','rede mit mann', 'rede mit professor', 'öffne luke',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("Du gehst in Richtung Hauptzentrale")
        laborFlur(environment)
        
    elif cmd == 'rede mit mann' or cmd == 'rede mit professor':
        time.sleep(0.5)
        print("Der Mann hält sein Stofftier in der Hand und sieht dich überglücklich an.")    
        print("Er fragt dich heiter: 'Was möchtest du wissen?'")
        gesprächProfessor(environment)
                
    elif cmd == 'umsehen':
        print("Du siehst dich ein wenig um.")
        print("Ein alter, verbeulter SCHRANK fällt dir sofort ins Auge, sonst sind Stapelweise")
        print("Kisten im Raum verteilt.")
        print("Ansonsten liegen auf vielen Tischen seltsame Gerätschaften, die du lieber nicht")
        print("anfassen solltest.")
        print("Der alte MANN spielt in einer Ecke mit seinem Stofftier.")
        labor(environment)
        
    elif cmd == 'öffne schrank':
        if 'Panzerung' in mAus or 'Panzerung' in mG5:
            time.sleep(0.5)
            print("Der Schrank ist leer.")
            time.sleep(1.5)
            labor(environment)  
        elif mAus[0] != 'Unterhose':
            time.sleep(0.5)
            print("Du öffnest den Schrank und darin befindet sich ein gepanzerter Overall.")
            time.sleep(2)
            print("Du hast jedoch schon Kleidung an und kannst den Overall nicht anziehen.")
            time.sleep(2.5)
            print("ziehe deine Kleidung aus, bevor du etwas neues anziehst.")
            time.sleep(2)
            labor(environment)
        else:    
            time.sleep(0.5)
            print("Du öffnest den Schrank und darin befindet sich eine gepanzerter Overall.")
            time.sleep(2)
            print("(1) Ziehe gepanzerten Overall an")
            time.sleep(1.5)
            print("(2) Gepanzerter Overall liegen lassen")
            time.sleep(1.5)
        
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("Du ziehst den Overall an.")
                time.sleep(1.5)
                print("Etwas schwer, du hast dich jedoch seit langem nicht mehr so sicher gefühlt.")
                mAus.remove('Unterhose')
                mAus.append('Panzerung')
                mS.remove(1)
                mS.append(15)
                time.sleep(2)
                labor(environment)      
                
            elif cmd == '2':
                time.sleep(0.5)
                print("Du lässt den gepanzerten Overall lieber liegen.") 
                time.sleep(1)
                labor(environment)
        
        
        
    elif cmd == 'öffne luke':
        print("Du schiebst eine Kiste beiseite und darunter befindet sich eine Luke.")
        print("Du öffnest sie und kletterst an einer Leiter abwärts.")
        print("Unten angekommen öffnest du eine weitere Luke.")
        print("Du springst heraus, dabei schließt sie sich.")
        print("Du probierst die Luke zu öffnen, jedoch ohne Erfolg.")
        generatorraum(environment)
    
def medAbteilungFlur(environment):
    if iRotAuge6HP[0] >= 0:
        time.sleep(0.5)
        print("Als du den Raum betrittst, greift dich ein Rotäugiger an!")
        time.sleep(0.5)
        kampfRotAuge6(environment)
        
    else:
        print("Momentane Position: Flur")
        print("(1) Gehe Richtung Hauptzentrale")
        print("(2) Gehe Richtung medizinische Abteilung")
        print("()  Sonstiges")
        
        cmdlist = ['1', '2', 'umsehen']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("Du gehst in Richtung Hauptzentrale")
            hauptzentrale(environment)
            
        elif cmd == '2':
            print("Du gehst in Richtung der medizinischen Abteilung")
            medAbteilung(environment)
            
        elif cmd == 'umsehen':
            print("Du siehst dich ein wenig um.")
            print("Da hängt eine Kamera vor der medizinischen Abteilung.")
            print("Außerdem befindet sich hier moch ein WASSERSPENDER.")
            medAbteilungFlur(environment)
            
        elif cmd == 'untersuche wasserspender':
            time.sleep(0.5)
            print("Als du dich dem Wasserspender näherst, kommt ein schöner Strahl Wasser heraus.")
            time.sleep(1.5)
            print("Du bist etwas beunruhigt, da die Farbe des Wassers einen roten Unterton hat.")
            time.sleep(1.5)
            medAbteilungFlur(environment)
            
        elif cmd == 'benutze wasserspender':
            time.sleep(0.5)
            print("Du trinkst das Wasser des Spenders.")
            time.sleep(2)
            print("Etwas an diesem Wasser schmeckt seltsam...")
            time.sleep(2.5)
            print("Du fühlst dich seltsam benommen und deine Augen beginnen zu jucken...")
            time.sleep(3)
            print("Du verlierst die Kontrolle über deinen Körper und dir wird schwarz vor Augen...")
            time.sleep(3.5)
            exit()
        
def medAbteilung(environment):
    if 'Jonas Laserkanone' in mW and iMedAbtEingang[0] == 'Verschlossen':
        print("Eine Kamera vor dem Eingang ist auf dich gerichtet.")
        print("'Wer sind sie?', dröhnt es aus der Gegensprechanlage unter der Kamera.")
        print("'Ohh, was haben sie denn da?")
        print(" Wenns sie mir ihre Schusswaffe überlassen, lasse ich sie herein.")
        print(" Ihre Wunden könnte ich auch Versorgen")
        print(" Was meinen sie?")
        print("(1) Zustimmen")
        print("(2) Ablehnen")
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            print("'Sehr schön, ich mache auf.")
            print("Die Tür öffnet sich und eine ältere Dame tritt heraus.")
            iMedAbtEingang.remove('Verschlossen')
            iMedAbtEingang.append('Geöffnet')
            print("'Das ist aber nett von ihnen, wirklich sehr nett.'")
            print("Du gibst ihr deine Waffe.")
            mW.remove('Jonas Laserkanone')
            mW.append('Faust')
            mG2.append('Jonas Laserkanone')
            mHP.remove(10)
            mHP.append(3)
            print("'Was ist denn mit ihnen geschehen?!")
            print(" Sie sehen aus, als wäre ein Raumschiff über sie gefahren!")
            print(" Lass mich kurz ihre Wunden versorgen...")
            print("...")
            mLP[0] = mLP[0] - mLP[0] + 100
            print(" Das wars.")
            print(" Falls sie hier nochmal mit Kleidung, die besseren Schutz bieten, als die meinigen,")
            print(" vorbei kommen, gebe ich ihnen etwas dafür. Mein Name ist übrigens Edith.'")
            print("Die alte Dame geht wieder durch die Tür.")
            print("Du folgst ihr")
            medAbteilung(environment)
            
        elif cmd == '2':
            print("'Dann geh doch bitte, wenn sie so freundlich wären.")
            print("Du gehst.")
            medAbteilungFlur(environment)
      
    elif iMedAbtEingang[0] == 'Verschlossen':
        print("Eine Kamera vor dem Eingang ist auf dich gerichtet.")
        print("'Wer sind sie?', dröhnt es aus der Gegensprechanlage unter der Kamera.")
        print("'Sie haben hier nichts verloren und ich kenne sie nicht, gehen sie!'")
        print("Da du keine Lust auf Streit hat, gehst du einige Schritte zurück.")
        medAbteilungFlur(environment)
        
    else:
        
        print("Momentane Position: Medizinische Abteilung")
        print("(1) Gehe Richtung Hauptzentrale")
        print("( ) Sonstiges")
    
        cmdlist = ['1', 'umsehen', 'rede mit frau']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            print("Du gehst in Richtung Hauptzentrale")
            medAbteilungFlur(environment)
        
        elif cmd == 'umsehen':
            print("Du siehst dich ein wenig um.")
            print("Die alte FRAU steht im Raum.")
            medAbteilung(environment)
            
        elif cmd == 'rede mit frau':
            time.sleep(0.5)
            gesprächEdith(environment)
            
def gefangenentraktZentraleKeinNarrezMehr(environment):
    time.sleep(0.5)
    print("Du betrittst den Raum.")
    time.sleep(0.5)
    print("Alles scheint wie zuvor zu sein, jedoch ist Narrez spurlos verschwunden.")
    time.sleep(1)
    
    cmdlist = ['umsehen', 
               'gehe zu schleuse', 
               'öffne schleuse', 
               'untersuche schleuse', 
               'untersuche fluchtkapsel',
               'gehe zu fluchtkapsel',
               'benutze fluchtkapsel',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        time.sleep(0.5)
        print("Du schaust dich im Raum um.")
        time.sleep(1.5)
        print("Viele verschlossene Schränke stehen auf der gegenüberliegenden Seite")
        print("des Rechners.")
        time.sleep(6)
        print("Eine FLUCHTKAPSEL ist neben dem Rechner zu sehen.")
        time.sleep(1.5)
        gefangenentraktZentraleKeinNarrezMehr(environment)
        
    elif cmd == 'untersuche fluchtkapsel' or cmd == 'gehe zu fluchtkapsel' or cmd == 'benutze fluchtkapsel':
        if iGenerator[0] == 'An':
            time.sleep(0.5)
            print("Du siehst, dass die Fluchtkapsel wieder aktiv ist.")
            dieFlucht(environment)
        else:
            time.sleep(0)
            print("Die Fluchtkapsel lässt sich nicht öffnen.")
            print("Der zugehörige GENERATOR muss erst wieder angeschaltet werden.")
            gefangenentraktZentraleKeinNarrezMehr(environment)
        
        
    elif cmd == 'gehe zu schleuse' or cmd == 'öffne schleuse' or cmd == 'untersuche schleuse':
        time.sleep(0.5)
        print("Du bewegst dich in Richtung Schleuse")
        time.sleep(1.5)
        print("Die Schleuse öffnet sich und du trittst hinein.")
        time.sleep(1.5)
        print("Du bist in einem Treppenhaus.")
        time.sleep(1)
        print("Auf einer Karte an der Wand siehst du, das über dir")
        print("die Mannschaftsquartiere sein müssten und unter dir ")
        print("der Maschinenraum.")
        time.sleep(6)
        print("Ein Weg führt nach oben, der andere nach unten.")
        time.sleep(1.5)
        treppenhausGZ(environment)
    
    
    
    
    
    
    
    
    
        
    
    
    
        
        


# - - - - - Gespräche - - - - -                          

def narrezGespräch(environment):
    time.sleep(2)
    print("Als du den Raum betrittst, zielt ein Mann mit einem Blaster auf dich.")
    time.sleep(2)
    print("Er hat eine aufgerissene Lippe und scheint nicht überrascht zu sein, dich zu sehen.")
    print("Er trägt eine Mechanikeruniform der 'Galaxy Space Traders', rot mit schwarzen Verzierungen.")
    print("Seine Statur ist eher mager, sein Gesicht eingefallen, dunkle Augenringe hängen unter seinen Augen.") 
    print("'Was suchst du hier?', dröhnt es aus seinen wulstigen Lippen.")
    narrezGespräch1(environment)

def narrezGespräch1(environment):
    
    print("(1) Nachfragen, wo ihr euch befindet")
    print("(2) Erklären, dass du das Gedächtnis verloren hast")
    print("(3) Fragen, was dich angegriffen hat")
    print("(4) Bitten, die Waffe herunter zu nehmen")
    print("(5) Drohen, damit er die Waffe herunter nimmt")
    
    cmdlist = ['1', '2', '3', '4', '5']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("Der Mann schüttelt den Kopf.")
        print("'Das weißt du nicht? Was ist denn mit dir los?")
        print(" Wir sind auf nem SpaceTraderShip unterwegs nach Karion 4.")
        print(" Die brauchen wohl Essen, Waffen und was weiß ich alles.")
        print(" Ach ja, und Gefangene.'")
        print("Der Mann zieht eine Augenbraue hoch, kneift die Augen zusammen und begutachtet dich.")
        if mAus[0] == 'Gefangenenoverall':
            print("'So wie du ausschaust, bist du wohl wegen irgendwas eingebuchtet worden.")
            print(" Was hast du gemacht? Jemanden umgebracht? Was genommen was nich dir gehört?")
            print(" Ist ja jetzt egal.")
            print(" Noch irgendwelche letzten Worte bevor ich dich Abknall?'")
            narrezGespräch2(environment)
        else:
            print("'Bist wohl ein Verrückter, so wie du rumläuft")
            print(" Noch irgendwelche letzten Worte bevor ich dich Abknall?'")
            narrezGespräch2(environment)
            
    elif cmd == '2':
        print("Der Mann schaut dich verwundert an.")
        print("'Du kannst dich an nichts erinnern?")
        print(" Bist wohl gegen ne Wand gerannt, wie?'")
        print("Die Mundwinkel des Mannes richten sich auf.")
        print("'Da du vom Gefangenenabteil des Schiffes kommst, kannst du dir wohl denken, wer du bist")
        print(" oder zumindest was du bist.")
        print(" Noch irgendwelche letzten Worte bevor ich dich Abknall?'")
        narrezGespräch2(environment)
        
    elif cmd =='3':
        print("Der Mann zuckt mit den Achseln")
        print("'Wer weiß das schon, die Hohlbirnen rennen hier auf dem ganzen Schiff rum.")
        print(" Die wichtigere Frage jedoch ist, was machst du hier?")
        narrezGespräch1(environment)       
    
    elif cmd == '4':
        print("'Einen Scheiß werd ich tun!'")
        narrezGespräch1(environment)
        
    elif cmd == '5':
        print("'HAHAHAHA'")
        print("Der Mann lacht und bevor du nur daran denkst ihn anzugreifen, schießt er auf dich.")
        print("Die Laserpistole brennt ein Loch durch deinen Kopf.")
        print("Du bist auf der Stelle tot...")
        print("GAME OVER")
        exit
        
def narrezGespräch2(environment):
    print("(1) Ihn bitten, dich nicht zu erschießen")
    print("(2) Angreifen")
    print("(3) Versuchen zu Flüchten")
    
    cmdlist = ['1', '2', '3',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("'Mhhhh...'")
        print("Er kratzt sich mit der Laserpistole am Kopf.")
        print("'Das ließe sich einrichten, wenn du für mich was erledigst.'")
        print("(1) Zustimmen")
        print("(2) Ablehnen")
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("'Wunderbar!")
            print("Er nimmt die Waffe runter")
            print("'Wir werden ja noch richtig gute Freunde wenn das so weiter geht.'")
            print("Ein falsches Grinsen entsteht in seinem Gesicht.")
            print("'Ich bin übrigens Narrez.")
            narrezGespräch3(environment)
            
        elif cmd == '2':
            print("'Schade, hättest mir nützlich sein können.'")
            print("Der Mann schießt auf dich")
            print("Die Laserpistole brennt ein Loch durch dein Herz.")
            print("Du bist auf der Stelle tot...")
            print("GAME OVER")
            exit
            
    if cmd == '2' or cmd == '3':
        print("'Was machst du da?!'")
        print("Der Mann schießt ohne zu zögern auf dich.")
        print("Die Laserpistole brennt ein Loch durch dein Gesicht.")
        print("Du bist auf der Stelle tot...")
        print("GAME OVER")
        exit
        
def narrezGespräch3(environment):
    print("'Jetzt sperr mal deine Lauscher auf.")
    print(" Soweit ich die Sache hier begriffen habe, sind einige Schiffsgeneratoren ausgefallen.")
    print(" Einer muss runter ins Maschinendeck gehen und von dort aus den Generator 4FK neu starten.")
    print(" Und dieser Glückliche bist du.")
    print(" Bist du dieser Glückliche?")
    print()
    print("(1) Ja")
    print("(2) Nein")
    print("(3) Leck mich")
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("'Gute Entscheidung.")
        print(" Zum Maschinenraum gehts da runter'")
        print("Er zeigt in Richtung einer Schleuse.")
        print("'Ignoriere einfach den Weg nach oben, nur Chaos und Rotäugige dort oben.")
        print(" Beeil dich, ich hab nich den ganzen Tag Zeit.'")
        print("Er wendet sich einem großen Rechner zu, der mittig im Raum platziert ist")
        print("und ignoriert dich.")
        gefangenentraktZentrale(environment)
        
    elif cmd == '2' or cmd == '3':
        print("'Schade... Dabei lief es doch gerade so gut zwischen uns beiden.")
        print("Ein Schuss fällt, du kippst um...")
        print("GAME OVER")
        exit
        
def wulffGespräch(environment):
    print("'Wer bist du', fragt der alte Mann mit grießgrämiger Stimme.")
    print("Er trägt eine in die Tage gekommene, grau-grüne Robe, die mit einem seltsamen Wappen ")
    print("geschmückt ist.")
    if mAus[0] == 'Gefangenenoverall':
        print("Es scheint, als ob ihm jetzt erst deine Kleidung auffällt.")
        print("'Ein Gefangener also... dann mach dich auf was gefasst!'")
        kampfWulff(environment)
    else:
        print("'Du scheinst einer vom Schiffspersonal zu sein, mein Glückwunsch, dass du solange überlebt hast.")
        print(" Mein Name ist Wulff, ich passe auf, dass hier niemand ungebetenes rein kommt.")
        print(" Ich sage dir kurz das Losungswort, dann kannst du zur Hauptzentrale weiter gehen.")
        print(" Es lautet: 'Dystopia'")
        mLosungswort.remove('Bitteschön')
        mLosungswort.append('Dystopia')
        print(" Geh gleich weiter, ich muss hier Wache stehen.'")
        print("Nachdem Wulff wieder seinen Posten übernommen hat, gehst du in die Hauptzentrale hinein.")
    aqariaGespräch(environment)
    
def aqariaGespräch(environment):
    print("Die Hauptzentrale des Schiffes wirkt riesig, das könnte jedoch auch daran liegen,")
    print("dass du bis auf die Unmengen an Terminals, Bildschirmen, Sitz- und Stehplätzen,")
    print("Leuchten, Schalter und sonderbaren Gerätschaften keine Menschenseele erblickst,")
    print("bis auf zwei bewaffnete Männer in grau-grünen Roben und einer Frau, die auf dem Sitz")
    print("des Kapitäns platz genommen hat.")
    print("Die zwei Männer, beide bewaffnet mit Kampfstäben, drehen sich zu dir um und kommen sofort auf dich zu.")
    print("Der linke von ihnen stellt dir eine Frage.")
    aqariaGespräch1(environment)
    
def aqariaGespräch1(environment):
    if mLosungswort[0]=='Dystopia':
        print("'Wie lautet das Losungswort?'")
        print("(1) Dystopia")
        print("(2) öhhh... Quasten Pham?")
        print("(3) vielleicht Gurke?")
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("'Okay, du kannst dich hier frei bewegen.")
            print(" Aber mach keinen Scheiß. Hast du gehört?")
            hauptzentrale(environment)
        elif cmd == '2' or cmd == '3':
            aqariaGespräch2(environment)
            
          
    else:
        print("'Wie lautet das Losungswort?'")
        print("(1) Das Losungswort nennen")
        print("(2) mh... Quasten Pham?")
        print("(3) vielleicht Gurke?")
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("Aber das kannst du doch nicht wissen...")
            print("Und falls du es weißt, hier gibt es kein PowerPlay...")
            aqariaGespräch1(environment)
        elif cmd == '2' or cmd == '3':
            aqariaGespräch2(environment)
        
        
        
            
def aqariaGespräch2(environment):
    print("'Feind, was suchst du hier?")
    print(" Na sag schon! Was war da draußen los")
    print("(1) Ich habe nichts böses im Sinn, bitte glaubt mir")
    print("(2) Was seid ihr denn für Affen?")
    if iWulffLP[0] <= 0:
        print("(3) Ich hab den da draußen getötet und jetzt seid ihr dran!!! (Angreifen)")
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("'Nichts böses im Sinn? Wir sollten lieber auf Nummer sicher gehen und ihn tö...'")
            print("Von weiter hinten ertöhnt eine helle Frauenstimme")
            print("'Ich glaube dir, bitte lasst den Mann passieren.'")
            print("'Aber Herrin, wir können doch nicht...'")
            print("'Ich sagte, lasst ihn passieren!'")
            print("Die redsame Wache blickt zu Boden und seine Miene wird ganz hart.")
            print("'Jawohl Herrin... Du darfst nun gehen.")
            print("Das lässt du dir nicht zweimal sagen und gehst an den Wachen vorbei.")
            hauptzentrale(environment)
            
        elif cmd == '2':
            print("'AFFEN!")
            print("Der Mann gibt dir eine mit seinem Stab.")
            mLP[0] = mLP[0] - 6
            
            if mLP[0] >= 0:
                print("Aua!")
                aqariaGespräch2(environment)
            else:
                print("Das war ein Hieb zuviel...")
                endingDeath(environment)
            
        elif cmd == '3':
            print("Die beiden schlagen dich ohne zu zögern zusammen.")
            print("Du wirst ohnmächtig...")
            exit()
        
    else:
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            print("'Nichts böses im Sinn? Wir sollten lieber auf Nummer sicher gehen und ihn tö...'")
            print("Von weiter hinten ertöhnt eine helle Frauenstimme")
            print("'Ich glaube dir, bitte lasst den Mann passieren.'")
            print("'Aber Herrin, wir können doch nicht...'")
            print("'Ich sagte, lasst ihn passieren!'")
            print("Die redsame Wache blickt zu Boden und seine Miene wird ganz hart.")
            print("'Jawohl Herrin... Du darfst nun gehen.")
            print("Das lässt du dir nicht zweimal sagen und gehst an den Wachen vorbei.")
            hauptzentrale(environment)
            
        elif cmd == '2':
            print("'AFFEN!")
            print("Der Mann gibt dir eine mit seinem Stab.")
            mLP[0] = mLP[0] - 6
            
            if mLP[0] >= 0:
                print("Aua!")
                aqariaGespräch2(environment)
            else:
                print("Das war ein Hieb zuviel...")
                endingDeath(environment)
    

def gesprächMerana(environment):
    time.sleep(0.5)
    print("(1) Wie heißen sie?")
    print("(2) Warum befindet ihr euch auf diesem Schiff?")
    print("(3) Was befindet sich im Labor?")
    print("(4) Was befindet sich in der Waffenkammer?")
    print("(5) Was befindet sich in der medizinischen Abteilung?")
    print("(6) Gespräch beenden")
        
    cmdlist = ['1', '2', '3', '4', '5', '6',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("'Ich heiße Merana, meine zwei Freunde hier heißen Dalex und Femin,")
        print(" die Wache draußen heißt Wulff. Sie sind meine Beschützer auf meinem")
        print(" Weg nach Karion 4.")
        gesprächMerana(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("'Der Mörder meines Vaters, Narilyn Rezamo, besser bekannt als Narrez, wird auf diesem")
        print(" Schiff nach Karion 4, dem Gefängnisplaneten, gebracht. Oder jedenfalls war das der")
        print(" Plan vor dem Unfall mit der Wasserversorgung. Jeder, der heute von diesem Wasser trank,")
        print(" wurde wahnsinnig, bekam diese grässlichen Augen und war nicht mehr ansprechbar.")
        time.sleep(3)
        print("(1) Merana sagen, Narrez sei in der Zentrale des Gefängnistraktes.")
        print("(2) Etwas anderes Fragen")
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            if iNarrezMerana[0] == 'Unwissend':
                time.sleep(0.5)
                print("'Dieser Schuft ist nicht mehr in seiner Kryokammer?")
                print(" Dalex, Femin, da wir höchst wahrscheinlich nie auf Karion 4 landen werden,")
                print(" werden wir uns um diesen Schandfleck der Menschheit kümmern.")
                print(" Ihr wisst, was ihr zu tun habt'")
                print("Ohne zu zögern gehen die beiden Wachen aus dem Raum in Richtung Gefängnistrakt.")
                print("'Vielen Dank für diese Information. Mit diesem Schlüssel kannst du diese TRUHE dort hinten")
                print(" öffnen. Der Inhalt soll deinen Lohn darstellen.'")
                print("Nach kurzer Zeit kommen die beiden Wachen wieder zurück in die Hauptzentrale.")
                print("Merana blickt beide interessiert an, die schweigsame Wache nickt nur still.")
                print("Ein böses, aber auch erleichtertes Lächeln zieht sich über das Gesocht der Frau.")
                print("'Gut.', ist alles was sie zu sagen hat.")
                iNarrezMerana.remove('Unwissend')
                iNarrezMerana.append('Wissend')
                gesprächMerana(environment)
                
            else:
                time.sleep(0.5)
                print("'Das sagtest du bereits.'")
                gesprächMerana(environment)
            
              
        elif cmd == '2':
            time.sleep(0.5)
            gesprächMerana(environment)
            
    elif cmd == '3':
        time.sleep(0.5)
        print("'Im Labor befindet sich ein seltsamer Professor.")
        print(" Er hatte auch von diesem Wasser getrunken, jedoch hatte er schnell genug ein Gegengift parat.")
        print(" Jetzt ist er nicht mehr ganz bei Trost, das Gift hatte wohl schon sein Gehirn angegriffen.")
        print(" Er redet nur noch von irgendeinem Stofftier.")
        print(" Femin meinte, er hätte so ein Stofftier in den Mannschaftsquartieren bereits gesehen.")
        print(" Wo genau er es zuletzt gesehen hätte, weiß er aber nicht.")
        gesprächMerana(environment)
    
    elif cmd == '4':
        time.sleep(0.5)
        print("'In der Waffenkammer hat sich so eine verrückte Gefangene verbarrikadiert.")
        print(" Jeder, der dort hinein geht, kommt nicht wieder heraus.")
        print(" Da kommt man wohl nur rein, wenn man die richtige Waffe besitzt.")
        gesprächMerana(environment)
        
    elif cmd == '5':
        time.sleep(0.5)
        print("' In der medizinischen Abteilung hat sich eine ältere Dame eingeschlossen.")
        print(" Sie ist ohne Schutz und lässt aus Sicherheitsgründen niemanden rein.")
        print(" Wenn man ihr etwas geben würde, womit sie sich etwas sicherer fühlen könnte,")
        print(" würde sie vielleicht die Tür öffnen.")
        gesprächMerana(environment)
        
    elif cmd == '6':
        time.sleep(0.5)
        print("Du siest dich weiter im Raum um")
        hauptzentrale(environment)
        
    
def gesprächProfessor(environment):
    time.sleep(0.5)
    print("(1) Was ist mit dir geschehen?")
    print("(2) Haben sie irgendetwas nützliches hier drinnen?")
    print("(3) Wissen sie etwas nützliches über Generatoren?")
    print("(4) Gespräch beenden")
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("'Fast wäre ich so rotäugig wie die anderen, ich bin aber schlau gewesen!")
        print(" Medizin hilft jederfrau und jedermann, solange man weiß, wann man sie einsetzten kann!")
        gesprächProfessor(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("'Ein alten gepanzerten Anzug liegt in dem SCHRANK da hinten, den kannst du von mir aus haben.")
        print(" Ich habe jetzt alles, was man zum glücklich sein braucht.'")
        gesprächProfessor(environment)
        
    elif cmd == '3':
        time.sleep(0.5)
        print("'Mit Generatoren habe ich jetzt nichts mehr zu tun!")
        print(" Unter dieser Kiste dort hinten ist eine LUKE, sie führt direkt zu den Generatoren.")
        print(" Warum sollte man überhaupt eine Abkürzung zu den Generatoren in einem Labor einbauen!?'")
        gesprächProfessor(environment)
        
    elif cmd == '4':
        time.sleep(0.5)
        print("Du entfernst dich von dem Professor")
        labor(environment)
        
    
def gesprächEdith(environment):
    time.sleep(0.5)
    print(" Du gehst zu Edith.")
    if iKleineRüstung[0] == 'Besitz':
        print("Edith schaut dich begeistert an.")
        print("'Das ist ja mal ein schöner Overall und stabil sieht er auch aus.")
        print("Edith nimmt sich den Overall.")
        print("'Vielen Dank dafür, hier, ich gebe dir den Schlüssel zum ARZNEISCHRANK")
        print(" in Zimmer H.")
        iKleineRüstung.remove('Besitz')
        iKleineRüstung.append('Dame')
        medAbteilung(environment)
    else:
        print("Ich glaube wir haben momentan nichts mehr zu Besprechen.")
        medAbteilung(environment)
        
        
    
    
# - - - - - Kämpfe - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                          

def kampf1FlurSüdRechts(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iWesen1LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            print("Der Gegner weiter hinten greift dich an!")
            kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iWesen1S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iWesen1HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iWesen1HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen1HP[0] #
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
            elif iWesen1S < mHP: #
                iWesen1LP[0] = iWesen1LP[0] + iWesen1S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iWesen1HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iWesen1HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen1HP[0] #
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Der Weg hinter dir ist versperrt, Flucht unmöglich!")
        kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iWesen1LP >= [6]:
            print("Dein Gegner ist noch top fit!")
            kampf1FlurSüdRechts(environment)
        elif iWesen1LP >= [3]:
            print("Dein Gegner macht langsam schlapp!")
            kampf1FlurSüdRechts(environment)
        elif iWesen1LP >= [0]:
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampf1FlurSüdRechts(environment)

def kampf2FlurSüdRechts(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iWesen2LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            time.sleep(1)
            print("Noch perplex vom Kampf sinkst du zu Boden.")
            print("'Was waren das für Wesen?'")
            print("Nach ein paar Minuten der Erholung stehst du wieder auf.")
            flurSüdRechtsGeschlossen(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iWesen2S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an!!")                
                if mS >= iWesen2HP: #
                    time.sleep(1)
                    print("Deine Rüstung federt den kompletten Schaden ab!")
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iWesen2HP: #
                    time.sleep(1)
                    print("Dein Gegner trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen2HP[0] #
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
            elif iWesen2S < mHP: #
                iWesen2LP[0] = iWesen2LP[0] + iWesen2S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an!!")
                if mS >= iWesen2HP: #
                    time.sleep(1)
                    print("Deine Rüstung federt den kompletten Schaden ab!")
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iWesen2HP: #
                    time.sleep(1)
                    print("Dein Gegner trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen2HP[0] #
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Der Weg hinter dir ist versperrt, Flucht unmöglich!")
        kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN     
    elif cmd == 'status gegner':
        if iWesen2LP >= [8]:
            print("Dein Gegner ist noch top fit!")
            kampf2FlurSüdRechts(environment)
        elif iWesen2LP >= [4]:
            print("Dein Gegner macht langsam schlapp!")
            kampf2FlurSüdRechts(environment)
        elif iWesen2LP >= [0]:
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampf2FlurSüdRechts(environment)
 
def kampfFlurSüdLinks(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iEtwasLP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            flurSüdLinksGeschlossen(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iEtwasS >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iEtwasHP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iEtwasHP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iEtwasHP[0] #
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN
            elif iEtwasS < mHP: #
                iEtwasLP[0] = iEtwasLP[0] + iEtwasS[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iEtwasHP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iEtwasHP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iEtwasHP[0] #
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Es gibt keinen Fluchtweg!")
        kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iEtwasLP >= [10]: #
            print("Dein Gegner ist noch top fit!")
            kampfFlurSüdLinks(environment)
        elif iEtwasLP >= [5]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfFlurSüdLinks(environment)
        elif iEtwasLP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfFlurSüdLinks(environment)
            
def kampfWulff(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iWulffLP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            print("Du verschwendest keine Zeit und gehst in den nächsten Raum.")
            time.sleep(1)
            aqariaGespräch(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iWulffS >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iWulffHP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iWulffHP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iWulffHP[0] #
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN
            elif iWulffS < mHP: #
                iWulffLP[0] = iWulffLP[0] + iWulffS[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iWulffHP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iWulffHP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iWulffHP[0] #
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du flüchtest!")
        time.sleep(1)
        treppenhausHZ(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iWulffLP >= [20]: ######
            print("Dein Gegner ist noch top fit!")
            kampfWulff(environment)
        elif iWulffLP >= [10]: ######
            print("Dein Gegner macht langsam schlapp!")
            kampfWulff(environment)
        elif iWulffLP >= [0]: ######
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfWulff(environment)
    
def kampfMMonster(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iMMonsterLP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast das Monster besiegt!!!")
            time.sleep(1)
            print("Jetzt kannst du dich etwas genauer im Maschinenraum umschauen.")
            time.sleep(1)
            maschinenraum(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iMMonsterS >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iMMonsterHP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iMMonsterHP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iMMonsterHP[0] #
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN
            elif iMMonsterS < mHP: #
                iMMonsterLP[0] = iMMonsterLP[0] + iMMonsterS[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iMMonsterHP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iMMonsterHP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iMMonsterHP[0] #
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du flüchtest!")
        time.sleep(1)
        maschinenraumFlur(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iMMonsterLP >= [10]: #
            print("Dein Gegner ist noch top fit!")
            kampfMMonster(environment)
        elif iMMonsterLP >= [5]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfMMonster(environment)
        elif iMMonsterLP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfMMonster(environment)
            
def kampfRotAuge1(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge1LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            mannschaftsquartiereFlur(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iRotAuge1S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iRotAuge1HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge1HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge1HP[0] #
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge1S < mHP: #
                iRotAuge1LP[0] = iRotAuge1LP[0] + iRotAuge1S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iRotAuge1HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge1HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge1HP[0] #
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du kannst nicht flüchten!")
        time.sleep(1)
        kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iRotAuge1LP >= [12]: #
            print("Dein Gegner ist noch top fit!")
            kampfRotAuge1(environment)
        elif iRotAuge1LP >= [7]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfRotAuge1(environment)
        elif iRotAuge1LP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfRotAuge1(environment)
            
def kampfRotAuge2(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge2LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            mannschaftsquartiereFlur3(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iRotAuge2S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iRotAuge2HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge2HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge2HP[0] #
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge2S < mHP: #
                iRotAuge2LP[0] = iRotAuge2LP[0] + iRotAuge2S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iRotAuge2HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge2HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge2HP[0] #
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du kannst nicht flüchten!")
        time.sleep(1)
        kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iRotAuge2LP >= [10]: #
            print("Dein Gegner ist noch top fit!")
            kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge2LP >= [5]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge2LP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
            
def kampfRotAuge3(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge3LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            print("Der Gegner ließ etwas fallen...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du nimmst den Gegenstand auf...")
            time.sleep(1)
            print("Es handelt sich dabei um ein Stoffkuscheltier")
            time.sleep(1)
            print("Es hat die Form eines Affen")
            time.sleep(1)
            print("Gegenstand mitnehmen?")
            print("(1) Ja")
            print("(2) Nein")
            
            cmdlist =['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(1)
                print("Du nimmst das Stofftier an dich.")
                time.sleep(1)
                print("Sehr süß")
                time.sleep(1)
                mStoffKuscheltier.remove('Rotauge')
                mStoffKuscheltier.append('Meins')
                print("Du verlässt den Raum")
                time.sleep(1)
                mannschaftsquartiereFlur3(environment)
            elif cmd == '2':
                time.sleep(1)
                print("Du lässt es lieber liegen.")
                time.sleep(1)
                print("Du bist viel zu männlich um Kuscheltiere mitzunehmen")
                time.sleep(1)
                mannschaftsquartiereFlur3(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iRotAuge3S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iRotAuge3HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge3HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge3HP[0] #
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge3S < mHP: #
                iRotAuge3LP[0] = iRotAuge3LP[0] + iRotAuge3S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iRotAuge3HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge3HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge3HP[0] #
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du flüchtest!")
        time.sleep(1)
        print("Du schließt die Tür hinter dir...")
        time.sleep(1)
        print("..Dein Gegner bekommt die Tür nicht auf.")
        time.sleep(1)
        mannschaftsquartiereFlur3(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iRotAuge3LP >= [15]: #
            print("Dein Gegner ist noch top fit!")
            kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge3LP >= [8]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge3LP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
    
def kampfRotAuge4(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge4LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            print("Du siehst, das der Gegner etwas in seiner Jacke hatte...")
            time.sleep(1)
            print("Es ist ein Medikit!")
            time.sleep(1)
            print("Du benutzt es gleich")
            mLP[0] = mLP[0] + 25
            time.sleep(1)
            waffenkammerFlur(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iRotAuge4S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iRotAuge4HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge4HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge4HP[0] #
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge4S < mHP: #
                iRotAuge4LP[0] = iRotAuge4LP[0] + iRotAuge4S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iRotAuge4HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge4HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge4HP[0] #
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du flüchtest!")
        time.sleep(1)
        hauptzentrale(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iRotAuge4LP >= [10]: #
            print("Dein Gegner ist noch top fit!")
            kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge4LP >= [5]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge4LP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN    
    
def kampfRotAuge5(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge5LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            laborFlur(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iRotAuge5S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iRotAuge5HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge5HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge5HP[0] #
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge5S < mHP: #
                iRotAuge5LP[0] = iRotAuge5LP[0] + iRotAuge5S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iRotAuge5HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge5HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge5HP[0] #
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du flüchtest!")
        time.sleep(1)
        hauptzentrale(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iRotAuge5LP >= [10]: #
            print("Dein Gegner ist noch top fit!")
            kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge5LP >= [5]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge5LP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
            
def kampfRotAuge6(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['a', 'angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge6LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            print("Du siehst, das der Gegner etwas in seiner Jacke hatte...")
            time.sleep(1)
            print("Es ist ein Medikit!")
            time.sleep(1)
            print("Du benutzt es gleich")
            mLP[0] = mLP[0] + 25
            time.sleep(1)
            medAbteilungFlur(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iRotAuge6S >= mHP: #
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iRotAuge6HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge6HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge6HP[0] #
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge6S < mHP: #
                iRotAuge6LP[0] = iRotAuge6LP[0] + iRotAuge6S[0] - mHP[0] #
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iRotAuge6HP: #
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge6HP: #
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge6HP[0] #
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du flüchtest!")
        time.sleep(1)
        hauptzentrale(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iRotAuge6LP >= [10]: #
            print("Dein Gegner ist noch top fit!")
            kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge6LP >= [5]: #
            print("Dein Gegner macht langsam schlapp!")
            kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge6LP >= [0]: #
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
            
# Ende

def endingDeath(environment):
    time.sleep(1)
    print("Du bist gestorben")
    time.sleep(1.5)
    print("Spiel wird beendet")
    exit(0)
    
def endeKeineFluchtkapsel(environment):
    time.sleep(0.5)
    print("Du betritts den Raum.")
    time.sleep(1)
    print("Narrez ist mit der Fluchtkapsel ganz alleine abgehauen!")
    time.sleep(1.5)
    print("Es gibt keine andere Möglichkeit aus dem Raumschiff zu entkommen.")
    time.sleep(2)
    print("GAME OVER")
    time.sleep(3)
    exit()
           
def dieFlucht(environment):
    time.sleep(0.5)
    print("Du öffnest die Fluchtkapsel und steigst hinein.")
    if iBewFrau[0] == 'Traurig':
        time.sleep(1.5)
        print("Kurz bevor du den Startvorgang einleitest, hörst du Schritte außerhalb der Kapsel.")
        time.sleep(1.5)
        print("'Nimm mich mit', ertönt eine dir bekannte Stimme.")
        time.sleep(1.5)
        print("Eine Person steht vor der Fluchtkapsel")
        time.sleep(1.5)
        print("Es handelt sich um die Frau aus der Waffenkammer.")
        time.sleep(1.5)
        print("'Bitte nimm mich mit, ich will hier nicht sterben!'")
        time.sleep(1.5)
        print("Du nickst ihr zu, sie bedankt sich und steigt zu dir in die Kapsel.")
        time.sleep(1.5)
        print("'Mein Name ist übrigens Izzin, wie lautet deiner?'")
        time.sleep(1.5)
        iWulffLuck.append(randint(1,2))
        if iWulffHP[0] >= 0 and iWulffLuck[0] == 1:
            print("Plötzlich fängt jemand an zu schreien!")
            time.sleep(1.5)                
            print("'Habt ihr noch nen Platz frei!', brüllt jemand laut von draußen.")
            time.sleep(1.5)
            print("Im nächsten Moment springt die Wache Wulff in die Fluchtkapsel")
            time.sleep(1.5)
            print("'Habt ihr noch nen Platz für mich frei?! Das ganze hier wurd mir zuviel!")
            time.sleep(1.5)
            print(" Wie heißt'n du eigenltich, Kleiner?")
            time.sleep(1.5) 
            print("")
            print("Plötzlich kommt dir die Erinnerung an deine Vergangenheit wieder...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("''Mein Name lautet Mex...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("  und ich bin für dieses Chaos verantwortlich.")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("Du aktivierst den Startvorgang und die Kapsel wird in den Weltraum geschossen.")
            time.sleep(1.5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!HERZLICHEN GLÜCKWUNSCH!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       Sie haben das Spiel erfolgreich beendet!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n             Viel Spaß beim nächsten mal!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            exit()
        else:
            print("Plötzlich kommt dir die Erinnerung an deine Vergangenheit wieder...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("''Mein Name lautet Mex...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("  und ich bin für dieses Chaos verantwortlich.")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("Du aktivierst den Startvorgang und die Kapsel wird in den Weltraum geschossen.")
            time.sleep(1.5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!HERZLICHEN GLÜCKWUNSCH!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       Sie haben das Spiel erfolgreich beendet!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n             Viel Spaß beim nächsten mal!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            exit()
    else:
        print("Auf einmal hörst du mehrere Schritte von draußen.")
        time.sleep(1.5)
        print("Merana und ihre zwei Wachen stehen vor dir.")
        time.sleep(1.5)
        print("'Ich erbitte um Einlass in diese Fluchtkapsel, damit meine Männer und ich wieder unsere Heimat")
        time.sleep(1.5)
        print(" sehen können. Wären sie so nett uns mitzunehmen?'")
        time.sleep(1.5)
        print("Die zwei Wachen sind währenddessen schon längst in die Kapsel eingestiegen und haben Platz")
        print("für ihre Begleitung geschaffen.")
        time.sleep(1.5)
        print("'Wie lautet denn der Name unseres Retters?'")
        time.sleep(1.5)
        if iWulffHP[0] >= 0:
            print("Draußen fängt jemand an zu schreien.")
            time.sleep(1.5)
            print("'Vergisst mich nicht!', brüllt jemand laut von draußen.")
            time.sleep(1.5)
            print("Im nächsten moment ist die Wache Wulff in die Fluchtkapsel gesprungen.")
            time.sleep(1.5)
            print("'Ihr hättet mich fasst vergessen?! Bei wem soll ich mich dafür bedanken, mh?'")
            time.sleep(1.5)
            print("Plötzlich kommt dir die Erinnerung an deine Vergangenheit wieder...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("''Mein Name lautet Mex...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("  und ich bin für dieses Chaos verantwortlich.")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("Du aktivierst den Startvorgang und die Kapsel wird in den Weltraum geschossen.")
            time.sleep(1.5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!HERZLICHEN GLÜCKWUNSCH!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       Sie haben das Spiel erfolgreich beendet!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n             Viel Spaß beim nächsten mal!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            exit()
        else:
            print("Plötzlich kommt dir die Erinnerung an deine Vergangenheit wieder...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("''Mein Name lautet Mex...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("  und ich bin für dieses Chaos verantwortlich.")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("Du aktivierst den Startvorgang und die Kapsel wird in den Weltraum geschossen.")
            time.sleep(1.5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!HERZLICHEN GLÜCKWUNSCH!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       Sie haben das Spiel erfolgreich beendet!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n             Viel Spaß beim nächsten mal!!!\n")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            exit()       
        
# Haupteingaben
        
def getcmd(cmdlist):
    
    cmd = input('\nEingabe: ')
    cmd = cmd.lower() # Eingegebene Großbuchstaben werden klein
    
    if cmd in cmdlist:
        return cmd
    
    elif cmd == 'hilfe' or cmd == 'eingabeoptionen':
        print("\nFolgende Eingaben sind an den richtigen Stellen anwendbar:")
        print("\n-----------------------------------------------------------------------------------")
        print("                           Normales Menü     ")
        print()
        print("umsehen                        -> Du siehst dich im Raum um")
        print("benutze 'Objekt'               -> nutzt ein nutzbares Objekt")
        print("gehe zu 'Objekt/Person'        -> gehe zu einem Objekt, einer Person")
        print("öffne 'Objekt'                 -> öffnet ein Objekt, falls es offen ist, oder")
        print("                                  du den benötigten Schlüssel hast/ das benötigte")
        print("                                  Passwort weißt")
        print("untersuche 'Objekt/Person'     -> untersucht ein Objekt, eine Person")
        print("nehme 'Objekt'                 -> nehme besagtes Objekt, dadurch wandert es ins")
        print("                                  Inventar oder in deinen Waffenslot, falls dieser")
        print("                                  leer ist")
        print("rede mit 'Person'              -> Mann, Frau oder Name eingeben, um mit der Person zu reden")
        print("lege Waffe ab                  -> leert den Waffenslot, eine neue waffe kann")
        print("                                  nun ausgerüstet werden")
        print("status                         -> zeigt dir deinen Gesundheitsstatus an")
        print("ziehe Kleidung aus             -> ziehe deine derzeitige Ausrüstung aus")
        print("ziehe 'Kleidung/Ausrüstung' an -> ziehe Ausrüstung an, du musst angelegte Ausrüstung")
        print("                               -> vorher ausziehen")
        print()
        print("Nicht immer sind alle Eingaben nutzbar, also nicht verzweifeln, falls mal eine Eingabe")
        print("nicht funktionieren sollte. Meist sind GROßGESCHRIEBENE Wörter in irgendeiner Weise nutzbar")
        print("\n-----------------------------------------------------------------------------------")
        print()
        print("                 Kampf Menü        ")
        print()
        print("                 angreifen       -> greift an")
        print("                 flüchten        -> flüchtet vor Gegner, falls möglich")
        print("                 status gegner   -> zeigt den Zustand des Gegners an")
        print("\n-----------------------------------------------------------------------------------")
        print()
        print("                 Auswahl Menü")
        print()
        print("                 1")
        print("                 2")
        print("                 3")
        print("...")
        print("An manchen Stellen des Spiels musst du eine Entscheidung treffen, hier hast du nur")
        print("eine begrenzte Auswahlmöglichkeit, die mit einer reinen Zahleneingabe funktioniert.")
        print("Außerdem wird diese Funktion die Fortbewegung nach dem Beginn des Spiels erleichtern.")
        print("\n-----------------------------------------------------------------------------------")
        
        return getcmd(cmdlist)
    
    elif cmd == 'status':
        if mLP >= [100]:
            print("Du hast volle Energie!!!")
            print("Du hast noch: {} Lebenspunkte".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [80]:
            print("Du hast ein paar Kratzer abbekommen!!")
            print("Du hast noch: {} Lebenspunkte".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [60]:
            print("Du bist leicht verletzt!")
            print("Du hast noch: {} Lebenspunkte".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [40]:
            print("Du bist verletzt, suche dir Hilfe.")
            print("Du hast noch: {} Lebenspunkte".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [20]:
            print("Kritischer Zustand!!!")
            print("Lange hälst du das nicht mehr aus")
            print("Du hast noch: {} Lebenspunkte".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [0]:
            print("Zu viele Verletzungen...")
            print("Wenn du langsam nichts tust, wirst du nicht mehr lange durchhalten...")
            print("Du hast noch: {} Lebenspunkte".format(mLP))
            return getcmd(cmdlist)
        elif mLP <= [0]:
            print("Noch ein Treffer, dann bist du tot!")
            return getcmd(cmdlist)
            
    elif cmd == 'ziehe kleidung aus':
    
        if 'Unterhose' in mAus:
            print("''Warum sollte ich meine Unterhose ausziehen!?...")
            print("  Die lasse ich schön an!...''")
            return getcmd(cmdlist)
        elif 'Gefangenenoverall' in mAus:
            print("Beim Ausziehen des Overalls ist ein Riss entstanden...")
            print("Gegenstand nicht mehr nutzbar.")
            mAus.remove('Gefangenenoverall')
            mAus.append('Unterhose')
            mG.append('Gefangenenoverall')
            mS.remove(2)
            mS.append(1)
            return getcmd(cmdlist)
        elif 'Technikeroverall' in mAus:
            print("Beim Ausziehen des Overalls ist ein Riss entstanden...")
            print("Gegenstand nicht mehr nutzbar.")
            mAus.remove('Technikeroverall')
            mAus.append('Unterhose')
            mG3.append('Technikeroverall')
            mS.remove(4)
            mS.append(1)
            return getcmd(cmdlist)
        elif 'Panzerung' in mAus:
            print("Beim Ausziehen des Overalls ist ein Riss entstanden...")
            print("Gegenstand nicht mehr nutzbar.")
            mAus.remove('Panzerung')
            mAus.append('Unterhose')
            mG5.append('Panzerung')
            mS.remove(10)
            mS.append(1)
            return getcmd(cmdlist)
        elif 'Monsterjäger' in mAus:
            print("Beim Ausziehen der Rüstung ist eine Delle entstanden...")
            print("In diese Rüstung kommst du nicht mehr rein.")
            mAus.remove('Monsterjäger')
            mAus.append('Unterhose')
            mG5.append('Monsterjäger')
            mS.remove(13)
            mS.append(1)
            return getcmd(cmdlist)
        
    elif cmd == 'lege waffe ab':
        
        if 'Faust' in mW:
            print("Zur Zeit hast du keine Waffen, nur deine Faust.")
            print("Willst du deine Faust ausreißen?!")
            print("Bist du wahnsinnig?!")
            return getcmd(cmdlist)
        elif 'Jonas Laserkanone' in mW:
            print("Beim Ablegen zerspringt Jonas Laserkanone in")
            print("tausend Einzelteile...")
            print("Wie willst du das nur Jonas erklären...")
            mW.remove('Jonas Laserkanone')
            mW.append('Faust')
            mG2.append('Jonas Laserkanone')
            mHP.remove(10)
            mHP.append(3)
            return getcmd(cmdlist)
        elif 'Rohr' in mW:
            print("Beim Ablegen zerbricht das Rohr entzwei...")
            print("Da muss wohl ein Klempner dran um das Ding zu reparieren...")
            mW.remove('Rohr')
            mW.append('Faust')
            mG4.append('Rohr')
            mHP.remove(7)
            mHP.append(3)
            return getcmd(cmdlist)
        elif 'Monsterhunter' in mW:
            print("Beim Ablegen geht der Monsterhunter kaputt...")
            print("Das wars wohl mit der Monsterjagt...")
            mW.remove('Monsterhunter')
            mW.append('Faust')
            mG6.append('Monsterhunter')
            mHP.remove(30)
            mHP.append(3)
            return getcmd(cmdlist)
        elif 'Laserschwert' in mW:
            print("Beim Ablegen geht dir das Schwert kaputt...")
            print("Möge die Macht mit dir sein...")
            mW.remove('Laserschwert')
            mW.append('Faust')
            mG7.append('Laserschwert')
            mHP.remove(15)
            mHP.append(3)
            return getcmd(cmdlist)
        
            
        
    elif cmd == 'quit':
        print("    Du hast das Spiel beendet")
        time.sleep(1)
        print("(1) play again")
        print("(2) quit")
    
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            print("Spiel wird neu gestartet")
            print("...")
            print("FEHLER AUGETRETEN")
            print("SPIEL WIRD BEENDET")
            exit()
        
        
        elif cmd== '2':
            print("Spiel wird beendet")
            exit()
            
    
    else:
        time.sleep(0.2)
        print("\n...")
        time.sleep(0.2)
        print('Das kannst du hier nicht tun')
        time.sleep(0.2)
        print('...')
        time.sleep(0.2)
        print("Falls du mal nicht weiter weißt,")
        print("gebe 'hilfe' ein, um Eingabemöglichkeiten")
        print("zu erhalten.")
        print()
        time.sleep(0.2)
        print("Außerdem sind GROßGESCHRIEBENE Worte meist")
        print('auf irgendeiner Weise nutzbar, wenn sie nach')
        print("der Eingabe 'umsehen' angezeigt werden.")
        time.sleep(0.2)
        
        return getcmd(cmdlist)
    

if __name__ == "__main__":
    environment = ['service port']
    startBildschirm(environment)