'''
Created on 17.09.2018

@author: michaelgress
'''

myList = []
def room1(environment):
    
    cmdlist = ['umsehen', 'nimm schlüssel', 'zeige inventar', 'öffne tür',]
    cmd = getcmd(cmdlist)
    
    if cmd == 'umsehen':
        print('vor dir liegt ein schlüssel')
        room1(environment)
        
    elif cmd == 'nimm schlüssel':
        if 'schlüssel' in myList:
            print("Du hast den Schlüssel bereits genommen")
            room1(environment)
            
        else:
            print('du nimmst den Schlüssel')
            myList.append('schlüssel')
            room1(environment)
        
    elif cmd == 'zeige inventar':
        for x in myList:
            print(x)
        room1(environment)
            
    elif cmd == 'öffne tür':
        print('Die Tür...')
        
        if 'schlüssel' in myList:
            print("hurray!")
            room1(environment)
            
        else:
            print("du hast keinen schlüssel")
            room1(environment)
    
    

def getcmd(cmdlist):
    
    cmd = input('\nWas tust du: ')
    cmd = cmd.lower() # Eingegebene Großbuchstaben werden klein
    
    if cmd in cmdlist:
        return cmd
    
    else:
        print('Das kannst du hier nicht tun')
        return getcmd(cmdlist)


if __name__ == "__main__":
    environment = ["blub"]
    room1(environment)