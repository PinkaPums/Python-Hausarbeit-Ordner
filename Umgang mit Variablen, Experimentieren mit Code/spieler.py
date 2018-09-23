'''
Created on 16.09.2018

@author: michaelgress
'''

import items

class Spieler():
    def __init__(self):
        self.inventar = []
        self.lebenspunkte = 100
        self.rüstwert = 0
        
    def is_alive(self):
        return self.hp > 0
    
    def nimmLaserknarre(self):
        