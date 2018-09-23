'''
Created on 12.09.2018

@author: michaelgress
'''

# Einführung


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

# Kryokammer

def kryokammer(environment):
    
    cmdlist = ['umsehen', 'untersuche hauptrechner', 'gehe zu hauptrechner', 'gehe zu tür', 'untersuche kryokapsel',]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        print("Du siehst dich etwas genauer um.")
        print("So wie es scheint, befindest du dich in einer Kryokammer.")
        print("Viele Kryokapseln umgeben dich, die Tür ist geschlossen.")
        print("eine der Kryokapseln ist geöffnet und zwar die, vor der du Bewusstlos lagst.")
        print("Ein Hauptrechner befindet sich an der gegenüberliegenden Seite der Tür.")
        kryokammer(environment)
        
    elif cmd == 'untersuche hauptrechner':
        print('Der Hauptrechner steht zu weit weg um untersucht zu werden.')
        kryokammer(environment)
        
    elif cmd == 'gehe zu hauptrechner':
        print('Du stehst nun vor dem Hauptrechner.')
        hauptrechner(environment)
        
    elif cmd == 'gehe zu tür':
        print('Du stehst vor der Tür.')
        kryokammer(environment)
        
    elif cmd == 'untersuche kryokapsel':
        print('beschädigt')
        kryokammer(environment)    
        
        
        
        
        
def hauptrechner(environment):
    
    cmdlist = ['benutze hauptrechner', 'quit',]
    cmd = getcmd(cmdlist)
    
    if cmd == 'benutze hauptrechner':
        print('Der Hauptrechner ist Passwort geschützt.')
        print('Passwort eingeben?')
        
        hauptrechner(environment)
        
    elif cmd == 'quit':
        kryokammer(environment)
        
    else:
        print('???')
        hauptrechner(environment)
      
      
        
        
# Haupteingaben
        
def getcmd(cmdlist):
    
    cmd = input('\nWas tust du: ')
    cmd = cmd.lower() # Eingegebene Großbuchstaben werden klein
    
    if cmd in cmdlist:
        return cmd
    
    elif cmd == 'hilfe':
        print("\n---------------------")
        print("- umsehen")
        print("- nutze 'Objekt/Person'")
        print("- gehe zu 'Objekt/Person'")
        print("- öffne 'Objekt'")
        print("- untersuche 'Gegenstand'")
        print("---------------------")
        return getcmd(cmdlist)
    
    else:
        print('\nDas kannst du hier nicht tun!!!')
        return getcmd(cmdlist)
    
if __name__ == "__main__":
    environment = ['service port']
    kryokammer(environment)