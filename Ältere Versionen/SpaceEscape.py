'''
Created on 11.09.2018

@author: michaelgress
'''

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

def start(kryokammer):
    
    print("hier?")
    
    cmdlist = ['hilfe', 'umsehen', 'gehe zu Computer', 'nutze Computer', 'gehe zu Tür', ]
    cmd = getcmd(cmdlist)
    if cmd == 'umsehen':
        print("Du siehst dich etwas genauer um.")
        print("SO wie es scheint, befindest du dich in einer Kryokammer.")
        print("Viele Kryokapseln umgeben dich, die Tür ist geschlossen.")
        print("eine der Kryokapseln ist geöffnet und zwar die, vor der du Bewusstlos lagst.")
        start(kryokammer)
        
def getcmd(cmdlist):
    cmd = input('\nWas tust du: ')
    if cmd in cmdlist:
        return cmd
    elif cmd == 'hilfe':
        print("---------------------")
        print("- umsehen")
        print("- nutze 'Objekt/Person'-")
        print("- gehe zu 'Objekt/Person'")
        print("- öffne 'Objekt'")
        print("---------------------")
        return getcmd(cmdlist)
    else:
        print('\nDas ist eine schlechte Idee')
        return getcmd(cmdlist)
    
if __name__ == "__main__":
    inventory = ['service port']
    start(inventory) #für start (Räume)