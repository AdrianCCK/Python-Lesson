def calculatePercentage(num, total):
    myresult = (num / total * 100)
    return round(myresult, 2)

num_value = input("Please enter the number value:")
total_value = input("Please enter the total value:")

print ("The number in percentage is", calculatePercentage(float (num_value), float(total_value)), "%")
