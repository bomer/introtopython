#Takes screen input of a number, radius 
def getRadius():  
    r = input("Enter the Radius of your circle")
    #todo - ensure number is positive!
    return r

#Times it itself and then by pi to get area
def calculateRadius(r):
    pi=3.14 #mathematical constant
    result = r*r*pi
    return result

#Print out the result
def displayResult(result):
    print "Area of your circle is" + str(result)

displayResult(calculateRadius(getRadius()))

