def power( base, powr ):
    result = base
    for i in range(powr - 1):
        result = result *  base
    return result

def recursive_power( base, power ):
    if power == 1:
        return base
    else:
        return base * recursive_power(base, power -1 )
    
print( recursive_power(2, 7) )
