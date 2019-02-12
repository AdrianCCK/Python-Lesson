from game import *

c = Chef()
stamplist = []

import random

score = 0

while True:
    a = random.randint(1,15)
    b = random.randint(1,15)

    stamplist.append( c.stamp() )
    
    
    answer = input("What is %d X %d: " % (a , b) )
    answer = int(answer)

    if (a*b) == answer:
        print( 'Correct!')
        score = (score + 1)
        c.reset()
        for stamp in stamplist:
            c.clearstamp( stamp )
        
        stamplist = []
        
    else:
        print( 'Sorry, try again!')
        c.forward(100)
    
    print('Score:', (score))
    if len( stamplist) >= 3:
        print( 'Game Over')
        break





    
