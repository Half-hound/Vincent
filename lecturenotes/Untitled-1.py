def minimum (list):
    return min(list)

def maximum (list):
    return max(list)

print(maximum([0,1,2]))

def jingleballs (a,b):
    for i in range (a,b):
        if i==(b-1):
            print ("balls")
        else:
            print ("jingle")

print (jingleballs(1,111))

def isprime(num):
    if num >= 0 and num != type(int):
        return "rip bozo try again"
    else:
        if num == 1:
            return "neither"
        elif num == 2:
            return "prime"
        else:
            if num % 2 == 0:
                "composite"
            else:
                for i in range (2, num):
                    if num % i == 0:
                        return "composite"
                    else:
                        return "prime"

