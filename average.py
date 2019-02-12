def total(m):
    result = 0
    
    #for item in m:
    #    result = result + item
    #    print(item)
        #result = result + m[1]

    for i in range( 0, len(m) ):
        result = result + m[i]
        print(i)
    return result

def average(measurements):
    total_ = total(measurements)
    print("total is : ", total_)
    count = len(measurements)
    print("count is : ", count)
    result = total_ / count
    return result



def find_min(m):
    minimum = 999999999999999
    for i in range(0,len(m)):
        if minimum > m[i]:
            minimum = m[i]
        
    return minimum

def find_max(m):
    maximum = 0
    for i in range(0,len(m)):
        if maximum < m[i]:
            maximum = m[i]

    return maximum




measurements = [ 15.4, 14.9, 14.5, 15.0, 15.1, 14.7 ] #unsorted
result = average( measurements )
print("average is : ", result)
print("min is : ", find_min(measurements) )
print("max is : ", find_max(measurements) )

measurements.sort()
if len( measurements ) % 2 == 0:
    print( measurements[len(measurements)//2-1 ] )
    print( measurements[len(measurements)//2 ] )
    result = measurements[len(measurements)//2-1 ] + measurements[len(measurements)//2 ]
    print("median1 is : ", result/2.0 )
else:
    
    print("median2 is : ", measurements[len(measurements)//2 ] )
