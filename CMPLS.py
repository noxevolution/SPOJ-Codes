t = int(raw_input())

while t:
    S,C = map(int,raw_input().split())
    listOfNumbers = map(int,raw_input().split())
    listOfAddedNumbers = []
    difference = []
    op = []

    new_list = listOfNumbers[:]
    l = len(new_list)

    while (l >= 1):
        difference.append(new_list[-1])

        if(new_list.count(new_list[0]) == len(new_list)): # if the difference is equal then just exit the loop
            if(len(new_list) > 1): break

        new_list = [m - n for n, m in zip(new_list, new_list[1:])] # checking the difference.....

        l -= 1

    if(sum(listOfNumbers) == 0):
        difference = listOfNumbers[:]
    else:
        difference = difference[::-1] # reversing the difference list....


    while C > 0:
        difference = [sum(difference[:i+1]) for i in range(len(difference))] # sum of adjacent differences....
        op.append(str(difference[-1]))
        C-=1

    print ' '.join(op)
    t-=1
