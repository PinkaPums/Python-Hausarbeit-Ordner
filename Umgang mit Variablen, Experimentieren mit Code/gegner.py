'''
Created on 16.09.2018

@author: michaelgress
'''

class Gegner():
    def __init__(self, name, lebenspunkte, rüstwert, schaden):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.rüstwert = rüstwert
        self.schaden = schaden
        
    def is_alive(self):
        return self.lebenspunkte > 0
    
class Verrückter(Gegner):
    def __init__(self):
        super().__init__(name="Verrückter", lebenspunkte=8, rüstwert=1, schaden=2)
        
class Infizierter(Gegner):
    def __init__(self):
        super().__init__(name="Infizierter", lebenspunkte=8, rüstwert=1, schaden=2)
        
class Infizierte(Gegner):
    def __init__(self):
        super().__init__(name="Infizierte", lebenspunkte=8, rüstwert=1, schaden=2)
        
class ToshiLazurra(Gegner):
    def __init__(self):
        super().__init__(name="Toshi Lazurra", lebenspunkte=28, rüstwert=4, schaden=8)   
        