def inc(firsthalf):
    leftlist=list(firsthalf)
    last = len(firsthalf)-1

    while leftlist[last]=='9':
        leftlist[last]='0'
        last-=1

    leftlist[last] = str(int(leftlist[last])+1)
    return "".join(leftlist)

t = long(raw_input())

while t:
    a = (raw_input())
    palin = ""
    oddOrEven = len(a) % 2

    if oddOrEven:
        size = len(a) / 2
        center = a[size]
    else:
        size = 0
        center = ''

    firsthalf = a[0 : len(a)/2]
    secondhalf = firsthalf[::-1]
    palin = firsthalf + center + secondhalf

    if (palin <= a):
        if(size == 0 and center == ''):
            if firsthalf == len(firsthalf)*'9':
                palin = '1' + (len(a)-1)*'0' + '1'
            else:
                firsthalf = inc(firsthalf)
                palin = firsthalf + firsthalf[::-1]

        elif(size == 0 and center != ''):
            if(center < '9'):
                palin = int(center) + 1
            else:
                palin = '11'

        elif(size > 0):
            lastvalue = int(center) + 1

            if (lastvalue == 10):
                if firsthalf == len(firsthalf)*'9':
                    palin = '1' + (len(a)-1)*'0' + '1'
                else:
                    firsthalf = inc(firsthalf)
                    palin = firsthalf + '0' + firsthalf[::-1]
            else:
                palin = firsthalf + str(lastvalue) + secondhalf
    print palin
    t-=1
