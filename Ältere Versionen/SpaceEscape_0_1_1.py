'''
Created on 17.09.2018

@author: michaelgress
'''

import time
from random import randint
from _dummy_thread import exit

# Spieler
mLP = [90] # myLebenspunbkte, Lebenspunkte des Spielers
mW = ['Faust'] # Ausgerüstete Waffe
mHP = [3] # ausgeübter Schaden
mI = [] # Inventar
mAus = ["Unterhose"] # Kleidung, Rüstung
mS = [1] # Schutz der Kleidung
mG = [] #Zerstörte Gegenstände, Muell

# Dauerhafte Schäden

mLippeAb = []

# NPC

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




# Einführung-------------------------------------------------
print("PROUDLYPRESENTINGGAMES proudly presents")
time.sleep(2)
print("a HAEFEM gamestudio gamy game")
time.sleep(2)
print("in cooperation with PYTHONKURSFU+00FCREINSTEIGER animation studios")

def startBildschirm(environment):
    time.sleep(2)
    print("---------------------------------------------------------\n")
    time.sleep(0.1)
    print("  Entkomme aus dem Raumschiff und geh dabei nicht drauf  ")
    time.sleep(0.1)
    print("\n---------------------------------------------------------\n")
    time.sleep(2)
    print("                            play")
    time.sleep(0.2)
    print("                            help")
    time.sleep(0.2)
    print("                            quit")
    time.sleep(0.2)
    
    cmdlist = ['play', 'quit', 'help']
    cmd = getcmd(cmdlist)
    
    if cmd == 'play':
        time.sleep(1)
        print("Spiel wird gestartet")
        time.sleep(1)
        intro(environment)
    elif cmd == 'quit':
        time.sleep(1)
        print("Spiel wird beendet")
        time.sleep(1)
        exit
    elif cmd == 'help':
        time.sleep(1)
        print("Falls du während dem Spiel Probleme bekommst, gebe 'hilfe' ein, um")
        print("Möglichkeiten der Eingabe zu erhalten.")
        time.sleep(5)
        print()
        print()
        startBildschirm(environment)
        
    
def intro(environment):    
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
    kryokammer(environment)



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
               'ziehe overall an',
               'skip'
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        print("Du siehst dich etwas genauer in dem verdunkeltem Raum um.")
        print("So wie es scheint, befindest du dich in einer kleineren Kryokammer.")
        print("Der Raum ist spartanisch eingerichtet, drei Kryokapseln liegen auf")
        print("der gegenüberliegenden Seite des einzigen Ausgangs des Raumes.")
        print("Eine der Kryokapseln ist geöffnet, die anderen zwei sind verschlossen.")
        print("An jedes der Kryokapseln ist ein Informationsterminal angeschlossen.")
        if 'GefangenenOverall' in mAus or 'GefangenenOverall' in mG:
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
        
    elif cmd == 'ziehe kleidung an' or cmd == 'ziehe gefangenenoverall an' or cmd == 'ziehe overall an':
        if 'Gefangenenoverall' in mAus or 'Gefangenenoverall' in mG:
            print("Du hattest den Gefangenenoverall bereits angezogen...")
            print("Hier liegt keiner mehr.")
            kryokammer(environment)
        else:
            print("Du ziehst den Gefangenenoverall an")
            print("Er ist recht unbequem und bietet wenig Schutz")
            print("'Immerhin besser als in Unterhosen rumzulaufen")
            mAus.remove('Unterhose')
            mAus.append('Gefangenenoverall')
            mS.remove(1)
            mS.append(2)
            kryokammer(environment)
            
    elif cmd == 'skip':
        narrezGespräch(environment) 
                
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
        print("Du entscheidest dich für den linken Weg")
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
        
        cmdlist = ['1', '2', 'greife an', 'angreifen']
        cmd = getcmd(cmdlist)
        
        if cmd == '1' or cmd == 'greife an' or cmd == 'angreifen':
            kampf1FlurSüdRechts(environment)
            
        elif cmd == '2':
            print("Als du mit dem Wesen reden willst, greift es dich an.")
            mLP[0] = mLP[0] - 7
            kampf1FlurSüdRechts(environment)
        
    elif cmd == '2':
        print("Du entscheidest dich doch lieber für den anderen Weg...")
        flurSüdLinks(environment)
        
    elif cmd == 'umsehen':
        print("Als du dich etwas genauer umschaust, entdeckst du am Ende des Weges")
        print("eine Kamera. Sie scheint aktiv zu sein.")
        flurSüdRechts(environment)
        
        
def flurSüdRechtsGeschlossen(environment):
    time.sleep(1)
    print("Du befindest dich im Flur.")
    
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
        print("Du siehst dich im Raum um.")
        print("Die zwei LEICHEN der seltsamen Wesen liegen auf dem Boden.")
        print("Eine ÜBERWACHUNGSKAMERA ist direkt auf dich gerichtet, sie hängt")
        print("über dem einzigen AUSGANG am Ende des Ganges. Sie scheint aktiv zu sein.")
        print("Zwei der vier TÜREN an den Seiten sind geöffnet, vermutlich kamen")
        print("aus diesen die Angreifer heraus.")
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'untersuche wesen' or cmd == 'untersuche leiche' or cmd == 'untersuche leichen' or cmd == 'untersuche gegner':
        print("Die zwei Leichen tragen die selben Overalls wie die Zwei in den")
        if mAus == 'Gefangenenoverall':
            print("Kryokapseln und wie ich momentan.")
            print("Sie atmen nicht mehr und zeigen keine Spur von Leben.")
            print("Die Gesichter sind bleich, ihre Augen vollkommen rot.")
            print("Keiner der beiden hat etwas interessantes bei sich.")
            flurSüdRechtsGeschlossen(environment)
        else:
            print("Kryokapseln. Sie atmen nicht mehr und zeigen keine Spur von Leben.")
            print("Die Gesichter sind bleich, ihre Augen vollkommen rot.")
            print("Keiner der beiden hat etwas interessantes bei sich.")
            flurSüdRechtsGeschlossen(environment)
            
    elif cmd == 'untersuche tür' or cmd == 'untersuche türen':
        print("Die zwei verschlossenen Türen lassen sich nicht öffnen.")
        print("Hinter den zwei offenen Türen befinden sich spärlich eingerichtete Räume.")
        print("Der Raum ist ausgestattet mit einer Toilette und einem hartes Bett.")
        print("Mehr findest du nicht.")
        flurSüdRechtsGeschlossen(environment)
    
    elif cmd == 'öffne tür' or cmd == 'öffne türen':
        print("Zwei der Türen können nicht geöffnet werden.")
        print("Die anderen sind offen.")
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'untersuche kamera' or cmd == 'untersuche überwachungskamera':
        print("Du gehst zur Kamera.")
        print("Sie bleibt starr und du erkennst, dass sie abgeschaltet ist.")
        print("Die Kamera hängt zu hoch, um sie zu berühren.")
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'untersuche ausgang' or cmd == 'öffne ausgang':
        print("Als du dich direkt vor den Ausgang stellst, öffnet sich die Schleuse.")
        print("(1) Gehe hindurch")
        print("(2) Raum weiter untersuchen")
        
        cmdlist =['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(1)
            print("Du gehst in den Raum...")
            time.sleep(3)
            narrezGespräch(environment)
        
        elif cmd == '2':
            time.sleep(1)
            print("Du siehst dich noch etwas in dem Raum um.")
            time.sleep(1)
            flurSüdRechtsGeschlossen(environment)
        
            

    
def flurSüdLinks(environment):
    print('Ein Gefühl sagt dir, der linke Weg wird der Richtige sein.')
    print("An der Biegung angekommen, nimmst du Geräusche von weiter weg war.")
    print("Du schaust vorsichtig um die Ecke...")
    print("Du erblickst den Rücken einer auf den Knien sitzenden Person.")
    print("Sie bewegt sich, vor ihr scheint etwas zu liegen, was sie beschäftigt.")
    print("(1) Zur Person gehen")
    print("(2) Den anderen Weg nehmen")
    
    cmdlist = ['1', '2', 'umsehen']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("Du entscheidest dich dafür nachzuschauen, was da hinten los ist.")
        print("Bei der Person angekommen, schließt sich hinter dir eine Notschleuse.")
        print("Du drehst dich um und bist erstmal verwundert.")
        print("Als du dich wieder umdrehst, packt dich die Person, oder besser gesagt, das 'Etwas', an den Schultern...")
        print("Das Etwas ist an Mund, Backen und Stirn mit Blut befleckt.")
        print("Es reißt sein Maul auf und versucht dich zu beißen.")
        print("(1) Angreifen")
        print("(2) Dem Angreifer in einem vernünftigen Gespräch bitten es zu unterlassen, dich auffressen zu wollen")
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("Du greifst an!")
            kampfFlurSüdLinks(environment)
            
        elif cmd == '2':
            print("Bevor du das Etwas mit deinen Argumenten angreifen kannst, beißt es dir ein Teil deiner Lippe ab.")
            mLippeAb.append(1)
            mLP[0] = mLP[0] - 12
            kampfFlurSüdLinks(environment)
    
    elif cmd == '2':
        print("Du entscheidest dich doch lieber für den anderen Weg...")
        flurSüdRechts(environment)
    
    elif cmd == 'umsehen':
        print("Als du dich etwas genauer umschaust, entdeckst du am Ende des Weges")
        print("eine Kamera. Sie scheint aktiv zu sein.")
        flurSüdLinks(environment)

def flurSüdLinksGeschlossen(environment):
    time.sleep(1)
    print("Du befindest dich im Flur.")    
    
    cmdlist = ['umsehen',
               'untersuche leichen',
               'öffne tür',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        print("")
        flurSüdLinksGeschlossen(environment)
    
    elif cmd == 'untersuche leichen':
        print("")
        print("Hier Waffe einfügen")
        flurSüdLinksGeschlossen(environment)
        
    elif cmd == 'öffne tür':
        print("tür geöffnet")
        narrezGespräch(environment)
        

    
        


# Gespräche

def narrezGespräch(environment):
    print("Als du den Raum betrittst, zielt ein Mann mit einem Blaster auf dich.")
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
        print("'Das ließe sich einrichten, wenn du für mich was erledigst'")
        print("(1) Zustimmen")
        print("(2) Ablehnen")
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("'Wunderbar!")
            print("Er nimmt die Waffe runter")
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
    print(" Einer muss runter ins Maschinendeck gehen und von dort aus den Generator für dieses")
    print(" Stockwerk neu starten. Und dieser Glückliche bist du.")
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
        print("'Beeil dich, ich hab nich den ganzen Tag Zeit.'")
        print("Er wendet sich wieder einem großen Rechner zu, der mittig im Raum platziert ist.")
        gefangenentraktZentrale(environment)
        
    elif cmd == '2' or cmd == '3':
        print("'Schade. Dabei lief es doch gerade so gut mit uns beiden.")
        print("Ein Schuss fällt, du kippst tot um...")
        print("GAME OVER")
        exit
        
def gefangenentraktZentrale(environment):
    exit
    
    
        
        
    
        
        
# Kämpfe

def kampf1FlurSüdRechts(environment): #HIER ENVIRONMENT ÄNDERN
    print("Es wird gekämpft!")
    cmdlist = ['angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            EndingDeath(environment)    
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
    cmdlist = ['angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner']
    cmd = getcmd(cmdlist)
    if cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            EndingDeath(environment)    
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
    cmdlist = ['angreifen', 'greife an', 'greif an', 'greife gegner an','greif gegner an', 'flüchten', 'status gegner',]
    cmd = getcmd(cmdlist)
    if cmd == 'angreifen' or cmd == 'greife an' or cmd == 'greif an' or cmd == 'greife gegner an' or cmd == 'greif gegner an':
        if mLP[0] <= 0:
            time.sleep(1)
            print("Du bist zu schwach für einen weiteren Angriff...")
            time.sleep(1)
            print("Der Gegner kommt auf dich zu...")
            time.sleep(1)
            print("...Dir wird schwarz vor Augen...")
            time.sleep(1)
            EndingDeath(environment)    
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
    
        
    
# Ende

def EndingDeath(environment):
    print("Du bist gestorben")
    print("Spiel wird beendet")
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
        print("lege Waffe ab                  -> leert den Waffenslot, eine neue waffe kann")
        print("                                  nun ausgerüstet werden")
        print("status                         -> zeigt dir deinen Gesundheitsstatus an")
        print("siehe Inventar                 -> zeigt dir die Gegenstände in deinem Inventar an")
        print("ziehe Kleidung aus             -> ziehe deine derzeitige Ausrüstung aus")
        print("ziehe 'Kleidung/Ausrüstung' an -> ziehe Ausrüstung an, du musst angelegte Ausrüstung")
        print("                               -> vorher ausziehen")
        print()
        print("Nicht immer sind alle Eingaben nutzbar, also nicht verzweifeln, falls mal eine Eingabe")
        print("Nicht funktionieren sollte.")
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
        print("eine begrenzte Auswahlmöglichkeit, die mit einer reinen Zahleneingabe funktioniert")
        print("\n-----------------------------------------------------------------------------------")
        
        return getcmd(cmdlist)
    
    elif cmd == 'status':
        if mLP == [100]:
            print("Du hast volle Energie!!!")
            return getcmd(cmdlist)
        elif mLP >= [80]:
            print("Du hast ein paar Kratzer abbekommen!!")
            return getcmd(cmdlist)
        elif mLP >= [60]:
            print("Du bist leicht verletzt!")
            return getcmd(cmdlist)
        elif mLP >= [40]:
            print("Du bist verletzt, suche dir Hilfe.")
            return getcmd(cmdlist)
        elif mLP >= [20]:
            print("Kritischer Zustand!!!")
            print("Lange hälst du das nicht mehr aus")
            return getcmd(cmdlist)
        elif mLP >= [0]:
            print("Zu viele Verletzungen...")
            print("Wenn du langsam nichts tust, wirst du nicht mehr lange durchhalten...")
            return getcmd(cmdlist)
    
    elif cmd == 'siehe inventar':
        for x in mI:
            print(x)
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
        
    elif cmd == 'lege waffe ab':
        
        if 'Faust' in mW:
            print("Zur Zeit hast du keine Waffen, nur deine Faust.")
            print("Willst du deine Faust rausreißen?!")
            print("Bist du wahnsinnig?!")
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
            intro(environment)
        
        
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
        return getcmd(cmdlist)
    

if __name__ == "__main__":
    environment = ['service port']
    startBildschirm(environment)