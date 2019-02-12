def rectangle_area( width, height): # input/ parameters / arguments
    myresult = width * height
    return myresult

def rectangle_perimeter( width, height): # input/ parameters / arguments
    myresult = width * 2 + height * 2
    return myresult

width = input("Please enter the width of the rectangle: ")
height = input("Please enter the height of the rectangle: ")

print("The area of the rectangle is", rectangle_area( int(width), int(height) ))
print("The perimeter of the rectangle is", rectangle_perimeter( int(width), int(height) ))

#int -> integer
#float, double -> decimal
# str -> string / text
