import random
from game import *

c = Chef()
#p = Pokemon()
#p.penup()
#p.hide()

pokemons = ['pikachu', 'raichu', 'charmander', 'bulbasaur', 'squirtle', 'onyx']
keepwalking = True

while keepwalking:
    rannum = random.randint(0,12)
    input( 'press enter to move')

    if rannum < 6:
        print( 'You ran into a ',   pokemons[rannum] )
        #p.stamp()
    else:
        c.forward(10)
        #p.forward(10)
    
    if rannum == 12:
        keepwalking = False
