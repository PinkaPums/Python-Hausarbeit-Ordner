'''
Created on 17.09.2018

@author: michaelgress
'''

from random import randint

myTreffsicherheit = [1]
zufall = []

print("Hallo?!")


print("who?!")
zufall.append(randint(1,8))
print("What?!")

if myTreffsicherheit[0] in zufall:
    print("Oh no")
    zufall.remove(1)
    print("schlag ging daneben")
    zufall.append(randint(1,8))
else:
    print("Oh yeah")
    
for x in myTreffsicherheit:
    print(x)       
for x in zufall:
    print(x)
