'''
Created on 17.09.2018

@author: michaelgress
'''

from random import randint
myWaffe = ['Faust']
mW = myWaffe
mySchaden = [3]
mS = mySchaden
myLebenspunkte = [100]
mLP = myLebenspunkte
myInventar = []
mI = myInventar
myAusrüstung = ["unterhose"]
mA = myAusrüstung 
mySchutz = [1]
mSch = mySchutz
myZerstörteWaffen = []
mZW = myZerstörteWaffen

itGegnerLebenspunkte = [20]
itGegnerSchaden = [5]
itGegnerSchutz = [2]
itGegnerDifferenz = [0]


def room1(environment):

    cmdlist = ['umsehen', 'nimm laserknarre', 'nimm messer', 'zeige waffe', 'nächster raum']
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        if 'Laserknarre' in myWaffe:
            print("du hast die knarre bereits genommen")
            room1(environment)
        
        elif 'messer' in myWaffe:
            print("du hast das messer bereits genommen")
            room1(environment)
            
        else:
            print("du siehst die knarre und ein messer")
            room1(environment)
        
    elif cmd == "nimm laserknarre":
        if 'Laserknarre' in myWaffe:
            print("Du hast die Knarre bereits genommen")
            room1(environment)
            
        elif 'messer' in myWaffe:
            print("Du kannst nicht zwei Waffen auf einmal nehmen")
            room1(environment)
            
        else:
            print('du nimmst die Knarre')
            myWaffe.remove('Faust')
            myWaffe.append('Laserknarre')
            mySchaden.remove(3)
            mySchaden.append(6)
            room1(environment)
            
    elif cmd == "nimm messer":
        if 'messer' in myWaffe or 'messer' in myZerstörteWaffen:
            print("Du hast das Messer bereits genommen")
            room1(environment)
            
        elif 'Laserknarre' in myWaffe:
            print("Du kannst nicht zwei Waffen auf einmal nehmen")
            room1(environment)
            
        else:
            print('du nimmst das Messer')
            myWaffe.remove('Faust')
            myWaffe.append('messer')
            mySchaden.remove(3)
            mySchaden.append(5)
            room1(environment)
            
    elif cmd == 'zeige waffe':
        for x in myWaffe:
            print("Deine derzeit ausgerüstete Waffe lautet ", x)
            room1(environment)
            
    elif cmd == 'nächster raum':
        print("du gehst in den nächsten raum")
        ANGRIFF(environment)
        
def ANGRIFF(environment):
    print("Kampfmodus")
    cmdlist = ['greife an', 'flüchte', 'lebenspunkte']
    cmd = getcmd(cmdlist)
    if cmd == 'greife an':
        if myLebenspunkte[0] <= 0:
            print("Du bist zu schwach für einen weiteren Angriff...")
            print("Der Gegner kommt auf dich zu...")
            print("...Dir wird schwarz vor Augen...")
            Ending(environment)    
        elif itGegnerLebenspunkte[0] <= 0:
            print("du hast den Gegner besiegt")
            NÄCHSTERRAUM(environment)            
        else:
            print("du greifst an")
            if itGegnerSchutz >= mySchaden:
                print("Du greifst an, jedoch scheint dein Gegner keinerlei Schaden zu nehmen")
                print("Fliehen wäre eine gute Idee")
                print("Dein Gegner greift an")                
                if mySchutz >= itGegnerSchaden:
                    print("Deine Rüstung federt den kompletten Schaden ab")
                    ANGRIFF(environment)                
                elif mySchutz < itGegnerSchaden:
                    print("Du bekommst Schaden")
                    myLebenspunkte[0] = myLebenspunkte[0] + mySchutz[0] - itGegnerSchaden[0]
                    ANGRIFF(environment)
            elif itGegnerSchutz < mySchaden:
                itGegnerLebenspunkte[0] = itGegnerLebenspunkte[0] + itGegnerSchutz[0] - mySchaden[0]
                print("Du greifst an und triffst")
                print("Dein Gegner greift an")
                if mySchutz >= itGegnerSchaden:
                    print("Deine Rüstung federt den kompletten Schaden ab")
                    ANGRIFF(environment)                
                elif mySchutz < itGegnerSchaden:
                    print("Du bekommst Schaden")
                    myLebenspunkte[0] = myLebenspunkte[0] + mySchutz[0] - itGegnerSchaden[0]
                    ANGRIFF(environment)
    elif cmd == 'flüchte':
        print("Du verschwindest in Raum 1")
        room1(environment)
        
def room3(environment):
    print("SweetVictory!!!")
    room1(environment)
        
            
def Ending(environment):
    print("Du bist tot...")
    room1(environment)




def getcmd(cmdlist):
    
    cmd = input('\nWas tust du: ')
    cmd = cmd.lower() # Eingegebene Großbuchstaben werden klein
    
    if cmd in cmdlist:
        return cmd
    elif cmd == 'lege waffe ab':
        if 'faust' in myWaffe:
            print("Du trägst keine Waffe")
        elif 'messer' in myWaffe:
            print("Du legst {} ab. Sie wird dabei zerstört.".format(myWaffe[0]))
            myWaffe.remove('messer')
            myWaffe.append('Faust')
            myZerstörteWaffen.append('messer')
            mySchaden.remove(5)
            mySchaden.append(3)
            return getcmd(cmdlist)
        elif 'Laserknarre' in myWaffe:
            print("Du legst die Laserknarre ab. Sie wird dabei zerstört.")
            myWaffe.remove('Laserknarre')
            myWaffe.append('Faust')
            mySchaden.remove(6)
            mySchaden.append(3)
            return getcmd(cmdlist)
    
    else:
        print('Das kannst du hier nicht tun')
        return getcmd(cmdlist)


if __name__ == "__main__":
    environment = ["blub"]
    room1(environment)