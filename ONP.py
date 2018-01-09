t = int(raw_input().strip())

def calculateRPN(a):
    j = 0
    result = ""
    stack = []
    while j < len(a):
        if(a[j] != "(" and a[j] != "+" and a[j] != "-" and a[j] != "*" and a[j] != "/" and a[j] != "^" and a[j] != ")"):
            result = result + a[j]
        else:
            if(a[j] == ")"):
                rightparent = ""
                while(rightparent != "("):
                    pos = len(stack) - 1
                    first = stack.pop(pos)
                    rightparent = stack[pos-1]
                    result = result + first
                if(len(stack) != 0):
                    stack.pop(len(stack) - 1)
            else:
                precedence = 0
                if(a[j] == "+" or a[j] == "-"):
                    if (len(stack) != 0):
                        pos = 0
                        pos = len(stack) - 1
                        if (stack[pos] == "+" or stack[pos] == "-" or stack[pos] == "*" or stack[pos] == "/" or stack[pos] == "^"):
                            precedence = 1

                elif(a[j] == "*" or a[j] == "/"):
                    if (len(stack) != 0):
                        pos = 0
                        pos = len(stack) - 1
                        if (stack[pos] == "*" or stack[pos] == "/" or stack[pos] == "^"):
                            precedence = 1

                if (precedence == 1):
                    pos = 0
                    pos = len(stack) - 1
                    more = stack.pop(pos)
                    result = result + more
                    stack.append(a[j])
                else:
                    stack.append(a[j])

        if (j == len(a) - 1):
            newstack = [stack[-i] for i in range(1, len(stack) + 1)]
            result = result + "".join(newstack)
        j = j+1

    print result

for i in range(t):
    a = raw_input()
    calculateRPN(a)
