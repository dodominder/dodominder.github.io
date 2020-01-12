from decimal import *

#set precision of Decimal numbers. The greater the precision, the more random numbers.
getcontext().prec = 100

def rootMe(x, n):
#This function uses the decimal module to give the nth root of the number x
    nthRoot = Decimal(x) ** (Decimal(1.0) / Decimal(n) )
    return nthRoot

"""cleanNumbers makes sure the given numbers can be used to create the table.
 It is called by the funciton createTable."""
def cleanNumbers(x,y):
    firstNumber = [int(d) for d in str(x)]
    secondNumber = [int(d) for d in str(y)]
    if (0 in firstNumber) or (1 in firstNumber) or (0 in secondNumber) or (1 in secondNumber):
        print("Neither number can contain a zero or a one.")
    elif (len(firstNumber) != len(secondNumber)):
        print("Neither number can contain a zero or a one.")
    else:
        count = 0
        for i, j in zip(firstNumber, secondNumber):
            if (Decimal(str(rootMe(i,j))) % 1 == 0):
                temp = firstNumber[count]
                firstNumber[count] = secondNumber[count]
                secondNumber[count] = temp
            count += 1
        return firstNumber, secondNumber

def createTable(x,y):
    """Creates a table of pseudo-random digits from the seed numbers x,y and outputs it to a text file called random_digits"""
    x, y = cleanNumbers(x,y)
    file = open("random_digits.txt","w+")
    for i, j in zip(x, y):
        file.write(str(rootMe(i,j))[2:]+"\n" )
    file.close()


#place seed numbers here
seed_number1 = 5372
seed_number2 = 6324

createTable(seed_number1,seed_number2)