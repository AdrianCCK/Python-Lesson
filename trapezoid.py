def trapezoid_area( length_base, length_top, height): # input/ parameters / arguments
    myresult = (length_base+length_top) * height * (1/2)
    return float(myresult)


length_base = input("Please enter the length of the trapezoid base: ")
length_top = input("Please enter the length of the trapezoid top: ")
height = input("Please enter the heigth of the trapezoid: ")

print("The area of the trapezoid is", trapezoid_area( float(length_base), float(length_top), float(height) ))

#int -> integer
#float, double -> decimal
# str -> string / text
