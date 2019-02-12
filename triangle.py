def triangle_area( length, height): # input/ parameters / arguments
    myresult = length * height* (1/2)
    return float(myresult)


length = input("Please enter the length of the triangle base: ")
height = input("Please enter the height of the triangle: ")

print("The area of the rectangle is", triangle_area( float(length), float(height) ))

#int -> integer
#float, double -> decimal
# str -> string / text
