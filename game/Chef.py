import turtle
from time import sleep

class Chef(turtle.Turtle):

  def __init__(self): #constructor
    super(Chef,self).__init__()
    self.reset()
    
  def forward(self, n, label=False):
    super().forward(n/2)
    if label:
      self.write( '%.2f' % n,font=("Arial",16,"bold")  )
    super().forward(n/2)
    
  
  def backward(self, n, label=False):
    super().backward(n/2)
    if label:
      self.write( '%.2f' % n,font=("Arial",16,"bold")  )
    super().backward(n/2)
    
  def south(self,n):
    #oripos = self.pos()
    self.shape(r'game\626967311_s.gif')
    self.setheading(270)
    self.forward(n,label=True)
    
  def north(self,n):
    
    self.shape(r'game\626967311_n.gif')
    self.setheading(90)
    self.forward(n,label=True)
  
  def east(self,n):
    
    self.shape(r'game\626967311.gif')
    self.setheading(0)
    self.forward(n,label=True)
  
  def west(self,n):
    
    self.shape(r'game\626967311_w.gif')
    self.setheading(180)
    self.forward(n,label=True)
  
  def reset(self): 
    super(Chef,self).reset()
    self.screen = self.getscreen()
    self.shape(r'game\626967311.gif') 
    self.screen.bgpic(r'game\large_RW1.gif')
    
    
    self.color("white")
    self.shapesize(outline=8)

import random 
class CookingPerson(Chef):
  def __init__(self, name=""):  #constructor
    super(Chef,self).__init__()
    self.shape(r'game\banana.gif')
    self.age = 0
    self.name = name
    self.gender = 'M' if random.randint(0,1) else 'F'
    self.HP = 100
    self.reset()
  def heal( self, addedHP ):
    self.HP = self.HP + addedHP

  def eat( self, food ):
    self.HP = self.HP + 1

  def damage(self, dmgHP):
    self.HP = self.HP - dmgHP

  def reset(self): 
    super(Chef,self).reset()
    self.shape(r'game\banana.gif') 
'''
myself = Person()
yourself = Person()
himself = Person()
John = Person("John")

myself.damage( 50 )
myself.eat( "apple" )
print ( myself.name )
print ( myself.HP )


print ( John.name )
print ( John.HP )
'''





class Pokemon(turtle.Turtle):

  def __init__(self):  #constructor
    super(Pokemon,self).__init__()
    self.reset()
    
  def forward(self, n, label=False):
    super().forward(n/2)
    if label:
      self.write( '%.2f' % n,font=("Arial",16,"bold")  )
    super().forward(n/2)
    
  
  def backward(self, n, label=False):
    super().backward(n/2)
    if label:
      self.write( '%.2f' % n,font=("Arial",16,"bold")  )
    super().backward(n/2)
    
  def south(self,n):
    #oripos = self.pos()
    self.shape(r'game\banana.gif')
    self.setheading(270)
    self.forward(n,label=True)
    
  def north(self,n):
    
    self.shape(r'game\banana.gif')
    self.setheading(90)
    self.forward(n,label=True)
  
  def east(self,n):
    
    self.shape(r'game\banana.gif')
    self.setheading(0)
    self.forward(n,label=True)
  
  def west(self,n):
    
    self.shape(r'game\banana.gif')
    self.setheading(180)
    self.forward(n,label=True)
  
  def reset(self): 
    super(Pokemon,self).reset()
    self.screen = self.getscreen()
    self.shape(r'game\banana.gif') 
    self.screen.bgpic(r'game\large_RW1.gif')
    
    
    self.color("white")
    self.shapesize(outline=8)
