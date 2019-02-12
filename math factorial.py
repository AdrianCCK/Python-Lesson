def recursive_factorial( base):
    if base == 1:
        return base
    else:
        return base * recursive_factorial(base - 1)

def factorial( base ):
    result = base
    while base > 1:
    #for i in range(base - 1):
        base = base - 1
        result = result *  base
    return result
    
print( factorial(8) )
