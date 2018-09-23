'''
Created on 16.09.2018

@author: michaelgress
'''
import time

mLP = [100] # myLebenspunbkte, Lebenspunkte des Spielers, LifePoints
mW = ['Faust'] # Ausgerüstete Waffe
mHP = [3] # ausgeübter Schaden, HitPoints
mI = [] # Inventar
mA = ["Unterhose"] # Kleidung, Rüstung
mS = [1] # Schutz der Kleidung
mG = [] #Zerstörte Gegenstände, Muell

iLP = [10]
iHP = [2]
iS = [1]


def ANGRIFF(environment): #HIER ENVIRONMENT ÄNDERN
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
            endingDeath(environment)    
        elif iLP[0] <= 0: ######
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Du hast den Gegner besiegt!!!")
            time.sleep(1)
            NÄCHSTERRAUM(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("Du greifst an...")
            if iS >= mHP: ######
                time.sleep(1)
                print("...jedoch scheint dein Gegner keinerlei Schaden zu nehmen.")
                print("Fliehen wäre eine gute Idee!")
                time.sleep(3)
                print("Dein Gegner greift an...")                
                if mS >= iHP: ######
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    ANGRIFF(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iHP: ######
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iHP[0] ######
                    time.sleep(1)
                    ANGRIFF(environment) #HIER ENVIRONMENT ÄNDERN
            elif iS < mHP: ######
                iLP[0] = iLP[0] + iS[0] - mHP[0] ######
                time.sleep(1)
                print("...und triffst!!")
                time.sleep(1)
                print("Dein Gegner greift an...")
                if mS >= iHP: ######
                    time.sleep(1)
                    print("...Deine Rüstung federt den kompletten Schaden ab!")
                    time.sleep(1)
                    ANGRIFF(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iHP: ######
                    time.sleep(1)
                    print("... und trifft dich!!!")
                    mLP[0] = mLP[0] + mS[0] - iHP[0] ######
                    time.sleep(1)
                    ANGRIFF(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flüchten':
        time.sleep(1)
        print("Du flüchtest!")
        time.sleep(1)
        VORHERIGERRAUM(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status gegner':
        if iLP >= [10]: ######
            print("Dein Gegner ist noch top fit!")
            ANGRIFF(environment) #HIER ENVIRONMENT ÄNDERN
        elif iLP >= [5]: ######
            print("Dein Gegner macht langsam schlapp!")
            ANGRIFF(environment) #HIER ENVIRONMENT ÄNDERN
        elif iLP >= [0]: ######
            print("Dein Gegner ist schwer verletzt, nur noch ein paar Treffer!")
            ANGRIFF(environment) #HIER ENVIRONMENT ÄNDERN
        

        