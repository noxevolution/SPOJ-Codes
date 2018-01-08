def recur_factorial(a):
   if a == 1:
       return a
   else:
       return a*recur_factorial(a-1)

def upperBoundCal(b, a):
    x = 0
    mul = 1
    while x < a:
        val = b - x
        mul = mul * val
        x+=1
    return mul
    
t = int(raw_input())

while t:
    S,C = map(int,raw_input().split())
    listOfNumbers = map(int,raw_input().split())
    listOfAddedNumbers = []

    while C > 0:
        new_list = listOfNumbers[:]

        l = len(new_list)
        initial = listOfNumbers[0]
        i = 1

        while l != 1:
            new_list = [m - n for n, m in zip(new_list, new_list[1:])]
            thing = ((upperBoundCal((len(listOfNumbers)), i) / recur_factorial(i)) * new_list[0])
            initial = initial + thing
            l -= 1
            i += 1

        listOfAddedNumbers.append(initial)
        listOfNumbers.append(initial)

        C-=1

    print ' '.join(str(x) for x in listOfAddedNumbers)

    t-=1
