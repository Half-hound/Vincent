def say_goodbye(name):
    print("Goodbye,", name)

def areacircle(r):
    return 3.14*(r**2)

def sub(a, b):
    return a - b

def mul(a, b):
    return (a*b)

def div(a,b):
    return (a/b)

def whatshouldiwear(readings):
    return (max(readings),min(readings))

def is_weekend(day:int):
    if day == 6 or day == 7:
        return True
    else:
        return False

def efficiency(dist,fuel):
    return dist/fuel

def encryption(code:int):
    return int(str(code%10) + str(code//10))

def power(num,powr):
    res = 1
    for i in range (0, powr):
        res = res*num
    return res


def minim(lis):
    for i in range(0, len(lis)):
        if i == 0:
            mini = lis[i]
        elif lis[i] < mini:
            mini = lis[i]
    return mini

def maxim(lis):
    for i in range(0, len(lis)):
        if i == 0:
            maxi = lis[i]
        elif lis[i] > maxi:
            maxi = lis[i]
    return maxi

def minimu(lis):
    lnth = len(lis)-1
    mini = lis[-1]
    while lnth > -1:
        if lis[lnth] < mini:
            mini = lis[lnth]
        lnth = lnth-1
    return mini

def maximu(lis):
    maxi = lis[-1]
    lnth = len(lis)-1
    while lnth > -1:
        if lis[lnth] > maxi:
            maxi = lis[lnth]
        lnth = lnth-1
    return maxi

def sumup(num:int):
    res=0
    for i in range(0, len(str(num))):
        res=int(str(num)[i]) + res
    return res

code = 83884
result = encryption(code) # code rearranged so that the last digit is the first
print(f"The result of encryption (5.4) with code = {code} is {result}.")


