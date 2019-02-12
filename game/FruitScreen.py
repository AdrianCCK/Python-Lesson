import turtle
from time import sleep


class FruitGame(object):

  def __init__(self):
    #super(FruitScreen,self).__init__()
    self.turtle = turtle.Turtle()
    self.screen = self.turtle.getscreen()

    
    self.screen.register_shape(r'game\apple.gif')
    self.screen.register_shape(r'game\banana.gif')
    self.turtle.penup()
    self.turtle.ht()
  
  def apple(self, n):
    self.turtle.shape(r'game\apple.gif') 
    self.drawfruit(n)
  def banana(self, n):
    self.turtle.shape(r'game\banana.gif') 
    self.drawfruit(n)
    
  def drawfruit(self, n):
    self.reset() 
    pos = self.turtle.pos()
    self.turtle.backward(300)
    for i in range(n):
      self.turtle.forward(60)    
      self.turtle.stamp() 
      self.turtle.left(90)
      self.turtle.forward(30)
      self.turtle.write( i+1,font=("Arial",30,"bold")  )
      self.turtle.backward(30)
      self.turtle.right(90)
                 
      if (i+1) % 10 == 0:
        self.turtle.setpos(pos)
        
        self.turtle.backward(300)
        self.turtle.right(90)
        self.turtle.forward((i/5)*50)
        self.turtle.left(90)
      else:
        sleep(0.5)
        
        
    self.turtle.setpos(pos)
  def reset(self): 
    self.screen.clear()
    self.turtle.penup()
    self.turtle.ht()
    #self.turtle.shape(r'C:\Users\user\Downloads\626967311.gif') 
    #screen.bgpic(r'C:\Users\user\Downloads\large_RW1.gif')
    self.screen.bgcolor("blue")
    
    self.turtle.color("yellow")