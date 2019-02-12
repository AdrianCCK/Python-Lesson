import pygame
from pygame.transform import flip
class Chef(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.speed = [0, 0]
       self.width = width
       self.height = height

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       #self.image = pygame.Surface([width, height])
       self.image = pygame.image.load(r"C:\Users\User\AppData\Local\Programs\Python\Python36-32\626967311.png")

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       
       self.__x = self.rect.left
       self.__y = self.rect.top   
           
    def get_x(self ):
       return self.__x
    
    def set_x(self, x ):
       self.__x = x 
       self.rect.left = x
       
       if self.rect.left < 0 or self.rect.right > self.width:    
          self.image = flip(self.image, True, False) 
          
          self.speed[0] = -self.speed[0]
          
         
    def get_y(self ):
       return self.__y    
       
    def set_y(self, y ):
       self.__y = y   
       self.rect.top = y
       
       if self.rect.top < 0 or self.rect.bottom > self.height:
          self.speed[1] = -self.speed[1]
          self.image = flip(self.image, False, True)
    
       
          
    x = property(get_x, set_x)
    y = property(get_y, set_y)    
    
