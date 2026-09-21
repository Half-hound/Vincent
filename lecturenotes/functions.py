name = "Vincent"

print("Hello,", name)
def say_hello(name):
    print("Hello,", name)

def add(a,b):
    return a+b

print(add (7,8))



def check_positive(num):
    if num > 0:
        return "positive"

    elif num < 0:
        return "negative"
    else:
        return 0

print(check_positive(3))

def help(temp):
    if 65 < temp < 80:
        return "i will die soon"
    elif temp > 80:
        return "im burning in hell"
    else: "im a popsicle"

print(help(70))