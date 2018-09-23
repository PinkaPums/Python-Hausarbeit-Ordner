'''
Created on 16.09.2018

@author: michaelgress
'''

# Gegenstände/Items

class Item():
    
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung
        
    def __str__(self):
        return "{}\n{}\n".format(self.name, self.beschreibung)
    
    
    
class Waffen(Item):
    
    def __init__(self, name, beschreibung, schaden):
        self.schaden = schaden
        super().__init__(name, beschreibung,)
        
    def __str__(self):
        return "{}\n{}\n".format(self.name, self.beschreibung)
    
class Laserknarre(Waffen):
    def __init__(self):
        super().__init__(name="Laserknarre",
                         beschreibung="Eine Knarre die Laser schießt",
                         schaden=9)
class Rohr(Waffen):
    def __init__(self):
        super().__init__(name="Rohr",
                         beschreibung="Ein Rohr mit zwei Öffnungen",
                         schaden=6)
        
class Faust(Waffen):
    def __init__(self):
        super().__init__(name="Faust",
                         beschreibung="Rau und kräftig",
                         schaden=3)
        
class Blaster(Waffen):
    def __init__(self):
        super().__init__(name="Blaster",
                         beschreibung="Schießt Blitze, tödlich!",
                         schaden=14)
        
class Vaporisierer(Waffen):
    def __init__(self):
        super().__init__(name="Vaporisierer",
                         beschreibung="Wird damit ein Ziel getroffen, sinkt die Überlebenschance auf Null!!!",
                         schaden=9001)    
    