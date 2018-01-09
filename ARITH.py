def generateFirstThreeLine(listofnums, operation):
    returnList = []
    firstLine = listofnums[0]

    if(operation == "*"):
        secondLine = '*' + listofnums[1]
        firstDigitOfSecondNum = int(listofnums[1][0])
        lastProductOfTwoDigits = str(int(listofnums[0]) * int(listofnums[1]))
    elif(operation == "+"):
        secondLine = '+' + listofnums[1]
        lastProductOfTwoDigits = " " * (len(secondLine) - len(str(int(listofnums[0]) + int(listofnums[1])))) + (str(int(listofnums[0]) + int(listofnums[1])))
    elif(operation == "-"):
        secondLine = '-' + listofnums[1]
        if (len(str(int(listofnums[0]) - int(listofnums[1]))) > len(secondLine)):
            lastProductOfTwoDigits = " " * (len(str(int(listofnums[0]) - int(listofnums[1]))) - len(secondLine)) + (str(int(listofnums[0]) - int(listofnums[1])))
        else:
            lastProductOfTwoDigits = " " * (len(secondLine) - len(str(int(listofnums[0]) - int(listofnums[1])))) + (str(int(listofnums[0]) - int(listofnums[1])))

    if(int(listofnums[1]) < int(listofnums[0])):

        if(operation == "+"):
            thi = int(listofnums[0]) + int(listofnums[1])
        elif(operation == "*"):
            thi = int(listofnums[0]) * int(listofnums[1][len(listofnums[1]) - 1])
        else:
            thi = int(listofnums[0]) - int(listofnums[1])

        if(thi >= int(listofnums[1]) and len(str(thi)) >= len(str(secondLine))):
            firstDottedLine = "-" * len(str(thi))
        else:
            firstDottedLine = "-" * len(secondLine)

    else:
        firstDottedLine = "-" * len(secondLine)

    if(len(lastProductOfTwoDigits) < len(firstDottedLine)):
        print " " * (len(firstDottedLine) - 1) + firstLine
        print secondLine
        print firstDottedLine

    else:
        print " " * (len(lastProductOfTwoDigits) - len(listofnums[0])) + firstLine
        print " " * ((len(lastProductOfTwoDigits) - len(listofnums[1])) - 1) + secondLine
        print " " * (len(lastProductOfTwoDigits) - len(firstDottedLine)) + firstDottedLine

    returnList.append(len(firstDottedLine))
    returnList.append(len(lastProductOfTwoDigits))
    returnList.append(lastProductOfTwoDigits)
    return returnList

t = int(raw_input())

while t:
    a = (raw_input())
    if (a.find("*") > -1):
        listofnums = a.split('*')
        twoLengths = generateFirstThreeLine(listofnums, '*')
        x = len(listofnums[1]) - 1
        productForFinal = 0
        while x >= 0:
            productStr = str(int(listofnums[0]) * int(listofnums[1][x]))
            product = str(productStr + (" " * ((len(listofnums[1])-1) - x)))
            productForFinal += int(productStr + ("0" * ((len(listofnums[1])-1) - x)))
            if (len(productStr) >= 1 and twoLengths[0] > twoLengths[1]):
                print " " * (((twoLengths[1] - len(product)))+1) + product
            else:
                print " " * ((twoLengths[1] - len(product))) + product
            x-=1

        if(len(listofnums[1]) > 1):
            print " " * (twoLengths[0] - len(str(productForFinal))) + "-" * len(str(productForFinal))
            print " " * (twoLengths[0] - len(str(productForFinal))) + str(productForFinal)

    elif(a.find("+") > -1):
        listofnums = a.split('+')
        twoLengths = generateFirstThreeLine(listofnums, '+')
        print twoLengths[2]

    elif(a.find("-") > -1):
        listofnums = a.split('-')
        twoLengths = generateFirstThreeLine(listofnums, '-')
        print twoLengths[2]
    t-=1
