'''
Created on 13.09.2018

@author: michaelgress
'''

# Einführung-------------------------------------------------

import time

print('-----------------------')
print('\n        Escace')
print("\n-----------------------")
print("...")
print("Du erwachst.")
print("Nach einigen Sekunden der Gefühlslosigkeit und Desorientierung")
print("übernimmt ein pochender Schmerz an deinem Kopf deine Aufmerksamkeit.")
print("Du fässt an deinen Kopf...")
print("Als du deine Hand herunter nimmst klebt Blut an deinen Fingern.")
print("...")
print("Du versuchst dich daran zu erinnern, was als letztes geschehen ist,")
print("jedoch kannst du dich an rein gar nichts mehr erinnern.")
print("blablabla, was tust du?")



def kryokammer(environment):
    
    cmdlist = ['umsehen', 'benutze terminal', 'gehe zu terminal', 'gehe zu informationsterminal', 'benutze informationsterminal', 'gehe zu tür', 'untersuche kryokapsel', 'benutze schalter']
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        print("Du siehst dich etwas genauer um.")
        print("So wie es scheint, befindest du dich in einer kleineren Kryokammer.")
        print("Drei Kryokapseln umgeben dich, eine Tür steht ihnen gegenüber.")
        print("Eine der Kryokapseln ist geöffnet und zwar die, vor der du aufgewacht bist.")
        print("An jedes der Kryokapseln ist ein Informationsterminal angeschlossen.")
        kryokammer(environment)
        
    elif cmd == 'gehe zu terminal':
        print('Vor dir sind drei Terminals.')
        terminal(environment)
    elif cmd == 'benutze terminal':
        print('Vor dir sind drei Terminals.')
        terminal(environment)                
    elif cmd == 'gehe zu informationsterminal':
        print('Vor dir sind drei Terminals.')
        terminal(environment)
    elif cmd == 'benutze informationsterminal':
        print('Vor dir sind drei Terminals.')
        terminal(environment)
            
    elif cmd == 'gehe zu tür':
        print('Du stehst vor der Tür.')
        print('Neben der Tür befindet sich ein Schalter für die Öffnung der Tür.')
        kryokammer(environment)
        
    elif cmd == 'benutze schalter':
        print('Ping\n----\n')
        print('Die Tür öffnet sich und grell blendendes Licht strahlt in den Raum.')
        print('Was möchtest du tun?\n')
        print('(1) Kryokammer weiter untersuchen?')
        print('(2) Kryokammer verlassen?')
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
            
        if cmd == '1':
            print("'Ich sollte mich lieber nochmal etwas genauer umsehen'")
            print("Die Tür schließt sich nach einigen Sekunden wieder.")
            kryokammer(environment)          
        elif cmd == '2':
            print('Du verlässt den Raum')
            print("bu betrittst einen langen Gang, hinter dir schließt sich die Tür")
            flurSüd(environment)
                 
    elif cmd == 'untersuche kryokapsel':
        print('beschädigt, vor der mittleren Blutspritzer')
        kryokammer(environment)
        
        
def terminal(environment):
    
    print('Welches der Terminals willst du benutzen?')
    print('(1) Terminal links')
    print('(2) Terminal mitte')
    print('(3) Terminal rechts')
    print('(4) Beende Bedienung')    
            
    cmdlist = ['1', '2', '3', '4',]
    cmd = getcmd(cmdlist)
            
    if cmd == '1':
        print('Beschreibung des Terminals, Bedienungsoptionen')
        terminal(environment)          
    elif cmd == '2':
        print('Beschreibung des Terminals, Bedienungsoptionen')
        terminal(environment)
    elif cmd == '3':
        print('Beschreibung des Terminals, Bedienungsoptionen')
        terminal(environment)
    elif cmd == '4':
        print('Du wendest dich den Terminals ab.')
        kryokammer(environment)



def flurSüd(environment):
    print("Du gehst den Gang entlang und kommst an eine Abzweigung")
    print("(1) Biege rechts ab")
    print("(2) Biege links ab")
    print("(3) Gehe zurück")
    
    cmdlist = ['1', '2', '3', 'umsehen',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("Du gehst nach rechts")
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
        print("20 m biegen die Wege in Richtung Norden.")
        


def flurSüdRechts(environment):
    print('schöner Flur')
    
    cmdlist = ['1',]
    cmd = getcmd(cmdlist)
    
    hauptzentrale(environment)
    
def flurSüdLinks(environment):
    print('hässlicher Flur')
    
    cmdlist = ['1',]
    cmd = getcmd(cmdlist)
    
    hauptzentrale(environment)
    
def hauptzentrale(environment):
    print("Hier ist noch ein Mann in Uniform, schlecht geschnitten")
    print("Er schaut dich schockiert an und hält seine Waffe auf dich gerichtet")
    print("Streitgespräch mit verschiedenen Optionen (auch Tod)")
    print("Er stellt sich als einen Techniker des Raumschiffes vor?")
    print("Er bittet dich, einige Aufgaben für ihn zu erledigen")
    print("Aufgabe: Notenergieversorgung aktivieren (Untere Decks, Maschinenraum)")
    print("Aufgabe: Freigabe zur Evakuierung einleiten (Kommandozentrale)")
    print("Optional: Waffe beschaffen (Waffenkammer)")
    print("Optional: Nach Überlebenden Ausschau halten")
    
    cmdlist = ['1',]
    cmd = getcmd(cmdlist)
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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